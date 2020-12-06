from hashlib import sha256

class Mining:
    # For miner program will only take in blockHash input.
    def __init__(self, blockString, difficulty):
        self.difficulty=difficulty
        self.blockString = blockString
        self.nonce = 0
        self.minedBy = None;  # to be filled in by miner
        self.blockHash = None;  # to be filled in by miner

    def mine(self):
        print("Mining is started...")
        blockHash = sha256((self.blockString + str(self.nonce)).encode()).hexdigest()
        while not blockHash.startswith('0' * self.difficulty):
            self.nonce += 1
            blockHash = sha256((self.blockString + str(self.nonce)).encode()).hexdigest()
        self.blockHash = blockHash;
        print("Nonce found for this block: "+ str(self.nonce))
        print("Blockhash: " + self.blockHash)

    def verifyBlockHash(self):
        blockHash = sha256((self.blockString + str(self.nonce)).encode()).hexdigest()
        if (blockHash.startswith('0' * self.difficulty)):
            print("Block is verified! Block was mined successfull with nonce: " + str(self.nonce))
        else:
            print("Block nonce: " + str(self.nonce) + " is INCORRECT for this block, please try to mine again")
        return (blockHash.startswith('0' * self.difficulty))