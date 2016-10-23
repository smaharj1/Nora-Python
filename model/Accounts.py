from integration.capitalone.CapitalOne import CapitalOne
from model.BalanceAnalytics import BalanceAnalytics

class Accounts(object):


    @staticmethod
    def CreateNewUser(db, data):
        if not Accounts.VerifyUserData(data):
            return 1
        if Accounts.CheckForUser(db, data['phone']):
            return 2

        co = CapitalOne()

        bankinfo = co.GetInfo(data['account_id'], data['account_number'])
        
        if bankinfo == None:
            return 3
        
        for key, val in bankinfo.iteritems():
            data[key] = val

        db.CreateUser(data)

        return 0

    @staticmethod
    def UpdateBankInfo(db, phone):
        co = CapitalOne()
        doc = db.Find(phone)

        id = doc['account_id']
        account = doc['account_number']

        bankinfo = co.GetInfo(id, account)
        db.UpdateBankFields(phone, bankinfo)

        
    @staticmethod
    def GetUserData(db, phone):
        return db.GetUserData(phone)

    @staticmethod
    def CheckForUser(db, phone):
        return db.CheckForUser(phone)

    @staticmethod
    def VerifyUserData(data):
        try:
            data['name']
            data['phone']
            data['account_id']
            data['account_number']
            
        except:
            return False
        return True
    
    @staticmethod
    def GetBankStats(db, phone, url):
        balance, price = db.GetBalanceAndPrice(phone, url)
        results = BalanceAnalytics.checkBalanceChangeEffects(price[0], balance)
        return results



