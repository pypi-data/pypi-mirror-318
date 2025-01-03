import pytest
from sallmon.core.transaction import Transaction

@pytest.fixture
def valid_transaction():
    """Fixture to provide a valid transaction."""
    return Transaction(sender="Alice", recipient="Bob", amount=10)

def test_transaction_creation(valid_transaction):
    """Test creating a transaction."""
    assert valid_transaction.sender == "Alice"
    assert valid_transaction.recipient == "Bob"
    assert valid_transaction.amount == 10

def test_invalid_transaction():
    """Test creating an invalid transaction."""
    with pytest.raises(ValueError):
        Transaction(sender="Alice", recipient="Bob", amount=-10)

def test_transaction_to_dict(valid_transaction):
    """Test transaction serialization."""
    tx_dict = valid_transaction.to_dict()
    assert tx_dict["sender"] == "Alice"
    assert tx_dict["recipient"] == "Bob"
    assert tx_dict["amount"] == 10
