from Mining import Mining
import requests

query = {'Miner':"123.123.123.123"}
response = requests.get('http://127.0.0.1:1234/mining/get-mining-job', params=query)
miningDict=response.json()

mining= Mining(blockString=miningDict["Blockstring"], difficulty=miningDict["Difficulty"], index=miningDict["Index"])
mining.mine()
blockHashIsVerified=mining.verifyBlockHash()
if (blockHashIsVerified):
    print("Block is verified! Block was mined successfull with nonce: " + str(mining.nonce))
else:
    print("Block nonce: " + str(mining.nonce) + " is INCORRECT for this block, please try to mine again")
