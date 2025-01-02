import time
import logging
from block import Block

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Blockchain")

class Blockchain:
    difficulty = 2

    def __init__(self):
        logger.info("Initializing Blockchain...")
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()
        logger.info("Blockchain initialized successfully.")


    def create_genesis_block(self):
        logger.info("Creating Genesis Block...")
        genesis_data = json.dumps({
            "message": "Genesis Block - Static",
            "note": "This is the genesis block for the blockchain."
        })  # Ensure data is valid JSON
        genesis_block = Block(0, "0", time.time(), genesis_data)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
        logger.debug(f"Genesis Block created: {genesis_block}")

    def add_transaction(self, sender, recipient, amount):
        logger.info(f"Adding transaction from {sender} to {recipient} for amount {amount}...")
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
        })
        logger.debug(f"Transaction added. Pending Transactions: {self.pending_transactions}")

    def mine_block(self, miner_address):
        if not self.pending_transactions:
            logger.warning("No pending transactions to mine.")
            return None

        logger.info(f"Mining a new block... Rewarding miner: {miner_address}")
        reward_transaction = {"sender": "System", "recipient": miner_address, "amount": 50}
        transactions_to_mine = self.pending_transactions + [reward_transaction]

        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            previous_hash=last_block.hash,
            timestamp=time.time(),
            transactions=transactions_to_mine,
        )

        logger.info(f"New block created with index {new_block.index}. Starting proof of work...")
        start_time = time.time()

        while not new_block.hash.startswith("0" * Blockchain.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()

        end_time = time.time()
        logger.info(f"Block mined successfully. Time taken: {end_time - start_time:.2f} seconds")
        logger.debug(f"Mined Block: {new_block}")

        # Save block to chain
        self.chain.append(new_block)

        # Persist block in database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO blocks (block_index, previous_hash, timestamp, data, hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (new_block.index, new_block.previous_hash, new_block.timestamp, 
                json.dumps(new_block.transactions), new_block.hash))
        conn.commit()

        # Clear mined transactions
        self.pending_transactions = []

        conn.close()
        logger.info("Pending transactions cleared.")

        return new_block

    def get_balance(self, address):
        """
        Calculate the balance for a specific address.
        """
        logger.info(f"Calculating balance for address: {address}")
        balance = 0

        for block in self.chain:
            for transaction in block.transactions:
                if transaction["recipient"] == address:
                    balance += transaction["amount"]
                if transaction["sender"] == address:
                    balance -= transaction["amount"]

        logger.debug(f"Balance for {address}: {balance}")
        return balance

    def __str__(self):
        chain_data = [block.__dict__ for block in self.chain]
        return f"Blockchain:\n{chain_data}"
