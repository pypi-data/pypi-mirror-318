import sqlite3
import json
import os
from datetime import datetime
import hashlib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] 🛠 %(message)s")

# Database file path
DB_FILE = os.path.expanduser("~/.sallmon/blockchain.db")


def init_db():
    """Initialize the database and create tables if they don't exist."""
    logging.info("🔧 Initializing blockchain database...")
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        # Create the blocks table
        c.execute("""
            CREATE TABLE IF NOT EXISTS blocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                block_hash TEXT UNIQUE,
                previous_hash TEXT,
                timestamp TEXT,
                coinbase TEXT,
                miner_address TEXT,
                reward REAL,
                transaction_count INTEGER,
                difficulty INTEGER,
                nonce INTEGER
            )
        """)
        logging.info("📦 Blocks table ready.")

        # Create the transactions table
        c.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id TEXT PRIMARY KEY,
                block_id INTEGER,
                transaction_type TEXT,
                amount REAL,
                sender TEXT,
                recipient TEXT,
                timestamp TEXT,
                spent BOOLEAN DEFAULT 0,
                FOREIGN KEY(block_id) REFERENCES blocks(id)
            )
        """)
        logging.info("🔗 Transactions table ready.")

        # Create the UTXO table
        c.execute("""
            CREATE TABLE IF NOT EXISTS utxos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                txid TEXT,
                "index" INTEGER,
                address TEXT,
                amount REAL,
                FOREIGN KEY(txid) REFERENCES transactions(id)
            )
        """)
        logging.info("💰 UTXO table ready.")

        # Check if the genesis block exists
        c.execute("SELECT COUNT(*) FROM blocks")
        if c.fetchone()[0] == 0:
            logging.info("🌟 No genesis block found. Creating genesis block...")
            create_genesis_block(c)
        else:
            logging.info("✅ Genesis block already exists.")

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"🚨 Database error during initialization: {e}")
    except Exception as e:
        logging.error(f"🚨 Unexpected error during initialization: {e}")
    finally:
        conn.close()
        logging.info("🛠 Blockchain database initialization complete.")


def create_genesis_block(cursor):
    """Create the genesis block."""
    try:
        # Set the timestamp to today at noon
        today_noon = datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0)

        # Define the difficulty for the genesis block
        genesis_difficulty = 4  # Initial difficulty

        # Genesis coinbase transaction
        genesis_coinbase = {
            "type": "coinbase",
            "amount": 10000,
            "sender": "system",
            "recipient": "miner-genesis-wallet",
            "timestamp": today_noon.isoformat()
        }

        # Prepare block data
        block_data = {
            "previous_hash": "0" * 64,  # No previous block
            "timestamp": today_noon.isoformat(),
            "coinbase": genesis_coinbase,
            "miner_address": "miner-genesis-wallet",
            "reward": 10000,
            "transaction_count": 1,
            "difficulty": genesis_difficulty,
        }

        # Perform proof-of-work to find a valid nonce for genesis
        nonce = 0
        block_data_str = json.dumps(block_data, sort_keys=True)
        while True:
            block_hash = hashlib.sha256(f"{block_data_str}-{nonce}".encode()).hexdigest()
            if block_hash.startswith("0" * genesis_difficulty):
                break
            nonce += 1

        # Finalize block data
        block_data.update({"nonce": nonce, "block_hash": block_hash})

        # Insert the genesis block into the database
        cursor.execute("""
            INSERT INTO blocks (block_hash, previous_hash, timestamp, coinbase, miner_address, reward,
                                transaction_count, difficulty, nonce)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (block_hash, block_data["previous_hash"], block_data["timestamp"], json.dumps(genesis_coinbase),
              block_data["miner_address"], block_data["reward"], block_data["transaction_count"],
              block_data["difficulty"], block_data["nonce"]))

        # Insert the coinbase transaction
        transaction_id = hashlib.sha256(json.dumps(genesis_coinbase, sort_keys=True).encode()).hexdigest()
        cursor.execute("""
            INSERT INTO transactions (id, block_id, transaction_type, amount, sender, recipient, timestamp, spent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            transaction_id,
            1,  # Genesis block ID
            genesis_coinbase["type"],
            genesis_coinbase["amount"],
            genesis_coinbase["sender"],
            genesis_coinbase["recipient"],
            genesis_coinbase["timestamp"],
            0  # Coinbase transactions are not spent
        ))

        # Insert the UTXO for the genesis transaction
        cursor.execute("""
            INSERT INTO utxos (txid, index, address, amount)
            VALUES (?, ?, ?, ?)
        """, (
            transaction_id,
            0,  # Single output for genesis
            genesis_coinbase["recipient"],
            genesis_coinbase["amount"]
        ))

        logging.info(f"🌟 Genesis block created with hash: {block_hash}, difficulty: {genesis_difficulty}, nonce: {nonce}")
    except sqlite3.Error as e:
        logging.error(f"🚨 Database error during genesis block creation: {e}")
    except Exception as e:
        logging.error(f"🚨 Unexpected error during genesis block creation: {e}")



def add_block(block_data):
    """Add a mined block to the blockchain database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Insert the block into the blocks table
        cursor.execute("""
            INSERT INTO blocks (block_hash, previous_hash, timestamp, coinbase, miner_address, reward,
                                transaction_count, difficulty, nonce)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            block_data["block_hash"],
            block_data["previous_hash"],
            block_data["timestamp"],
            json.dumps(block_data["coinbase"]),
            block_data["miner_address"],
            block_data["reward"],
            block_data["transaction_count"],
            block_data["difficulty"],
            block_data["nonce"]
        ))

        # Get the block ID of the newly inserted block
        block_id = cursor.lastrowid

        # Insert transactions into the transactions table
        for tx in block_data["transactions"]:
            cursor.execute("""
                INSERT INTO transactions (id, block_id, transaction_type, amount, sender, recipient, timestamp, spent)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                tx["txid"],
                block_id,
                tx["type"],
                tx["amount"],
                tx.get("sender", None),
                tx["recipient"],
                tx["timestamp"],
                0  # Mark all transactions as unspent initially
            ))

        conn.commit()
        logging.info(f"✅ Block added successfully with hash: {block_data['block_hash']}")
    except sqlite3.Error as e:
        logging.error(f"🚨 Database error while adding block: {e}")
    except Exception as e:
        logging.error(f"🚨 Unexpected error while adding block: {e}")
    finally:
        conn.close()


def get_latest_block():
    """Retrieve the latest block from the blockchain database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Query to get the most recent block
        cursor.execute("""
            SELECT * FROM blocks
            ORDER BY id DESC
            LIMIT 1
        """)
        row = cursor.fetchone()

        if row:
            block = {
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
            }
            return block
        return None  # No blocks in the database

    except sqlite3.Error as e:
        logging.error(f"🚨 Database error while retrieving the latest block: {e}")
        return None
    except Exception as e:
        logging.error(f"🚨 Unexpected error while retrieving the latest block: {e}")
        return None
    finally:
        conn.close()


# Initialize the database at startup
if __name__ == "__main__":
    init_db()
    logging.info("✅ Blockchain database setup is complete!")
