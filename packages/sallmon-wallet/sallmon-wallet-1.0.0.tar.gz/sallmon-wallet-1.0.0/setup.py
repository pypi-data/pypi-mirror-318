from setuptools import setup, find_packages

setup(
    name="sallmon-wallet",
    version="1.0.0",
    description="Sallmon Wallet CLI for managing cryptocurrency wallets.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # This should find 'sallmon_wallet'
    install_requires=[
        "click",
        "cryptography",
        "ecdsa",
        "base58",
    ],
    entry_points={
        "console_scripts": [
            "sallmon = sallmon_wallet.cli:cli",  # Path to wallet CLI entry
        ],
    },
)
