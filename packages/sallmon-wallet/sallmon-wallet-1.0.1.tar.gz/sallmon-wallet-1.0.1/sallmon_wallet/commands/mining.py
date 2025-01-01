import time
import hashlib
import json
import logging
from sallmon_wallet.commands.utxo import add_utxo
from sallmon_wallet.commands.mempool import get_mempool, remove_from_mempool
from sallmon_wallet.services.database import get_db_connection

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("mining")

def mine_block(miner_address):
    """
    Perform the mining process to create a new block.
    If no transactions are available in the mempool, only the coinbase transaction is included.
    """
    logger.info("Starting the mining process...")
    try:
        # Fetch the latest block from the database
        conn = get_db_connection()
        cursor = conn.cursor()

        logger.info("Fetching the latest block from the database...")
        cursor.execute("SELECT block_index, hash FROM blocks ORDER BY block_index DESC LIMIT 1")
        latest_block = cursor.fetchone()

        if latest_block:
            block_index, previous_hash = latest_block
            block_index += 1
            logger.info(f"Latest block: Index {block_index - 1}, Hash {previous_hash}")
        else:
            # No previous block found, use the genesis block settings
            logger.warning("No previous block found. Using genesis block settings.")
            previous_hash = "static_genesis_hash"
            block_index = 0

        # Fetch transactions from the mempool
        logger.info("Fetching transactions from the mempool...")
        transactions = get_mempool()
        if not transactions:
            logger.warning("No transactions in the mempool. Mining block with only coinbase transaction.")
            transactions = []

        # Add the coinbase transaction
        logger.info(f"Adding coinbase transaction for miner: {miner_address}")
        coinbase_transaction = {
            "sender": "System",
            "recipient": miner_address,
            "amount": 50,  # Mining reward
        }
        transactions.append(coinbase_transaction)

        # Create the new block
        logger.info("Creating a new block...")
        block = {
            "index": block_index,
            "previous_hash": previous_hash,
            "timestamp": int(time.time()),
            "data": transactions,
        }

        # Calculate the hash with Proof of Work
        logger.info("Performing proof of work...")
        block["hash"] = proof_of_work(block)

        # Persist the block to the database
        logger.info("Saving the new block to the database...")
        cursor.execute('''
            INSERT INTO blocks (block_index, previous_hash, timestamp, data, hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            block["index"],
            block["previous_hash"],
            block["timestamp"],
            json.dumps(block["data"]),  # Ensure data is stored as JSON
            block["hash"]
        ))
        conn.commit()

        # Update the UTXOs for the miner
        logger.info("Updating UTXOs for the miner...")
        add_utxo(miner_address, tx_id=block["hash"], index=0, amount=coinbase_transaction["amount"])

        # Clear processed transactions from the mempool
        tx_ids = [tx.get("tx_id") for tx in transactions if "tx_id" in tx]
        if tx_ids:
            logger.info(f"Removing {len(tx_ids)} transactions from the mempool.")
            remove_from_mempool(tx_ids)

        conn.close()

        logger.info(f"Block mined successfully! Block index: {block_index}, Hash: {block['hash']}")
        return block

    except Exception as e:
        logger.error(f"Error during the mining process: {e}")
        return None


def proof_of_work(block, difficulty=4):
    """
    Perform Proof of Work for the given block.
    The hash must start with 'difficulty' number of leading zeros.
    """
    block_string = json.dumps(block, sort_keys=True)
    nonce = 0

    while True:
        # Append the nonce and calculate the hash
        test_string = f"{block_string}{nonce}"
        hash_result = hashlib.sha256(test_string.encode()).hexdigest()

        if hash_result.startswith("0" * difficulty):
            logger.info(f"Proof of work completed. Nonce: {nonce}, Hash: {hash_result}")
            block["nonce"] = nonce
            return hash_result  # Return the valid hash

        nonce += 1


def send_block_to_endpoint(block, endpoint):
    """Send the mined block to the given API endpoint."""
    payload = {
        "index": block["index"],
        "previous_hash": block["previous_hash"],
        "timestamp": block["timestamp"],
        "data": block["data"],
        "hash": block["hash"]
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        if response.status_code == 200:
            logger.info("Block successfully sent to the endpoint.")
            return True
        else:
            logger.error(f"Failed to send block to endpoint. Status code: {response.status_code}")
            return False
    except requests.RequestException as e:
        logger.error(f"Error sending block to endpoint: {e}")
        return False
