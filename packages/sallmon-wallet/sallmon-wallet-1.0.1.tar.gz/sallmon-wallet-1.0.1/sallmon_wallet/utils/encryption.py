import os
import json
from ecdsa import SigningKey, SECP256k1

WALLET_PATH = os.path.expanduser("~/.sallmon-wallet/wallet.json")

def generate_keypair():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

def save_wallet(private_key, password):
    with open(WALLET_PATH, "w") as wallet_file:
        wallet_file.write(private_key.to_pem().decode())

def load_wallet(password):
    try:
        with open(WALLET_PATH, "r") as wallet_file:
            private_key = SigningKey.from_pem(wallet_file.read().encode())
        return private_key
    except Exception as e:
        print(f"Error loading wallet: {e}")
        return None

import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def decrypt_data(encrypted_data, password):
    decoded_data = base64.b64decode(encrypted_data)
    salt, iv, ciphertext = decoded_data[:16], decoded_data[16:32], decoded_data[32:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()
