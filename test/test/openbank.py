import requests

_baseURL = "https://ulsterbank.openbankproject.com/obp/v1.2.1/banks/ulster/accounts/"

class Transaction:
   def __init__(self, txid, posted, value):
       self.txid = txid
       self.posted = posted
       self.value = value

class account:
   def getBalance (self, AccountID):
       url = "{0}{1}/public/account".format(_baseURL, AccountID)
       response = requests.get(url, headers={"obp_limit":"1","obp_offset":"2"})
       return response.json()['balance']

   def getTransactions (self, AccountID):
       transactionList = []
       url = "{0}{1}/public/transactions".format(_baseURL, AccountID)
       response = requests.get(url, headers={"obp_limit":"2","obp_offset":"2"})
       for tx in response.json()['transactions']:
           #print tx['id']
           #print tx['details']['posted']
           #print tx['details']['value']
           #tx =Transaction(tx['id'],tx['details']['posted'],tx['details']['value'])
           #print tx.txid
           transactionList.append({"ID":tx['id'],"POSTED":tx['details']['posted'],
                                   "AMOUNT":tx['details']['value']['amount'],
                                   "CCY":tx['details']['value']['currency']})
       return transactionList # json.dumps(transactionList.__dict__)