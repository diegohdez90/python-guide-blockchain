from Crypto.PublicKey import RSA
import Crypto.Random as Random
import binascii

BITS = 1024


class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    def load_keys(self):
        try:
            with open("wallet.txt", mode="r") as f:
                keys = f.readlines()
                public_key = keys[0][:-1]
                private_key = keys[0]
                self.public_key = public_key
                self.private_key = private_key
        except (IOError, IndexError):
            print("Loading wallet failed!")

    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                with open("wallet.txt", mode="w") as f:
                    f.write(self.public_key)
                    f.write("\n")
                    f.write(self.private_key)
            except (IOError, IndexError):
                print("Saving wallet failed!")

    def generate_keys(self):
        private_key = RSA.generate(BITS, Random.new().read)
        public_key = private_key.public_key()
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))
