import click
import requests
import json
from datetime import datetime
from commands.wallet import wallet
from commands.mine import mine

BASE_URL = "http://127.0.0.1:1337"

# Hardcoded peers
HARDCODED_PEERS = ["96.70.45.233:1337", "172.234.207.57:1337"]

@click.group()
def cli():
    """Sallmon CLI - Manage peers and broadcast messages."""
    pass

@click.command()
@click.argument("peer_ip")
def register_peer(peer_ip):
    """Register a new peer."""
    url = f"{BASE_URL}/register-peer"
    payload = {"ip": peer_ip}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        click.echo(f"✅ Peer registered: {peer_ip}")
    else:
        click.echo(f"❌ Failed to register peer: {response.json()}")


import socket

@click.command()
@click.option("--self-ip", required=False, help="The public IP and port of this node (e.g., 172.234.203.211:1337). If not provided, the public IP will be auto-detected.")
def load_hardcoded_peers(self_ip):
    """Load hardcoded peers and broadcast join-network."""
    # Detect public IP if not provided
    if not self_ip:
        try:
            # Resolve public IP by pinging an external service (or use an API like `httpbin`)
            public_ip = socket.gethostbyname(socket.gethostname())
            self_ip = f"{public_ip}:1337"  # Append default port
            click.echo(f"🌐 Auto-detected public IP: {self_ip}")
        except Exception as e:
            click.echo(f"❌ Failed to auto-detect public IP: {str(e)}")
            return

    all_registered = True

    # Register each hardcoded peer
    for peer in HARDCODED_PEERS:
        url = f"{BASE_URL}/register-peer"
        payload = {"ip": peer}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            click.echo(f"✅ Peer registered: {peer}")
        else:
            click.echo(f"❌ Failed to register peer: {peer} - {response.json()}")
            all_registered = False

    # Only broadcast join-network if all peers were successfully registered
    if all_registered:
        click.echo("🌐 Broadcasting join-network message to peers...")
        url = f"{BASE_URL}/broadcast"
        payload = {
            "type": "join-network",
            "id": f"join-{datetime.utcnow().isoformat()}",
            "timestamp": datetime.utcnow().isoformat(),
            "content": {"ip": self_ip},
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            click.echo(f"✅ Join-network message broadcasted: {response.json()}")
        else:
            click.echo(f"❌ Failed to broadcast join-network message: {response.json()}")
    else:
        click.echo("⚠️ Not all peers registered. Join-network broadcast skipped.")


@click.command()
@click.option("--type", default="blocks", help="Type of message (blocks, mempool, etc.).")
@click.option("--id", default=None, help="Unique message ID (default: auto-generated).")
@click.option("--content", default=None, help="Message content (JSON format).")
def broadcast(type, id, content):
    """Broadcast a message to peers."""
    url = f"{BASE_URL}/broadcast"
    if not id:
        id = f"msg-{datetime.utcnow().isoformat()}"
    if not content:
        content = '{"data": "Hello, World!"}'
    payload = {
        "type": type,
        "id": id,
        "timestamp": datetime.utcnow().isoformat(),
        "content": json.loads(content),
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        click.echo(f"✅ Message broadcasted: {response.json()}")
    else:
        click.echo(f"❌ Failed to broadcast message: {response.json()}")

@click.command()
def list_peers():
    """List all registered peers."""
    url = f"{BASE_URL}/get-peers"
    response = requests.get(url)
    if response.status_code == 200:
        peers = response.json().get("peers", [])
        click.echo(f"🌐 Registered Peers: {peers}")
    else:
        click.echo(f"❌ Failed to retrieve peers: {response.json()}")

cli.add_command(register_peer)
cli.add_command(load_hardcoded_peers)
cli.add_command(broadcast)
cli.add_command(list_peers)
cli.add_command(wallet)

cli.add_command(mine)

if __name__ == "__main__":
    cli()
