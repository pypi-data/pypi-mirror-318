import sqlite3
import logging
from sallmon_wallet.config import DB_PATH

logging.basicConfig(level=logging.INFO)

def get_connection():
    """Get a connection to the database and ensure the transactions table exists."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create the transactions table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        recipient TEXT,
        amount REAL,
        timestamp TEXT
    )
    """)
    conn.commit()
    return conn

def get_mempool():
    """Fetch all transactions from the transactions table."""
    conn = get_connection()
    logging.info("Fetching transactions from the transactions table...")
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, sender, recipient, amount, timestamp FROM transactions")
        transactions = [{"tx_id": row[0], "sender": row[1], "recipient": row[2], "amount": row[3], "timestamp": row[4]} for row in cursor.fetchall()]
    except sqlite3.Error as e:
        logging.error(f"Error fetching transactions from the transactions table: {e}")
        transactions = []
    finally:
        conn.close()
    
    return transactions

def remove_from_mempool(tx_ids):
    """Remove processed transactions from the transactions table."""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.executemany("DELETE FROM transactions WHERE id = ?", [(tx_id,) for tx_id in tx_ids])
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error removing transactions from transactions table: {e}")
    finally:
        conn.close()
