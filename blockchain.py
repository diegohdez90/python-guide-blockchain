from functools import reduce
from collections import OrderedDict
import hashlib as hl
import json


from utils.hash import hash_block, hash_string_256
from classes.block import Block


# Initializing blockchain list
MINING_REWARD = 10

blockchain = []
open_transactions = []
owner = "Diego"
participants = {
    "Diego"
}


def load_load():
    global blockchain
    global open_transactions
    global genesis_block
    try:
        with open("data.txt", mode="r") as f:
            file_content = f.readlines()
            blockchain = json.loads(file_content[0][:-1])
            updated_blockchain = []
            for block in blockchain:
                tx_transactions = [
                    OrderedDict(
                        [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]
                updated_block = Block(
                    block['index'], block['previous_hash'], tx_transactions, block['proof'], block['timestamp'])
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(file_content[1])
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = OrderedDict(
                    [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
    except (IOError, IndexError):
        genesis_block = Block(previous_hash="", index=0,
                              transactions=[], proof=100)
        blockchain = [genesis_block]
        open_transactions = []
    except ValueError:
        print('Value Error')
    except:
        print("Wildcard!")
    finally:
        print("Cleanup!")


load_load()


def save_data():
    try:
        with open('data.txt', mode="w") as f:
            saveable_chain = [block.__dict__ for block in blockchain]
            f.write(json.dumps(saveable_chain))
            f.write("\n")
            f.write(json.dumps(open_transactions))
    except IOError:
        print(e)


def get_last_blockchain_value():
    """ Return last value """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain to the blockchain 

    Args:
        sender (_type_): The sender of the coin
        recipient (_type_): The recipient of the coins
        amount (float, optional): The amount of coins sent with the transaction. Defaults to 1.0.
    """

    transaction = OrderedDict([(
        'sender', sender,
    ), (
        'recipient', recipient
    ), (
        'amount', amount
    )])

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = OrderedDict([(
        'sender', 'MINING',
    ), (
        'recipient', owner,
    ), (
        'amount', MINING_REWARD
    )])
    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)
    block = Block(len(blockchain), hashed_block, copied_transaction, proof)
    blockchain.append(block)
    return True


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block.transactions
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    amount_sent = reduce(
        lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_sender, 0)
    tx_recipient = [[tx['amount'] for tx in block.transactions
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(
        lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_recipient, 0)
    return amount_received - amount_sent


def get_transaction_value():
    """Input to retrieve value from command prompt

    Returns:
        float: Value to be added in blockchain array
    """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your amount transaction please: "))
    return tx_recipient, tx_amount


def get_user_choice():
    return input("Your choice: ")


def get_blockchain_elements():
    for block in blockchain:
        print("Output block")
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    """Verify the current blockchain

    Returns:
        Boolean: Returns True if block is valid otherwise returns False
    """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block.previous_hash != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
            print('Proof of work is invalid')
            return False
    return True


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    return guess_hash[0:2] == "00"


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


waiting_for_input = True


while waiting_for_input:
    print("Please choice")
    print("1. Add a new transaction")
    print("2. Mine a new block")
    print("3. Output blockchain blocks")
    print("4  Output participants")
    print("5. Transaction validity")
    print("q. Quit")
    choice = get_user_choice()
    if choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Transaction added!')
        else:
            print('Transaction Failed!')
        print(open_transactions)
    elif choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif choice == '3':
        get_blockchain_elements()
    elif choice == '4':
        print(participants)
    elif choice == '5':
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("There are invalid transactions")
    elif choice == "q":
        waiting_for_input = False
    else:
        print("Input invalid")

    if not verify_chain():
        get_blockchain_elements()
        print("Invalid blockchain")
        break

    balance = get_balance('Diego')
    print("Balance of {}: {:.2f}".format("Diego", balance))
else:
    print("User left!")

print("Done!")
