from blockchain.transaction_pool import TransactionPool

def test_add_transaction():
    """Test adding a transaction to the pool."""
    pool = TransactionPool()
    pool.add_transaction("Alice pays Bob 10 BTC")
    
    assert len(pool.transactions) == 1
    assert pool.transactions[0] == "Alice pays Bob 10 BTC"

def test_clear_transactions():
    """Test clearing the transaction pool."""
    pool = TransactionPool()
    pool.add_transaction("Alice pays Bob 10 BTC")
    pool.clear()
    
    assert len(pool.transactions) == 0
