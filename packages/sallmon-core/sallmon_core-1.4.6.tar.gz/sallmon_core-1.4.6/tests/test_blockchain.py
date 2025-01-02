import time
from blockchain.blockchain import Blockchain

def test_genesis_block():
    """Test if the genesis block is created correctly."""
    blockchain = Blockchain()
    genesis_block = blockchain.chain[0]
    
    assert genesis_block.index == 0
    assert genesis_block.previous_hash == "0"
    assert genesis_block.data == "Genesis Block"

def test_mine_block():
    """Test mining a block."""
    blockchain = Blockchain()
    blockchain.mine_block("test_data")
    
    assert len(blockchain.chain) == 2
    mined_block = blockchain.chain[1]
    assert mined_block.data == "test_data"

def test_chain_validation():
    """Test blockchain validation."""
    blockchain = Blockchain()
    blockchain.mine_block("test_data")
    
    assert blockchain.is_chain_valid()

    # Tamper with the chain
    blockchain.chain[1].data = "tampered_data"
    assert not blockchain.is_chain_valid()
