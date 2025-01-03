import click
import requests

BASE_URL = "http://127.0.0.1:1337"  # Ensure this points to the correct API base URL

@click.group()
def mine():
    """Mine blocks."""
    pass

@mine.command()
@click.argument("miner_address")
def start(miner_address):
    """Start mining a new block."""
    url = f"{BASE_URL}/mine-block"
    payload = {"miner_address": miner_address}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            block = response.json().get("block")
            click.echo(f"✅ Successfully mined a new block:\n{block}")
        else:
            error = response.json().get("detail", "Unknown error")
            click.echo(f"❌ Failed to mine block: {error}")
    except Exception as e:
        click.echo(f"❌ Error connecting to the mining endpoint: {str(e)}")
