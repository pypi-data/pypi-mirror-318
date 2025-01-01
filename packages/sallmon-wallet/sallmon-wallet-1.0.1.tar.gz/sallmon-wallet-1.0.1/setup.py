from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sallmon-wallet",
    version="1.0.1",  # Incremented version number
    description="Sallmon Wallet CLI for cryptocurrency wallet management and blockchain integration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andrew Polykandriotis",
    author_email="andrew@minakilabs.com",
    url="https://github.com/minakilabs/sallmon-sdk",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "cryptography",
        "requests",
        "ecdsa",
        "base58",
    ],
    entry_points={
        "console_scripts": [
            "sallmon-wallet=sallmon_wallet.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
