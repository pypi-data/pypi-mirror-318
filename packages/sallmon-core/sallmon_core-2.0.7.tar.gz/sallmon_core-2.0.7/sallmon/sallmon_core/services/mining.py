import json
import hashlib
import time
from datetime import datetime, timedelta
from sallmon_core.services.mempool import get_mempool, reset_mempool
from sallmon_core.services.block_db import add_block, get_latest_block
from sallmon_core.services.utxos import validate_utxos, add_utxo
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] 🛠 %(message)s")

BLOCK_REWARD = 50  # Fixed coinbase reward
MINING_TARGET_TIME = 32  # Target mining time in seconds
INITIAL_DIFFICULTY = 4  # Initial difficulty
DIFFICULTY_ADJUSTMENT_FACTOR = 0.1  # How aggressively to adjust difficulty


def create_coinbase_transaction(miner_address):
    """Create a coinbase transaction to reward the miner."""
    return {
        "type": "coinbase",
        "txid": hashlib.sha256(f"coinbase-{miner_address}-{time.time()}".encode()).hexdigest(),
        "index": 0,
        "address": miner_address,
        "amount": BLOCK_REWARD,
        "timestamp": datetime.utcnow().isoformat(),
    }


def proof_of_work(block_data, difficulty):
    """Perform proof-of-work to find a valid nonce."""
    nonce = 0
    block_data_str = json.dumps(block_data, sort_keys=True)
    while True:
        hash_attempt = hashlib.sha256(f"{block_data_str}-{nonce}".encode()).hexdigest()
        if hash_attempt.startswith("0" * difficulty):
            return nonce, hash_attempt
        nonce += 1


def adjust_difficulty(previous_block, start_time):
    """Adjust the difficulty based on mining time."""
    if not previous_block:
        return INITIAL_DIFFICULTY

    previous_timestamp = datetime.fromisoformat(previous_block["timestamp"])
    time_taken = (start_time - previous_timestamp).total_seconds()

    if time_taken > MINING_TARGET_TIME:
        # Make mining easier
        new_difficulty = max(1, int(previous_block["difficulty"] - DIFFICULTY_ADJUSTMENT_FACTOR))
    else:
        # Make mining harder
        new_difficulty = int(previous_block["difficulty"] + DIFFICULTY_ADJUSTMENT_FACTOR)

    logging.info(f"⏳ Adjusted difficulty: {new_difficulty} (time taken: {time_taken:.2f}s)")
    return new_difficulty


def mine_block(miner_address):
    """Mine a new block."""
    try:
        start_time = datetime.utcnow()

        # Get transactions from mempool
        mempool = get_mempool()
        valid_transactions = validate_utxos(mempool)

        # Add the coinbase transaction
        coinbase_tx = create_coinbase_transaction(miner_address)
        valid_transactions.insert(0, coinbase_tx)

        # Get previous block
        previous_block = get_latest_block()
        previous_hash = previous_block["block_hash"] if previous_block else "0" * 64

        # Adjust difficulty
        difficulty = adjust_difficulty(previous_block, start_time)

        # Prepare block data
        block_data = {
            "previous_hash": previous_hash,
            "timestamp": start_time.isoformat(),
            "transactions": valid_transactions,
            "difficulty": difficulty,
        }

        # Perform proof-of-work
        logging.info(f"⛏️ Mining block with difficulty: {difficulty}")
        nonce, block_hash = proof_of_work(block_data, difficulty)

        # Finalize block
        block_data.update({"nonce": nonce, "block_hash": block_hash})
        add_block(block_data)

        # Add coinbase UTXO
        add_utxo(
            txid=coinbase_tx["txid"],
            index=coinbase_tx["index"],
            address=coinbase_tx["address"],
            amount=coinbase_tx["amount"]
        )

        # Reset the mempool
        reset_mempool()

        end_time = datetime.utcnow()
        logging.info(f"✅ Block mined successfully! Hash: {block_hash}")
        logging.info(f"⏱️ Time taken: {(end_time - start_time).total_seconds()} seconds")
        logging.info(f"📦 Block Data: {json.dumps(block_data, indent=4)}")
        return block_data

    except Exception as e:
        logging.error(f"🚨 Error while mining block: {e}")
        return None
