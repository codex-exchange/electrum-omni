import requests, getpass
import time, json
import random


class RPCHostOmni():
    def __init__(self):
        USER = getpass.getuser()
        self._session = requests.Session()
        # self._url = daemon_url
        self._headers = {'content-type': 'application/json'}
        self.id = random.randrange(2**31 - 1)

    def set_url(self, daemon_url):
        self._url = daemon_url

    def call(self, rpcMethod, *params):
        self.id += 1
        payload = json.dumps({"id": str(self.id), "method": rpcMethod, "params": list(params), "jsonrpc": "2.0"})
        tries = 10
        hadConnectionFailures = False
        while True:
            try:
                response = self._session.post(self._url, headers=self._headers, data=payload, verify=False)
            except requests.exceptions.ConnectionError:
                tries -= 1
                if tries == 0:
                    raise Exception('Failed to connect for remote procedure call.')
                hadFailedConnections = True
                print(
                    "Couldn't connect for remote procedure call, will sleep for ten seconds and then try again ({} more tries)".format(
                        tries))
                time.sleep(10)
            else:
                if hadConnectionFailures:
                    print('Connected for remote procedure call after retry.')
                break
        if not response.status_code in (200, 500):
            raise Exception('RPC connection failure: ' + str(response.status_code) + ' ' + response.reason)
        responseJSON = response.json()
        if 'error' in responseJSON and responseJSON['error'] != None:
            raise Exception('Error in ' + rpcMethod + ' RPC call: ' + str(responseJSON['error']))
        # return responseJSON['result']
        return responseJSON

    # Bitcoin Generic RPC calls
    def importAddress(self, addr):
        return self.call("importaddress", addr)

    def listUnspent(self, addr):
        return self.call("listunspent", 0, 999999, "\'[\"" + addr + "\"]\'")

    def getRawTransaction(self, txid):
        return self.call("getrawtransaction", txid, 1)

    def sendRawTransaction(self, tx):
        try:
            return self.call("sendrawtransaction", tx)
        except Exception as e:
            return e

    def validateAddress(self, addr):
        return self.call("validateaddress", addr)

    def createRawTransaction(self, ins, outs):
        return self.call("createrawtransaction", ins, outs)

    def decodeRawTransaction(self, rawtx):
        return self.call("decoderawtransaction", rawtx)

    def estimateFee(self, blocks=4):
        return self.call("estimatefee", blocks)

    ## Omni Specific RPC calls
    def getBalance(self, addr, propertyid):
        return self.call("omni_getbalance", addr, propertyid)

    def getAllBalancesForAddress(self, addr):
        return self.call("omni_getallbalancesforaddress", addr)

    def getTransaction(self, tx):
        return self.call("omni_gettransaction", tx)

    def decodeTransaction(self, rawtx):
        return self.call("omni_decodetransaction", rawtx)

    def listProperties(self):
        return self.call("omni_listproperties")

    def getProperty(self, propertyid):
        return self.call("omni_getproperty", propertyid)

    def getSimplesendPayload(self, propertyid, amount):
        return self.call("omni_createpayload_simplesend", int(propertyid), amount)

    def createRawTxOpReturn(self, payload, rawtx=None):
        return self.call("omni_createrawtx_opreturn", rawtx, payload)

    def createRawTxInput(self, txhash, index, rawtx=None):
        return self.call("omni_createrawtx_input", rawtx, txhash, index)

    def createRawTxReference(self, destination, rawtx=None):
        return self.call("omni_createrawtx_reference", rawtx, destination, 0.00000546)

