import hashlib
import json

# Example block data
block_data = {
    "previous_hash": "previous_block_hash",
    "timestamp": "2025-01-02T22:30:00Z",
    "coinbase": {
        "type": "coinbase",
        "amount": 50,
        "sender": "system",
        "recipient": "miner-wallet-address",
        "timestamp": "2025-01-02T22:30:00Z"
    },
    "miner_address": "miner-wallet-address",
    "reward": 50,
    "transaction_count": 1,
    "difficulty": 3,
    "transactions": []
}

# Perform proof of work
difficulty = block_data["difficulty"]
block_data_str = json.dumps(block_data, sort_keys=True)
nonce = 0
while True:
    block_hash = hashlib.sha256(f"{block_data_str}-{nonce}".encode()).hexdigest()
    if block_hash.startswith("0" * difficulty):  # Adjust leading zeros for difficulty
        break
    nonce += 1

# Update block data
block_data["block_hash"] = block_hash
block_data["nonce"] = nonce

print("Valid Block Data:")
print(json.dumps(block_data, indent=4))
