from time import time

from utils.printable import Printable


class Block(Printable):

    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time
        self.proof = proof
