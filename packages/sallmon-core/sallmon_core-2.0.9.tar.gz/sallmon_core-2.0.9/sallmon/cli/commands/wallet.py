import click
from sallmon.sallmon_core.services.wallets import create_wallet, list_wallets, get_wallet, delete_wallet

@click.group()
def wallet():
    """Manage wallets."""
    pass

@wallet.command()
@click.argument("passphrase")
def create(passphrase):
    """Create a new wallet."""
    try:
        wallet = create_wallet(passphrase)
        click.echo(f"Wallet created: {wallet}")
    except Exception as e:
        click.echo(f"Error: {e}")

@wallet.command()
def list():
    """List all wallets."""
    try:
        wallets = list_wallets()
        click.echo(f"Wallets: {wallets}")
    except Exception as e:
        click.echo(f"Error: {e}")

@wallet.command()
@click.argument("wallet_id")
def get(wallet_id):
    """Retrieve a wallet by ID."""
    try:
        wallet = get_wallet(wallet_id)
        if wallet:
            click.echo(f"Wallet: {wallet}")
        else:
            click.echo(f"Wallet not found: {wallet_id}")
    except Exception as e:
        click.echo(f"Error: {e}")

@wallet.command()
@click.argument("wallet_id")
def delete(wallet_id):
    """Delete a wallet by ID."""
    try:
        if delete_wallet(wallet_id):
            click.echo(f"Wallet {wallet_id} deleted")
        else:
            click.echo(f"Wallet not found: {wallet_id}")
    except Exception as e:
        click.echo(f"Error: {e}")

@wallet.command()
@click.argument("address")
def balance(address):
    """Retrieve the balance for a wallet or account."""
    import requests

    BASE_URL = "http://127.0.0.1:1337"
    url = f"{BASE_URL}/wallet/balance"
    payload = {"address": address}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            balance = response.json().get("balance", 0.0)
            click.echo(f"Balance for {address}: {balance} coins")
        else:
            click.echo(f"Error: {response.json().get('detail', 'Failed to retrieve balance')}")
    except Exception as e:
        click.echo(f"Error: {e}")
