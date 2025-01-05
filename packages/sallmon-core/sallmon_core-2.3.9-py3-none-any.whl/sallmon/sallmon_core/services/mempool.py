# sallmon_core/services/mempool.py
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] 🛠 %(message)s")

# Thread-safe mempool
class Mempool:
    def __init__(self):
        self.lock = threading.Lock()
        self.transactions = {}

    def add_transaction(self, transaction_id, transaction):
        """Add a transaction to the mempool."""
        with self.lock:
            if transaction_id in self.transactions:
                logging.warning(f"🚨 Duplicate transaction detected: {transaction_id}")
                return False  # Duplicate transaction
            self.transactions[transaction_id] = transaction
            logging.info(f"✅ Transaction added to mempool: {transaction_id}")
            return True

    def get_transactions(self):
        """Retrieve all transactions from the mempool."""
        with self.lock:
            transactions = list(self.transactions.values())
            logging.info(f"📜 Retrieved {len(transactions)} transactions from mempool.")
            return transactions

    def clear(self):
        """Clear all transactions in the mempool."""
        with self.lock:
            count = len(self.transactions)
            self.transactions.clear()
            logging.info(f"🧹 Cleared {count} transactions from mempool.")
            return True

    def remove_transaction(self, transaction_id):
        """Remove a specific transaction from the mempool."""
        with self.lock:
            if transaction_id in self.transactions:
                del self.transactions[transaction_id]
                logging.info(f"❌ Removed transaction from mempool: {transaction_id}")
                return True
            logging.warning(f"⚠️ Transaction not found in mempool: {transaction_id}")
            return False


# Global mempool instance
mempool = Mempool()

# Public API
def add_to_mempool(transaction_id, transaction):
    """Add a transaction to the mempool."""
    return mempool.add_transaction(transaction_id, transaction)

def get_mempool():
    """Retrieve all transactions from the mempool."""
    return mempool.get_transactions()

def reset_mempool():
    """Clear the mempool."""
    return mempool.clear()

def remove_from_mempool(transaction_id):
    """Remove a specific transaction from the mempool."""
    return mempool.remove_transaction(transaction_id)
