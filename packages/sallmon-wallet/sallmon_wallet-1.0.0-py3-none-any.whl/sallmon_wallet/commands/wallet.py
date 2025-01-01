import os
import json
import hashlib
import ecdsa
import base58

WALLET_FILE = os.path.expanduser("~/.sallmon/wallet.json")


def generate_wallet():
    """Generate a new wallet and return its details."""
    # Step 1: Generate a private key
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.verifying_key

    # Step 2: Generate a wallet address (Base58Check encoding)
    sha256_pk = hashlib.sha256(public_key.to_string()).digest()
    ripemd160_pk = hashlib.new("ripemd160", sha256_pk).digest()
    wallet_address = base58.b58encode_check(b"\x00" + ripemd160_pk).decode()

    # Step 3: Save the wallet
    wallet_data = {
        "private_key": private_key.to_string().hex(),
        "public_key": public_key.to_string().hex(),
        "address": wallet_address,
    }
    save_wallet(wallet_data)
    return wallet_address


def save_wallet(wallet_data):
    """Save a new wallet to the wallet file."""
    os.makedirs(os.path.dirname(WALLET_FILE), exist_ok=True)
    if not os.path.exists(WALLET_FILE):
        wallets = []
    else:
        with open(WALLET_FILE, "r") as f:
            wallets = json.load(f)

    wallets.append(wallet_data)

    with open(WALLET_FILE, "w") as f:
        json.dump(wallets, f, indent=4)


def load_wallets():
    """Load all wallets from the wallet file."""
    if not os.path.exists(WALLET_FILE):
        return []
    with open(WALLET_FILE, "r") as f:
        return json.load(f)
