import time
from blockchain.block import Block

def test_block_creation():
    """Test if a block is created correctly."""
    timestamp = time.time()
    block = Block(1, "previous_hash", timestamp, "test_data", "hash_value", 0)
    
    assert block.index == 1
    assert block.previous_hash == "previous_hash"
    assert block.timestamp == timestamp
    assert block.data == "test_data"
    assert block.hash == "hash_value"
    assert block.nonce == 0

def test_block_hash():
    """Test hash calculation for a block."""
    index = 1
    previous_hash = "prev_hash"
    timestamp = 1234567890
    data = "test_data"
    nonce = 0

    calculated_hash = Block.calculate_hash(index, previous_hash, timestamp, data, nonce)
    assert len(calculated_hash) == 64  # SHA-256 produces a 64-character hash
