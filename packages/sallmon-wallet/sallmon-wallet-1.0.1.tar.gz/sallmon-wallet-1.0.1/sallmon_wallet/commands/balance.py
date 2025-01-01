import click
from sallmon_wallet.utils import load_wallet, generate_address
from sallmon_wallet.blockchain_utils import calculate_balance

@click.command()
def balance():
    """Show wallet balance."""
    password = click.prompt("Enter your wallet password", hide_input=True)
    private_key = load_wallet(password)
    if private_key:
        address = generate_address(private_key.get_verifying_key())
        balance = calculate_balance(address)
        click.echo(f"Wallet Balance: {balance}")
