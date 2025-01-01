import subprocess
import json
import os
import unittest


class TestCLI(unittest.TestCase):
    def setUp(self):
        """Set up a clean environment for testing."""
        self.wallet_file = os.path.expanduser("~/.sallmon/wallet.json")
        self.utxo_file = os.path.expanduser("~/.sallmon/utxos.json")

        # Backup and clear wallet and UTXO files
        self.wallet_backup = None
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, "r") as f:
                self.wallet_backup = f.read()
            os.remove(self.wallet_file)

        self.utxo_backup = None
        if os.path.exists(self.utxo_file):
            with open(self.utxo_file, "r") as f:
                self.utxo_backup = f.read()
            os.remove(self.utxo_file)

    def tearDown(self):
        """Restore the original environment."""
        if self.wallet_backup:
            with open(self.wallet_file, "w") as f:
                f.write(self.wallet_backup)
        if self.utxo_backup:
            with open(self.utxo_file, "w") as f:
                f.write(self.utxo_backup)

    def run_cli(self, command):
        """Run a CLI command and return the output."""
        result = subprocess.run(
            ["python3", "cli.py"] + command,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    def test_create_wallet(self):
        """Test creating a new wallet."""
        output = self.run_cli(["create-wallet"])
        self.assertIn("New wallet address created:", output)

        # Verify the wallet file
        with open(self.wallet_file, "r") as f:
            wallets = json.load(f)
        self.assertEqual(len(wallets), 1)

    def test_list_wallets(self):
        """Test listing wallets."""
        # Create two wallets
        self.run_cli(["create-wallet"])
        self.run_cli(["create-wallet"])

        output = self.run_cli(["list-wallets"])
        self.assertIn("1. Address:", output)
        self.assertIn("2. Address:", output)

    def test_check_balance(self):
        """Test checking balance."""
        # Create a wallet and add UTXOs
        address = self.run_cli(["create-wallet"]).split(": ")[-1]
        self.run_cli(["add-utxo", "--address", address, "--tx-id", "tx1", "--index", "0", "--amount", "100"])
        self.run_cli(["add-utxo", "--address", address, "--tx-id", "tx2", "--index", "1", "--amount", "50"])

        # Check balance
        output = self.run_cli(["check-balance", "--address", address])
        self.assertIn(f"Balance for {address}: 150.0", output)

    def test_add_and_spend_utxo(self):
        """Test adding and spending UTXOs."""
        address = self.run_cli(["create-wallet"]).split(": ")[-1]

        # Add UTXO
        self.run_cli(["add-utxo", "--address", address, "--tx-id", "tx1", "--index", "0", "--amount", "50"])
        output = self.run_cli(["check-balance", "--address", address])
        self.assertIn(f"Balance for {address}: 50.0", output)

        # Spend UTXO
        self.run_cli(["spend-utxo", "--address", address, "--tx-id", "tx1", "--index", "0"])
        output = self.run_cli(["check-balance", "--address", address])
        self.assertIn(f"Balance for {address}: 0.0", output)


def test_mine_block(self):
    """Test mining a block and updating the miner's UTXOs."""
    miner_address = self.run_cli(["create-wallet"]).split(": ")[-1]

    # Mine a block
    output = self.run_cli(["mine", "--address", miner_address])
    print("Mine Command Output:", output)  # Debugging step
    mined_block = json.loads(output)["Mined block"]  # Parse JSON output

    # Verify the block content (coinbase transaction)
    self.assertIn("transactions", mined_block)
    self.assertEqual(len(mined_block["transactions"]), 1)
    coinbase_tx = mined_block["transactions"][0]
    self.assertEqual(coinbase_tx["recipient"], miner_address)
    self.assertEqual(coinbase_tx["amount"], 50)

    # Verify the miner's balance
    balance_output = self.run_cli(["check-balance", "--address", miner_address])
    self.assertIn(f"Balance for {miner_address}: 50.0", balance_output)

def test_mine_and_broadcast_block(self):
    """Test mining a block and broadcasting it."""
    miner_address = self.run_cli(["create-wallet"]).split(": ")[-1]

    # Mine and broadcast the block
    output = self.run_cli(["mine", "--address", miner_address, "--broadcast"])
    print("Mine and Broadcast Output:", output)  # Debugging step
    mined_block = json.loads(output.split("\n")[0])["Mined block"]  # Parse JSON output

    # Verify the block content
    self.assertIn("transactions", mined_block)
    self.assertEqual(len(mined_block["transactions"]), 1)
    coinbase_tx = mined_block["transactions"][0]
    self.assertEqual(coinbase_tx["recipient"], miner_address)
    self.assertEqual(coinbase_tx["amount"], 50)

    # Verify the miner's balance
    balance_output = self.run_cli(["check-balance", "--address", miner_address])
    self.assertIn(f"Balance for {miner_address}: 50.0", balance_output)


if __name__ == "__main__":
    unittest.main()
