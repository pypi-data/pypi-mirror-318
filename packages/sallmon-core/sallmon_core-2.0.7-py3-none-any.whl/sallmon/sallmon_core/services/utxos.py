import sqlite3
import logging
from typing import List, Dict

DB_FILE = "~/.sallmon/blockchain.db"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] 🛠 %(message)s")

def get_connection():
    """Get a database connection."""
    return sqlite3.connect(DB_FILE)

import sqlite3
from sallmon_core.services.block_db import DB_FILE

def add_utxo(txid: str, index: int, address: str, amount: float):
    """Add a UTXO to the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO utxos (txid, "index", address, amount)
            VALUES (?, ?, ?, ?)
        """, (txid, index, address, amount))
        conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()


def get_utxos(address: str = None) -> List[Dict]:
    """Retrieve UTXOs. Optionally filter by address."""
    try:
        conn = get_connection()
        c = conn.cursor()
        if address:
            c.execute("SELECT * FROM utxos WHERE address = ? AND spent = 0", (address,))
        else:
            c.execute("SELECT * FROM utxos WHERE spent = 0")
        rows = c.fetchall()
        return [{"id": row[0], "txid": row[1], "index": row[2], "address": row[3], "amount": row[4]} for row in rows]
    except sqlite3.Error as e:
        logging.error(f"🚨 Database error while retrieving UTXOs: {e}")
        return []
    finally:
        conn.close()


def spend_utxo(txid: str, index: int, address: str, amount: float):
    """Spend a UTXO by marking it as used or removing it."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM utxos
        WHERE txid = ? AND "index" = ? AND address = ? AND amount = ?
    """, (txid, index, address, amount))
    conn.commit()
    affected_rows = cursor.rowcount
    conn.close()
    return affected_rows > 0  # True if UTXO was spent


# sallmon_core/services/utxos.py

def validate_utxos(transactions):
    """
    Validate transactions against available UTXOs.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        valid_transactions = []

        for tx in transactions:
            txid = tx.get("txid")
            tx_index = tx.get("index")
            cursor.execute("""
                SELECT * FROM utxos WHERE txid = ? AND "index" = ?
            """, (txid, tx_index))
            utxo = cursor.fetchone()

            if utxo:
                # Transaction is valid
                valid_transactions.append(tx)

        return valid_transactions

    except sqlite3.Error as e:
        logging.error(f"🚨 Database error during UTXO validation: {e}")
        return []
    except Exception as e:
        logging.error(f"🚨 Unexpected error during UTXO validation: {e}")
        return []
    finally:
        conn.close()

# sallmon_core/services/utxos.py

def validate_transaction(transaction):
    """
    Validate a transaction.
    Ensure the transaction structure and UTXO availability.
    """
    required_fields = ["txid", "index", "address", "amount"]
    for field in required_fields:
        if field not in transaction:
            return False, f"Missing field: {field}"
    
    # Check for valid UTXO (you can expand this with actual UTXO checks)
    if transaction["amount"] <= 0:
        return False, "Transaction amount must be greater than zero."

    # Add additional validations as needed
    return True, "Transaction is valid."
