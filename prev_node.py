from uuid import uuid4
from blockchain import Blockchain
from utils.verification import Verification
from wallet import Wallet


class Node:

    def __init__(self):
        # self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_value(self):
        """Input to retrieve value from command prompt

        Returns:
            float: Value to be added in blockchain array
        """
        tx_recipient = input("Enter the recipient of the transaction: ")
        tx_amount = float(input("Your amount transaction please: "))

        return tx_recipient, tx_amount

    def get_user_choice(self):
        return input("Your choice: ")

    def get_blockchain_elements(self):
        for block in self.blockchain.chain:
            print("Output block")
            print(block)
        else:
            print("-" * 20)

    def listen_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print("Please choice")
            print("1. Add a new transaction")
            print("2. Mine a new block")
            print("3. Output blockchain blocks")
            print("4. Transaction validity")
            print("5. Create wallet")
            print("6. Load Wallet")
            print("7. Save keys")
            print("q. Quit")
            choice = self.get_user_choice()
            if choice == "1":
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(
                    self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print('Transaction added!')
                else:
                    print('Transaction Failed!')
                print(self.blockchain.get_open_transactions())
            elif choice == '2':
                if not self.blockchain.mine_block():
                    print("Mining failed. Got no wallet?")
            elif choice == '3':
                self.get_blockchain_elements()
            elif choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif choice == "7":
                self.wallet.save_keys()
            elif choice == "q":
                waiting_for_input = False
            else:
                print("Input invalid")

            if not Verification.verify_chain(self.blockchain.chain):
                self.get_blockchain_elements()
                print("Invalid blockchain")
                break

            print("Balance of {}: {:.2f}".format(
                self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print("User left!")

        print("Done!")


if __name__ == '__main__':

    node = Node()
    node.listen_for_input()
