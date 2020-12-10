from Mining import Mining
import requests

MinerIP="123.123.123.123"
query = {'Miner':MinerIP}
response = requests.get('http://127.0.0.1:1234/mining/get-mining-job', params=query)
miningDict=response.json()

mining= Mining(blockString=miningDict["Blockstring"], difficulty=miningDict["Difficulty"], index=miningDict["Index"])
mining.mine()
blockHashIsVerified=mining.verifyBlockHash()
if (blockHashIsVerified):
    print("Block is verified! Block was mined successfull with nonce: " + str(mining.nonce))
    minedBlock={'MinedBy':MinerIP,"Blockindex":miningDict["Index"], "MinedNonce":str(mining.nonce)}
    BlockSubmissionResponse = requests.post('http://127.0.0.1:1234/mining/submit-mined-block', minedBlock)
else:
    print("Block nonce: " + str(mining.nonce) + " is INCORRECT for this block, please try to mine again")

