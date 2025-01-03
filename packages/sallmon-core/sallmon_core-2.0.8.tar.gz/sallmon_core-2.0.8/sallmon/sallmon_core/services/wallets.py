import os
import json
import uuid
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

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

def create_wallet(passphrase):
    """Create a new wallet and store it."""
    wallets = load_wallets()

    # Generate RSA key pair
    key = RSA.generate(2048)
    private_key = key.export_key(passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")
    public_key = key.publickey().export_key()

    wallet_id = str(uuid.uuid4())
    wallets[wallet_id] = {
        "public_key": public_key.decode(),
        "encrypted_private_key": b64encode(private_key).decode(),  # Store encrypted private key
        "balance": 0.0,  # Initially zero balance
    }

    save_wallets(wallets)
    return {"wallet_id": wallet_id, "public_key": public_key.decode()}

def list_wallets():
    """List all wallet IDs."""
    wallets = load_wallets()
    return [{"wallet_id": wallet_id, "public_key": data["public_key"]} for wallet_id, data in wallets.items()]

def get_wallet(wallet_id):
    """Retrieve wallet details by ID."""
    wallets = load_wallets()
    return wallets.get(wallet_id, None)

def delete_wallet(wallet_id):
    """Delete a wallet by ID."""
    wallets = load_wallets()
    if wallet_id in wallets:
        del wallets[wallet_id]
        save_wallets(wallets)
        return True
    return False

def decrypt_private_key(wallet_id, passphrase):
    """Decrypt the private key for a wallet."""
    wallets = load_wallets()
    wallet = wallets.get(wallet_id)
    if not wallet:
        raise ValueError("Wallet not found.")

    encrypted_private_key = b64decode(wallet["encrypted_private_key"])
    key = RSA.import_key(encrypted_private_key, passphrase=passphrase)
    return key.export_key().decode()
