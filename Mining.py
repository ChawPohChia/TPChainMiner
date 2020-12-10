from hashlib import sha256

class Mining:
    # For miner program will only take in blockHash input.
    def __init__(self, blockString, difficulty, index):
        self.blockIndex=index
        self.difficulty=difficulty
        self.blockString = blockString
        self.nonce = 0
        self.minedBy = None;  # to be filled in by miner
        self.blockHash = None;  # to be filled in by miner

    def mine(self):
        print("Mining is started...")
        print("Difficuly: " + str(self.difficulty))
        print("Block index: "+str(self.blockIndex))
        print("Blockstring: " + self.blockString)
        blockHash = sha256((self.blockString + str(self.nonce)).encode()).hexdigest()
        while not blockHash.startswith('0' * self.difficulty):
            self.nonce += 1
            blockHash = sha256((self.blockString + str(self.nonce)).encode()).hexdigest()
        self.blockHash = blockHash;
        print("Nonce found for this block: "+ str(self.nonce))
        print("Blockhash: " + self.blockHash)

    def verifyBlockHash(self):
        blockHash = sha256((self.blockString + str(self.nonce)).encode()).hexdigest()
        return (blockHash.startswith('0' * self.difficulty))