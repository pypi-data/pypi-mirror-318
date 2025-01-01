import hashlib
import json
import sqlite3
import time
import os

BLOCKCHAIN_DB = os.path.expanduser("~/.sallmon/blockchain.db")

def generate_address(public_key):
    """Generate a wallet address from the public key."""
    return hashlib.sha256(public_key.to_string()).hexdigest()[:40]

def calculate_balance(address):
    """Calculate wallet balance based on UTXOs."""
    conn = sqlite3.connect(BLOCKCHAIN_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM blocks")
    blocks = cursor.fetchall()
    conn.close()

    spent_outputs = set()
    utxos = []

    for block in blocks:
        block_data = json.loads(block[0])
        transactions = block_data.get("transactions", [])
        for tx in transactions:
            for idx, output in enumerate(tx.get("outputs", [])):
                if output["to"] == address and f"{tx['id']}:{idx}" not in spent_outputs:
                    utxos.append(output)
            for input_tx in tx.get("inputs", []):
                spent_outputs.add(f"{input_tx['tx_id']}:{input_tx['index']}")

    return sum(utxo["amount"] for utxo in utxos)

def mine_block_locally(address):
    """Mine a block locally."""
    previous_hash = "0" * 64
    transactions = [{"to": address, "amount": 10, "type": "reward"}]

    block = {
        "index": 1,
        "previous_hash": previous_hash,
        "transactions": transactions,
        "nonce": 0,
    }

    while True:
        block_string = json.dumps(block, sort_keys=True).encode()
        block_hash = hashlib.sha256(block_string).hexdigest()
        if block_hash.startswith("0000"):
            block["hash"] = block_hash
            break
        block["nonce"] += 1

    return block

def broadcast_block(block):
    """Broadcast the block."""
    # Placeholder for broadcasting logic
    print("Block broadcasted:", block)
