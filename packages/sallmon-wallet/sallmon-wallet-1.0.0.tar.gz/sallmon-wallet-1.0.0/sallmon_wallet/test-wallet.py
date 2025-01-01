import json
from utils.encryption import decrypt_data
from ecdsa import SigningKey

wallet_path = "/home/c80129b/.sallmon-wallet/wallet.json"
password = input("Enter your wallet password: ")

try:
    with open(wallet_path, "r") as file:
        wallet_data = json.load(file)
    encrypted_key = wallet_data["encrypted_key"]
    pem = decrypt_data(encrypted_key, password)
    private_key = SigningKey.from_pem(pem)
    print("Wallet loaded successfully!")
    print(f"Private Key: {private_key.to_string().hex()}")
except Exception as e:
    print(f"Error: {e}")
