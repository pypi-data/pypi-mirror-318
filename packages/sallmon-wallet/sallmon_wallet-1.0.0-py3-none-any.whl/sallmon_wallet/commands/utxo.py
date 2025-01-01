import os
import json
import requests
import logging
import sqlite3

# Constants
UTXO_FILE = os.path.expanduser("~/.sallmon_wallet/utxos.json")
TRANSACTION_BROADCAST_ENDPOINT = "http://localhost:1337/broadcast-transaction/"
DB_PATH = os.path.expanduser("~/.sallmon/blockchain.db")

# Logging Configuration
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


# --- UTXO File Operations ---
def load_utxos():
    """📤 Load all UTXOs from the UTXO file."""
    if not os.path.exists(UTXO_FILE):
        logging.debug("🔍 UTXO file not found. Returning an empty UTXO set.")
        return {}
    try:
        with open(UTXO_FILE, "r") as f:
            utxos = json.load(f)
            logging.debug(f"📂 Loaded {len(utxos)} UTXOs from file.")
            return utxos
    except Exception as e:
        logging.error(f"❌ Error loading UTXO file: {e}")
        return {}


def save_utxos(utxos):
    """💾 Save UTXOs to the UTXO file."""
    try:
        os.makedirs(os.path.dirname(UTXO_FILE), exist_ok=True)
        with open(UTXO_FILE, "w") as f:
            json.dump(utxos, f, indent=4)
        logging.debug("✅ UTXOs saved successfully.")
    except Exception as e:
        logging.error(f"❌ Error saving UTXOs: {e}")


# --- UTXO Management ---
def add_utxo(wallet_address, tx_id, index, amount):
    """➕ Add a UTXO for a specific wallet address."""
    logging.debug(f"➕ Adding UTXO: TX_ID={tx_id}, Index={index}, Amount={amount} for wallet {wallet_address}.")
    utxos = load_utxos()
    if wallet_address not in utxos:
        utxos[wallet_address] = []
    utxo_key = {"tx_id": tx_id, "index": index, "amount": amount}
    if utxo_key not in utxos[wallet_address]:
        utxos[wallet_address].append(utxo_key)
        save_utxos(utxos)
        logging.info(f"🪙 Added UTXO successfully: {utxo_key}.")
    else:
        logging.warning(f"⚠️ Duplicate UTXO detected: {utxo_key}. Not added.")


def get_utxos_for_wallet(wallet_address):
    """🧾 Derive UTXOs dynamically from the blockchain for a specific wallet."""
    logging.info(f"🔍 Fetching UTXOs for wallet: {wallet_address}.")
    blockchain = fetch_blockchain()
    if not blockchain:
        logging.error("❌ Failed to fetch the blockchain.")
        return []

    utxos = derive_utxos(wallet_address, blockchain)
    logging.info(f"🔍 Found {len(utxos)} UTXOs for wallet {wallet_address}.")
    return utxos


def derive_utxos(wallet_address, blockchain):
    """
    Derive UTXOs for the given wallet address from the blockchain.
    """
    logging.info(f"🔍 Deriving UTXOs for wallet {wallet_address}.")
    utxos = []
    spent_outputs = set()

    for block in blockchain:
        block_index = block.get("block_index")
        block_data = block.get("data", [])

        if not block_data:
            logging.warning(f"⚠️ Block {block_index} has no transaction data. Skipping.")
            continue

        for tx in block_data:
            # Identify and record spent outputs
            if "inputs" in tx:
                for tx_input in tx["inputs"]:
                    spent_outputs.add((tx_input["tx_id"], tx_input["index"]))
                    logging.debug(f"🔻 Marked output as spent: {tx_input}.")

            # Identify unspent outputs
            if "recipient" in tx and tx["recipient"] == wallet_address:
                utxo_key = (block["hash"], 0)  # Coinbase transactions use index 0
                if utxo_key not in spent_outputs:
                    utxos.append({
                        "tx_id": block["hash"],
                        "index": 0,
                        "amount": tx["amount"]
                    })
                    logging.debug(f"🟢 Found UTXO: TX_ID={block['hash']}, Index=0, Amount={tx['amount']}.")

    logging.info(f"🧾 Derived {len(utxos)} UTXOs for wallet {wallet_address}.")
    return utxos


# --- Blockchain Fetch ---
def fetch_blockchain():
    """Fetch the blockchain from the SQLite database."""
    logging.debug("🌐 Fetching blockchain from SQLite database.")
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        query = '''
        SELECT block_index, previous_hash, timestamp, data, hash FROM blocks
        ORDER BY block_index ASC
        '''
        cursor.execute(query)
        rows = cursor.fetchall()

        blockchain = []
        for row in rows:
            try:
                block_data = json.loads(row[3]) if row[3] else None
            except json.JSONDecodeError as e:
                logging.warning(f"⚠️ Invalid JSON in block data at block_index {row[0]}: {e}")
                block_data = None  # Fallback to None for invalid JSON

            block = {
                "block_index": row[0],
                "previous_hash": row[1],
                "timestamp": row[2],
                "data": block_data,
                "hash": row[4],
            }
            blockchain.append(block)

        connection.close()
        logging.info(f"🌐 Blockchain fetched with {len(blockchain)} blocks.")
        return blockchain

    except sqlite3.Error as e:
        logging.error(f"❌ Database error: {e}")
        return []


def spend_utxo(wallet_address, amount, recipient):
    """Spend UTXOs and create a transaction."""
    logging.info(f"💸 Attempting to spend {amount} from {wallet_address} to {recipient}.")
    
    # Fetch UTXOs
    utxos = get_utxos_for_wallet(wallet_address)
    total, inputs = 0, []

    logging.debug(f"🔍 Available UTXOs: {utxos}")

    # Select UTXOs to fulfill the transaction amount
    for utxo in utxos:
        inputs.append({"tx_id": utxo["tx_id"], "index": utxo["index"]})
        total += utxo["amount"]
        if total >= amount:
            break

    if total < amount:
        logging.error("❌ Insufficient funds.")
        raise ValueError("Insufficient funds")

    # Create transaction outputs
    outputs = [{"recipient": recipient, "amount": amount}]
    if total > amount:  # Add change output
        outputs.append({"recipient": wallet_address, "amount": total - amount})

    # Explicitly include transaction metadata
    transaction = {
        "inputs": inputs,
        "outputs": outputs,
        "sender": wallet_address,
        "recipient": recipient,
        "amount": amount
    }

    logging.debug(f"📤 Created transaction: {transaction}")

    # Broadcast the transaction
    broadcast_transaction(transaction)
    logging.info(f"✅ Transaction successfully created and broadcasted: {transaction}.")

def broadcast_transaction(transaction):
    """Broadcast the transaction to the network."""
    logging.info(f"🌐 Broadcasting transaction: {transaction}.")
    try:
        response = requests.post(TRANSACTION_BROADCAST_ENDPOINT, json=transaction)
        logging.debug(f"🌐 Server response status code: {response.status_code}")
        logging.debug(f"🌐 Server response body: {response.text}")
        if response.status_code == 200:
            logging.info(f"🌐 Transaction broadcasted successfully: {transaction}.")
        else:
            logging.warning(f"⚠️ Transaction broadcast failed. Server responded with: {response.text}")
            logging.debug(f"Transaction data sent: {transaction}")
    except requests.RequestException as e:
        logging.error(f"❌ Error broadcasting transaction: {e}")
