import os
import json
import unittest
from sallmon_wallet.commands.utxo import load_utxos, save_utxos, get_utxos_for_wallet, add_utxo, spend_utxo

class TestUTXO(unittest.TestCase):
    def setUp(self):
        """Set up a test UTXO file."""
        self.utxo_file = os.path.expanduser("~/.sallmon/utxos_test.json")
        self.original_file = os.path.expanduser("~/.sallmon/utxos.json")
        self.sample_wallet = "1E8bZc5wVior9ZrmBySJwYwL6obRj4zUyz"

        # Redirect the UTXO file path for testing
        global UTXO_FILE
        UTXO_FILE = self.utxo_file

        # Start with a clean slate
        if os.path.exists(self.utxo_file):
            os.remove(self.utxo_file)

    def tearDown(self):
        """Clean up the test UTXO file."""
        if os.path.exists(self.utxo_file):
            os.remove(self.utxo_file)

    def test_add_utxo(self):
        """Test adding a UTXO."""
        add_utxo(self.sample_wallet, "tx1", 0, 50)
        utxos = get_utxos_for_wallet(self.sample_wallet)
        self.assertEqual(len(utxos), 1)
        self.assertEqual(utxos[0]["amount"], 50)

    def test_spend_utxo(self):
        """Test spending a UTXO."""
        add_utxo(self.sample_wallet, "tx1", 0, 50)
        spend_utxo(self.sample_wallet, "tx1", 0)
        utxos = get_utxos_for_wallet(self.sample_wallet)
        self.assertEqual(len(utxos), 0)

    def test_get_utxos_for_wallet(self):
        """Test retrieving UTXOs for a wallet."""
        add_utxo(self.sample_wallet, "tx1", 0, 50)
        add_utxo(self.sample_wallet, "tx2", 1, 30)
        utxos = get_utxos_for_wallet(self.sample_wallet)
        self.assertEqual(len(utxos), 2)
        self.assertEqual(utxos[0]["amount"], 50)
        self.assertEqual(utxos[1]["amount"], 30)

    def test_utxos_persistence(self):
        """Test that UTXOs persist across operations."""
        add_utxo(self.sample_wallet, "tx1", 0, 50)
        add_utxo(self.sample_wallet, "tx2", 1, 30)

        # Reload UTXOs from file
        utxos = load_utxos()
        self.assertIn(self.sample_wallet, utxos)
        self.assertEqual(len(utxos[self.sample_wallet]), 2)

    def test_save_and_load_utxos(self):
        """Test saving and loading UTXOs."""
        utxos = {self.sample_wallet: [{"tx_id": "tx1", "index": 0, "amount": 50}]}
        save_utxos(utxos)
        loaded_utxos = load_utxos()
        self.assertIn(self.sample_wallet, loaded_utxos)
        self.assertEqual(loaded_utxos[self.sample_wallet][0]["amount"], 50)


if __name__ == "__main__":
    unittest.main()
