from functools import reduce
import json


from utils.hash import hash_block
from utils.verification import Verification
from classes.block import Block
from classes.transaction import Transaction


# Initializing blockchain list
MINING_REWARD = 10

blockchain = []
open_transactions = []
owner = "Diego"


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
                tx_transactions = [Transaction(
                    tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]
                updated_block = Block(
                    block['index'], block['previous_hash'], tx_transactions, block['proof'], block['timestamp'])
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(file_content[1])
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = Transaction(
                    tx['sender'], tx['recipient'], tx['amount'])
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
            saveable_chain = [block.__dict__ for block in [Block(el.index, el.previous_hash, [
                                                                 t_el.__dict__ for t_el in el.transactions], el.proof, el.timestamp) for el in blockchain]]
            f.write(json.dumps(saveable_chain))
            f.write("\n")
            saveable_transaction = [
                tx.__dict__ for tx in open_transactions]
            f.write(json.dumps(saveable_transaction))
    except IOError as e:
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

    transaction = Transaction(sender, recipient, amount)
    verifier = Verification()
    if verifier.verify_transaction(transaction, get_balance):
        open_transactions.append(transaction)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = Transaction('MINING', owner, MINING_REWARD)
    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)
    block = Block(len(blockchain), hashed_block, copied_transaction, proof)
    blockchain.append(block)
    return True


def get_balance(participant):
    tx_sender = [[tx.amount for tx in block.transactions
                  if tx.sender == participant] for block in blockchain]
    open_tx_sender = [tx.amount
                      for tx in open_transactions if tx.sender == participant]
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    amount_sent = reduce(
        lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_sender, 0)
    tx_recipient = [[tx.amount for tx in block.transactions
                     if tx.recipient == participant] for block in blockchain]
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


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    verifier = Verification()
    while not verifier.valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


waiting_for_input = True


while waiting_for_input:
    print("Please choice")
    print("1. Add a new transaction")
    print("2. Mine a new block")
    print("3. Output blockchain blocks")
    print("4. Transaction validity")
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
        verifier = Verification()
        if verifier.verify_transactions(open_transactions, get_balance):
            print("All transactions are valid")
        else:
            print("There are invalid transactions")
    elif choice == "q":
        waiting_for_input = False
    else:
        print("Input invalid")

    verifier = Verification()
    if not verifier.verify_chain(blockchain):
        get_blockchain_elements()
        print("Invalid blockchain")
        break

    balance = get_balance('Diego')
    print("Balance of {}: {:.2f}".format("Diego", balance))
else:
    print("User left!")

print("Done!")
