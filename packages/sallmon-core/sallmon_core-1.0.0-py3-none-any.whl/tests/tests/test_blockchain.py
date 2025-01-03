import pytest
from sallmon.core.blockchain import Blockchain

@pytest.fixture
def blockchain():
    """Fixture to provide a fresh blockchain instance."""
    return Blockchain()

def test_add_valid_block(blockchain):
    """Test adding a valid block to the blockchain."""
    block = {
        "index": 1,
        "previous_hash": Blockchain.calculate_hash({"dummy": "block"}),
        "timestamp": 123456789,
        "data": [{"sender": "Alice", "recipient": "Bob", "amount": 10}],
        "nonce": 123,
        "hash": "dummyhash"
    }
    blockchain.add_block(block)
    assert len(blockchain.chain) == 2  # Includes the genesis block
    assert blockchain.chain[-1] == block

def test_add_invalid_block(blockchain):
    """Test that an invalid block is not added."""
    block = {
        "index": 1,
        "previous_hash": "wrong_hash",
        "timestamp": 123456789,
        "data": [{"sender": "Alice", "recipient": "Bob", "amount": 10}],
        "nonce": 123,
        "hash": "dummyhash"
    }
    with pytest.raises(ValueError):
        blockchain.add_block(block)

def test_chain_integrity(blockchain):
    """Test the integrity of the blockchain."""
    # Add a valid block
    block = {
        "index": 1,
        "previous_hash": blockchain.chain[-1]["hash"],
        "timestamp": 123456789,
        "data": [{"sender": "Alice", "recipient": "Bob", "amount": 10}],
        "nonce": 123,
        "hash": "dummyhash"
    }
    blockchain.add_block(block)
    assert blockchain.validate_chain() is True

    # Tamper with a block
    blockchain.chain[-1]["data"] = [{"sender": "Charlie", "recipient": "Bob", "amount": 50}]
    assert blockchain.validate_chain() is False
