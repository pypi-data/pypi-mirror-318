import time
import hashlib
import json
import click
import requests
import logging
from sallmon_wallet.commands import wallet, utxo
from sallmon_wallet.commands.utxo import get_utxos_for_wallet, derive_utxos, fetch_blockchain
from sallmon_wallet.commands.mining import send_block_to_endpoint
from sallmon_wallet.commands.mempool import get_mempool
from sallmon_wallet.services.database import get_db_connection

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DIFFICULTY = 4  # Number of leading zeroes required in the hash


@click.group()
def cli():
    """Sallmon Wallet System"""
    pass


@cli.command()
def create_wallet():
    """Create a new wallet and display the address."""
    address = wallet.generate_wallet()
    click.echo(f"New wallet address created: {address}")


@cli.command()
def list_wallets():
    """List all wallets."""
    wallets = wallet.load_wallets()
    if not wallets:
        click.echo("No wallets found.")
        return

    for idx, w in enumerate(wallets, 1):
        click.echo(f"{idx}. Address: {w['address']}")


@cli.command()
@click.option("--address", prompt="Wallet Address", help="The wallet address to check the balance for.")
def check_balance(address):
    """Check the balance of a wallet address."""
    blockchain = fetch_blockchain()
    if not blockchain:
        click.echo("Failed to fetch the blockchain.")
        return

    utxos = derive_utxos(address, blockchain)
    balance = sum(utxo["amount"] for utxo in utxos)
    click.echo(f"Balance for {address}: {float(balance):.1f}")


@cli.command()
@click.option("--address", "address", required=True, help="The wallet address to spend funds from.")
@click.option("--amount", "amount", required=True, type=float, help="The amount to transfer.")
@click.option("--recipient", "recipient", required=True, help="The recipient's wallet address.")
def spend_utxo(address, amount, recipient):
    """Spend UTXOs to create a transaction."""
    logging.info(f"💸 Attempting to spend {amount} from {address} to {recipient}.")

    try:
        # Call the spend_utxo function and handle exceptions
        utxo.spend_utxo(address, amount, recipient)
        click.echo(f"✅ Successfully sent {amount} from {address} to {recipient}.")
    except ValueError as e:
        logging.error(f"❌ Transaction error: {str(e)}")
        click.echo(f"Error: {str(e)}")
    except Exception as e:
        logging.error(f"❌ Unexpected error: {str(e)}")
        click.echo(f"Error: {str(e)}")

#def spend_utxo(address, amount, recipient):
#    """Spend UTXOs to create a transaction."""
#    try:
#        utxo.spend_utxo(address, amount, recipient)
#        click.echo(f"Successfully sent {amount} from {address} to {recipient}.")
#    except ValueError as e:
#        click.echo(f"Error: {str(e)}")


def proof_of_work(block):
    """Perform Proof of Work to find a valid nonce."""
    block["nonce"] = 0
    block_string = json.dumps(block, sort_keys=True)
    while not hashlib.sha256(block_string.encode()).hexdigest().startswith("0" * DIFFICULTY):
        block["nonce"] += 1
        block_string = json.dumps(block, sort_keys=True)
    block["hash"] = hashlib.sha256(block_string.encode()).hexdigest()
    return block


@cli.command()
@click.option("--address", prompt="Miner Address", help="The wallet address of the miner.")
@click.option("--broadcast", is_flag=True, help="Broadcast the mined block to peers.")
@click.option("--endpoint", default="http://localhost:1337", help="The endpoint of the blockchain node.")
def mine(address, broadcast, endpoint):
    """Mine a new block using Proof of Work."""
    transactions = get_mempool()
    if not transactions:
        click.echo("No transactions in the mempool. Mining block with only coinbase transaction.")
        transactions = []

    # Add coinbase transaction
    coinbase_transaction = {"sender": "System", "recipient": address, "amount": 50}
    transactions.append(coinbase_transaction)

    # Fetch the latest block from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT block_index, hash FROM blocks ORDER BY block_index DESC LIMIT 1")
    latest_block = cursor.fetchone()
    if latest_block:
        previous_hash = latest_block[1]
        index = latest_block[0] + 1
    else:
        previous_hash = "static_genesis_hash"
        index = 0
    conn.close()

    # Create the block
    block = {
        "index": index,
        "previous_hash": previous_hash,
        "timestamp": int(time.time()),
        "data": transactions,
    }
    click.echo("Starting Proof of Work...")
    block = proof_of_work(block)
    click.echo(f"Block mined with nonce: {block['nonce']} and hash: {block['hash']}")

    # Broadcast the block
    if broadcast:
        click.echo(f"Broadcasting block to {endpoint}/broadcast-block...")
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(f"{endpoint}/broadcast-block", json=block, headers=headers)
            if response.status_code == 200:
                click.echo("Block broadcasted successfully!")
            else:
                click.echo(f"Failed to broadcast the block. Status code: {response.status_code}")
        except requests.RequestException as e:
            click.echo(f"Error broadcasting block: {e}")
    else:
        click.echo("Broadcast flag not set. Block not broadcasted or stored.")



@cli.command()
def show_mempool():
    """Show the current mempool with pending transactions."""
    mempool = get_mempool()
    if not mempool:
        click.echo("Mempool is empty.")
    else:
        click.echo("Current Mempool:")
        for tx in mempool:
            click.echo(tx)


@cli.command()
@click.option("--endpoint", default="http://localhost:1337", help="The endpoint of the blockchain node.")
def sync_blockchain(endpoint):
    """Sync the local blockchain with peers."""
    try:
        response = requests.get(f"{endpoint}/blocks")
        if response.status_code == 200:
            blockchain = response.json()
            # Implement save_blockchain() logic here
            click.echo("Blockchain synced successfully!")
        else:
            click.echo(f"Failed to sync blockchain: {response.status_code} {response.text}")
    except requests.RequestException as e:
        click.echo(f"Error syncing blockchain: {e}")


if __name__ == "__main__":
    cli()
