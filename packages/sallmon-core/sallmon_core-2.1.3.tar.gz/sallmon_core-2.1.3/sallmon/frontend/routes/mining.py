from flask import Blueprint, request, jsonify, render_template
import hashlib
import json
import logging
from datetime import datetime
import requests  # To send the mined block to the WebSocket API

mining_blueprint = Blueprint("mining", __name__)

# Constants
BLOCK_REWARD = 50
INITIAL_DIFFICULTY = 4
WS_ENDPOINT = "http://localhost:1337/send-to-ws"  # Update this to match your WebSocket endpoint

# Mock blockchain data
blockchain = []

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Helper Functions
def proof_of_work(block_data, difficulty):
    """Perform proof-of-work."""
    nonce = 0
    block_data_str = json.dumps(block_data, sort_keys=True)
    while True:
        hash_attempt = hashlib.sha256(f"{block_data_str}-{nonce}".encode()).hexdigest()
        if hash_attempt.startswith("0" * difficulty):
            return nonce, hash_attempt
        nonce += 1

def broadcast_block(block_data):
    """Send the mined block to the WebSocket API."""
    try:
        response = requests.post(WS_ENDPOINT, json={"type": "blocks", "block_data": block_data})
        if response.status_code == 200:
            logging.info("✅ Block broadcasted successfully.")
        else:
            logging.warning(f"🚨 Failed to broadcast block: {response.json()}")
    except Exception as e:
        logging.error(f"🚨 Error broadcasting block: {e}")

@mining_blueprint.route("/mine-block", methods=["POST"])
def mine_block():
    """Mine a block and return its details."""
    try:
        data = request.json
        miner_address = data.get("miner_address")

        if not miner_address:
            return jsonify({"error": "Miner address is required."}), 400

        # Mining logic
        start_time = datetime.utcnow()
        previous_hash = blockchain[-1]["block_hash"] if blockchain else "0" * 64
        difficulty = INITIAL_DIFFICULTY

        block_data = {
            "previous_hash": previous_hash,
            "timestamp": start_time.isoformat(),
            "miner_address": miner_address,
            "transactions": [],
            "difficulty": difficulty,
            "reward": BLOCK_REWARD,
        }

        nonce, block_hash = proof_of_work(block_data, difficulty)

        block_data.update({
            "nonce": nonce,
            "block_hash": block_hash,
        })

        # Append block to blockchain
        blockchain.append(block_data)
        logging.info(f"Block mined: {block_hash}")

        # Broadcast the block to WebSocket API
        broadcast_block(block_data)

        return jsonify({"status": "success", "block": block_data}), 200

    except Exception as e:
        logging.error(f"Error during mining: {e}")
        return jsonify({"error": str(e)}), 500

@mining_blueprint.route("/blockchain", methods=["GET"])
def get_blockchain():
    """Retrieve the current blockchain."""
    try:
        return jsonify({"status": "success", "blockchain": blockchain}), 200
    except Exception as e:
        logging.error(f"Error fetching blockchain: {e}")
        return jsonify({"error": str(e)}), 500

@mining_blueprint.route("/mine", methods=["GET"])
def mining_page():
    """Render the mining page."""
    return render_template("mine.html")
