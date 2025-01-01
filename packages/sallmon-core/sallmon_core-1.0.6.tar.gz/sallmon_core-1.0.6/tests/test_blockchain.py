from blockchain import Blockchain

def test_blockchain():
    print("🚀 Starting Blockchain Test...")

    # Initialize Blockchain
    blockchain = Blockchain()

    # Test Genesis Block
    print("🔗 Testing Genesis Block...")
    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].index == 0
    print("✅ Genesis block created successfully.")

    # Add Transactions
    print("💸 Adding Transactions...")
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.add_transaction("Bob", "Charlie", 5)
    assert len(blockchain.pending_transactions) == 2
    print("✅ Transactions added successfully.")

    # Mine a Block
    print("⛏️ Mining a Block...")
    miner_address = "Miner1"
    mined_block = blockchain.mine_block(miner_address)
    assert mined_block.index == 1
    assert len(blockchain.pending_transactions) == 0
    print("✅ Block mined successfully.")

    # Check Balances
    print("💰 Checking Balances...")
    alice_balance = blockchain.get_balance("Alice")
    bob_balance = blockchain.get_balance("Bob")
    charlie_balance = blockchain.get_balance("Charlie")
    miner_balance = blockchain.get_balance(miner_address)

    assert alice_balance == -10
    assert bob_balance == 5  # Corrected expected value
    assert charlie_balance == 5
    assert miner_balance == 50
    print("✅ Balances validated successfully.")
