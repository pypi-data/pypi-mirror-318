import json
import hashlib
import logging
import time
from datetime import datetime
from sallmon.sallmon_core.services.mempool import get_mempool, reset_mempool
from sallmon.sallmon_core.services.block_db import add_block, get_latest_block
from sallmon.sallmon_core.services.utxos import validate_utxos, add_utxo

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] 🛠 %(message)s")

# Constants
BLOCK_REWARD = 50  # Reward for mining a block
MSRP_FACTOR = 0.8  # MSRP = 80% of FMV
INITIAL_DIFFICULTY = 4
TARGET_BLOCK_TIME = 314  # 3 minutes and 14 seconds
DIFFICULTY_ADJUSTMENT_FACTOR = 0.1


def calculate_fmv(resource_cost, total_blocks):
    """Calculate the Fair Market Value of the coin."""
    logging.debug(f"Calculating FMV with resource_cost={resource_cost}, total_blocks={total_blocks}")
    return resource_cost / total_blocks if total_blocks > 0 else resource_cost


def calculate_msrp(fmv):
    """Calculate the Manufacturer's Suggested Retail Price of the coin."""
    logging.debug(f"Calculating MSRP with FMV={fmv}")
    return fmv * MSRP_FACTOR


def track_contributions(mempool):
    """Track resource contributions from users."""
    contributions = {tx["address"]: tx["contribution"] for tx in mempool}
    total_contribution = sum(contributions.values())
    logging.debug(f"Contributions tracked: {contributions}, Total contribution: {total_contribution}")
    return contributions, total_contribution


def create_coinbase_transaction(miner_address):
    """Create a coinbase transaction."""
    logging.debug(f"Creating coinbase transaction for miner_address={miner_address}")
    return {
        "type": "coinbase",
        "txid": hashlib.sha256(f"coinbase-{miner_address}-{time.time()}".encode()).hexdigest(),
        "index": 0,
        "address": miner_address,
        "amount": BLOCK_REWARD,
        "timestamp": datetime.utcnow().isoformat(),
    }


def proof_of_work(block_data, difficulty):
    """Perform Proof-of-Work to mine a valid block."""
    nonce = 0
    block_data_str = json.dumps(block_data, sort_keys=True)
    logging.info(f"Starting Proof-of-Work with difficulty={difficulty}")
    while True:
        hash_attempt = hashlib.sha256(f"{block_data_str}-{nonce}".encode()).hexdigest()
        if hash_attempt.startswith("0" * difficulty):
            logging.info(f"Proof-of-Work successful! nonce={nonce}, hash={hash_attempt}")
            return nonce, hash_attempt
        if nonce % 100000 == 0:
            logging.debug(f"Proof-of-Work progress: nonce={nonce}, last_hash={hash_attempt}")
        nonce += 1


from datetime import timezone

def adjust_difficulty(previous_block, start_time):
    """Adjust the mining difficulty dynamically."""
    if not previous_block:
        logging.info("No previous block found. Using initial difficulty.")
        return INITIAL_DIFFICULTY

    # Handle ISO format with 'Z' for UTC
    previous_timestamp_str = previous_block["timestamp"].replace("Z", "+00:00")
    previous_timestamp = datetime.fromisoformat(previous_timestamp_str)

    # Ensure both datetimes are timezone-aware
    if previous_timestamp.tzinfo is None:
        previous_timestamp = previous_timestamp.replace(tzinfo=timezone.utc)
    if start_time.tzinfo is None:
        start_time = start_time.replace(tzinfo=timezone.utc)

    # Calculate time difference
    time_taken = (start_time - previous_timestamp).total_seconds()
    logging.info(f"Time taken since last block: {time_taken} seconds")

    if time_taken > TARGET_BLOCK_TIME:
        logging.info("Adjusting difficulty: making it easier")
        return max(1, int(previous_block["difficulty"] - DIFFICULTY_ADJUSTMENT_FACTOR))
    else:
        logging.info("Adjusting difficulty: making it harder")
        return int(previous_block["difficulty"] + DIFFICULTY_ADJUSTMENT_FACTOR)


def mine_block(miner_address, resource_cost):
    """Main mining function."""
    try:
        start_time = datetime.utcnow()

        # Load mempool and validate transactions
        mempool = get_mempool()
        valid_transactions = validate_utxos(mempool)

        # Calculate contributions
        contributions, total_contribution = track_contributions(valid_transactions)

        # Add coinbase transaction
        coinbase_tx = create_coinbase_transaction(miner_address)
        valid_transactions.insert(0, coinbase_tx)

        # Load previous block data
        previous_block = get_latest_block()
        previous_hash = previous_block["block_hash"] if previous_block else "0" * 64
        previous_height = previous_block["height"] if previous_block else 0

        # Adjust difficulty
        difficulty = adjust_difficulty(previous_block, start_time)

        # Prepare block data
        block_data = {
            "previous_hash": previous_hash,
            "timestamp": start_time.isoformat(),
            "transactions": valid_transactions,
            "difficulty": difficulty,
            "height": previous_height + 1,  # Increment the block height
        }

        # Perform Proof-of-Work
        logging.info(f"⛏️ Mining block with difficulty {difficulty}...")
        nonce, block_hash = proof_of_work(block_data, difficulty)

        # Finalize the block
        block_data.update({"nonce": nonce, "block_hash": block_hash})
        add_block(block_data)

        # Update UTXO for coinbase transaction
        add_utxo(coinbase_tx["txid"], coinbase_tx["index"], coinbase_tx["address"], coinbase_tx["amount"])

        # Reset mempool
        reset_mempool()

        # Coin Valuation
        total_blocks = block_data["height"]
        fmv = calculate_fmv(resource_cost, total_blocks)
        msrp = calculate_msrp(fmv)

        end_time = datetime.utcnow()
        logging.info(f"✅ Block mined successfully! Hash: {block_hash}")
        logging.info(f"⏱️ Time taken: {(end_time - start_time).total_seconds()} seconds")
        logging.info(f"💰 FMV: ${fmv:.2f}, MSRP: ${msrp:.2f}")

        return {"block": block_data, "fmv": fmv, "msrp": msrp, "rewards": contributions}

    except Exception as e:
        logging.error(f"🚨 Error during mining: {e}")
        return None
