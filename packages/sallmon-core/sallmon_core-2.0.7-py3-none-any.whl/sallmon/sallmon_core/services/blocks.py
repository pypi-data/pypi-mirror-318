import sqlite3
import json
import os
import logging
from sallmon_core.services.block_db import add_block, get_latest_block, DB_FILE

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] 🛠 %(message)s")

def validate_block(block_data):
    """Validate the structure and content of a block."""
    required_fields = ["block_hash", "previous_hash", "timestamp", "transactions", "difficulty", "nonce"]
    for field in required_fields:
        if field not in block_data:
            logging.error(f"🚨 Block validation failed: Missing field {field}")
            return False, f"Missing field {field}"

    # Additional validations (e.g., proof-of-work validation) can be added here
    if not block_data["block_hash"].startswith("0" * block_data["difficulty"]):
        logging.error("🚨 Block validation failed: Invalid proof of work")
        return False, "Invalid proof of work"

    return True, "Block is valid"

def get_all_blocks():
    """Retrieve all blocks from the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM blocks ORDER BY id ASC")
        rows = cursor.fetchall()

        blocks = []
        for row in rows:
            blocks.append({
                "id": row[0],
                "block_hash": row[1],
                "previous_hash": row[2],
                "timestamp": row[3],
                "coinbase": json.loads(row[4]),
                "miner_address": row[5],
                "reward": row[6],
                "transaction_count": row[7],
                "difficulty": row[8],
                "nonce": row[9],
            })
        return blocks
    except sqlite3.Error as e:
        logging.error(f"🚨 Database error while retrieving blocks: {e}")
        return []
    except Exception as e:
        logging.error(f"🚨 Unexpected error while retrieving blocks: {e}")
        return []
    finally:
        conn.close()
