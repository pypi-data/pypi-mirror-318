import click
import json
from pathlib import Path

# Wallet storage file
WALLETS_FILE = Path("~/.sallmon/wallets.json").expanduser()


def load_wallets():
    """Load wallets from the JSON file."""
    if WALLETS_FILE.exists():
        with open(WALLETS_FILE, "r") as file:
            return json.load(file)
    return {}


def save_wallets(wallets):
    """Save wallets to the JSON file."""
    with open(WALLETS_FILE, "w") as file:
        json.dump(wallets, file, indent=4)


@click.group()
def wallet():
    """Manage wallets."""
    pass


@wallet.command()
@click.argument("passphrase")
def create(passphrase):
    """Create a new wallet."""
    wallets = load_wallets()
    wallet_id = f"wallet-{len(wallets) + 1}"
    wallets[wallet_id] = {
        "address": f"address-{wallet_id}",
        "balance": 0.0,
        "passphrase": passphrase,
    }
    save_wallets(wallets)
    click.echo(f"Wallet created: {wallet_id}")


@wallet.command()
def list():
    """List all wallets."""
    wallets = load_wallets()
    if wallets:
        for wallet_id, wallet in wallets.items():
            click.echo(f"{wallet_id}: {wallet['address']}")
    else:
        click.echo("No wallets found.")


@wallet.command()
@click.argument("wallet_id")
def get(wallet_id):
    """Retrieve a wallet by ID."""
    wallets = load_wallets()
    wallet = wallets.get(wallet_id)
    if wallet:
        click.echo(f"Wallet: {wallet}")
    else:
        click.echo(f"Wallet not found: {wallet_id}")


@wallet.command()
@click.argument("wallet_id")
def delete(wallet_id):y
    """Delete a wallet by ID."""
    wallets = load_wallets()
    if wallet_id in wallets:
        del wallets[wallet_id]
        save_wallets(wallets)
        click.echo(f"Wallet {wallet_id} deleted")
    else:
        click.echo(f"Wallet not found: {wallet_id}")


