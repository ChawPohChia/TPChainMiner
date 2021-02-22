from Mining import Mining
import requests
from tkinter import *
from datetime import datetime

MinerIP="123.123.123.123"
def clicked():
    def printMessage(message):
        T.insert(END, "["+str(datetime.now())+"]" +message + "\n")
    query = {'Miner':MinerIP}
    response = requests.get('http://127.0.0.1:1234/mining/get-mining-job', params=query)
    miningDict=response.json()

    if (len(miningDict) !=0):
        mining= Mining(blockString=miningDict["Blockstring"], difficulty=miningDict["Difficulty"], index=miningDict["Index"])
    else:
       printMessage("There is no mining job available")
       return

    mining.mine()
    blockHashIsVerified=mining.verifyBlockHash()
    if (blockHashIsVerified):
        #print("Block is verified! Block was mined successfull with nonce: " + str(mining.nonce))
        printMessage("Block is verified! Block was mined successfull with nonce: " + str(mining.nonce))
        minedBlock={'MinedBy':MinerIP,"Blockindex":miningDict["Index"], "MinedNonce":str(mining.nonce)}
        response = requests.post('http://127.0.0.1:1234/mining/submit-mined-block', minedBlock)
        responseDict = response.json()
        if(responseDict["accepted"]):
            #print("Block is submitted and accepted. Returned message: "+responseDict["message"])
            printMessage("Block is submitted and accepted. Returned message: "+responseDict["message"])
        else:
            #print("Mined block submission was rejected! Reason: " + responseDict["message"])
            printMessage("Mined block submission was rejected! Reason: " + responseDict["message"])

    else:
        #print("Block nonce: " + str(mining.nonce) + " is INCORRECT for this block, please try to mine again")
        printMessage("Block nonce: " + str(mining.nonce) + " is INCORRECT for this block, please try to mine again")

window = Tk()
window.title("Welcome to TPChain Miner Programme")
window.geometry('350x350')
lbl = Label(window, text="Click to mine TP Chain from http://127.0.0.1:1234")
lbl.grid(column=0, row=0)
btn = Button(window, text="Start mining",command=clicked)
btn.grid(column=0, row=2)
lbl1 = Label(window, text="Logging:")
lbl1.grid(column=0, row=4)
T = Text(window, height=15, width=35)
T.grid(column=0, row=6)
T.insert(END, "["+str(datetime.now())+"]"+"Mining started at "+MinerIP+"..\n")
window.mainloop()


