# script.py

# Simulates a node validator in a PoS network

import time
import random

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Simplified hash function for demonstration purposes
        return str(self.index) + str(self.timestamp) + str(self.transactions) + self.previous_hash

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Validator:
    def __init__(self, id):
        self.id = id
        self.balance = 1000  # Initial stake

    def validate_block(self, block):
        # Simulate block validation - check hash, previous hash, transactions
        print(f"Validator {self.id} validating block {block.index}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate validation time
        if block.hash != block.calculate_hash():
            raise Exception("Invalid block hash")
        # Add more validation checks here
        return True

    def propose_block(self, transactions):
        # Simulate block proposal - create a new block
        previous_block = blockchain[-1] if blockchain else None
        previous_hash = previous_block.hash if previous_block else "0"
        new_block = Block(len(blockchain), time.time(), transactions, previous_hash)
        return new_block

    def sign_block(self, block):
        # Simulate block signing - add validator's signature
        print(f"Validator {self.id} signing block {block.index}")
        time.sleep(random.uniform(0.1, 0.3)) # Simulate signing time
        block.signature = f"Signature from validator {self.id}"
        return block

blockchain = []
validators = [Validator(i) for i in range(1, 4)]

while True:
    # Simulate transaction generation
    transactions = [Transaction(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for _ in range(random.randint(1, 5))]

    # Select a validator to propose a block
    proposer = random.choice(validators)
    new_block = proposer.propose_block(transactions)

    # Validate the block by other validators
    valid = True
    for validator in validators:
        if validator != proposer and not validator.validate_block(new_block):
            valid = False
            break

    if valid:
        # Sign the block
        signed_block = proposer.sign_block(new_block)
        blockchain.append(signed_block)
        print(f"Block {signed_block.index} added to blockchain. Hash: {signed_block.hash}")

    time.sleep(2)
