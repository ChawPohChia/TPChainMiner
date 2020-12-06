from Mining import Mining
import requests

query = {'Miner':"123.123.123.123"}
response = requests.get('http://127.0.0.1:1234/mining/get-mining-job', params=query)
print(response.json())

mining= Mining(blockString="Try this", difficulty=5)
mining.mine()
mining.verifyBlockHash()
print("The end")