import requests
import json

class CapitalOne(object):  
    API_ID = "56c66be6a73e492741507558"  
    API_KEY = "492a87eea5a538d79e8485139235f42b"
    
    def __init__(self):
        pass

    def GetAllInformation(self, id):
        response = requests.get('http://api.reimaginebanking.com/customers/' + CapitalOne.API_ID + '/accounts?key=' + CapitalOne.API_KEY)
        print(response.text)

    def CreateAccount(self):
        url = 'http://api.reimaginebanking.com/customers/' + CapitalOne.API_ID + '/accounts?key=' + CapitalOne.API_KEY
        payload = {
        "type": "Checking",
        "nickname": "Main",
        "rewards": 10000,
        "balance": 512,	
        }

        response = requests.post( 
            url, 
            data=json.dumps(payload),
            headers={'content-type':'application/json'},
            )
        
        print(response.status_code)

        if response.status_code == 201:
            print('account created')

    def GetInfo(self, UserID, AccountID):
        url = 'http://api.reimaginebanking.com/customers/' + UserID + '/accounts?key=' + CapitalOne.API_KEY
        response = requests.get(url)
        
        data = None
        if(response.status_code == 200):
            data = response.json()
        else:
            return None
        
        result = None
        for obj in data:
            if obj['_id'] == AccountID:
                obj['id'] = AccountID
                del obj['_id']
                return obj
        
        return None
        



