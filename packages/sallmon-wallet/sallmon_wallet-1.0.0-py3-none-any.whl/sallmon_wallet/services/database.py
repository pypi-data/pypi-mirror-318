import sqlite3
import os

def get_db_connection():
    """Get a database connection."""
    db_path = os.path.expanduser("~/.sallmon/blockchain.db")
    conn = sqlite3.connect(db_path)
    return conn
