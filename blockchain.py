import functools

# Initializing blockchain list
MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Diego"
participants = {
    "Diego"
}


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

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transaction
    }
    blockchain.append(block)
    return True


def hash_block(last_block):
    return '-'.join([str(last_block[key]) for key in last_block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amount: tx_sum + tx_amount[0] if len(tx_amount) > 0 else 0, tx_sender, 0)
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(
        lambda tx_sum, tx_amount: tx_sum + tx_amount[0] if len(tx_amount) > 0 else 0, tx_recipient, 0)
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
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True


while waiting_for_input:
    print("Please choice")
    print("1. Add a new transaction")
    print("2. Mine a new block")
    print("3. Output blockchain blocks")
    print("4  Output participants")
    print("5. Transaction validity")
    print("h. Manipulate the chain")
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
    elif choice == '3':
        get_blockchain_elements()
    elif choice == '4':
        print(participants)
    elif choice == '5':
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("There are invalid transactions")
    elif choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{
                    'sender': "Chris",
                    'recipient': "Diego",
                    'amount': 99.99
                }]
            }
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
