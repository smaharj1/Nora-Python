
from flask import Flask
from flask_pymongo import PyMongo


class Mongo(object):
    
    def __init__(self, app):
        app.config['MONGO_DBNAME'] = 'nora'
        self.mongo = PyMongo(app, config_prefix='MONGO')

    def UpdateBankFields(self, phone, fields):
        self.mongo.db.Users.update({'phone' : phone}, { '$set' : {'balance' : fields['balance'], 'rewards' : fields['rewards']} }, upsert=False)

    def Find(self, phone):
        cursor = self.mongo.db.Users.find({'phone' : phone})
        if(cursor.count() == 0):
            return None
        else:
            return cursor[0]
    
    def appendPhoto(self, userID, userData):

        listFound = self.mongo.db.noradata.find({'_id': str(userID)})
        
        if listFound.count() != 0:
            data = listFound[0]['photos']
            data.append(userData)

            self.mongo.db.noradata.update({'_id': str(userID)}, {'$set': {'photos': data}}, upsert=False)


    def FindData(self, username, password):
        '''Returns the id if the user provided information is correct'''
        result = self.mongo.db.norauser.find({'username':username, 'password': password})

        if (result.count() == 0):
            return None
        else:
            res = result[0]
            return str(res['_id'])


    def CreateAuth(self, userData):
        findInfo =  self.FindData(userData['username'], userData['pswd'])

        if findInfo is None:
            returnID = self.mongo.db.norauser.insert({'username': userData['username'], 'password': userData['pswd']})
            self.mongo.db.noradata.insert({
                '_id': str(returnID), 
                'name': userData['name'],
                'photos': []
                })

            return True
        else:
            return False

    def CreateUser(self, data):
        self.mongo.db.Users.insert_one(data)


    def CheckForUser(self, phone):
        result = self.mongo.db.Users.find({'phone' : phone})
        count = 0
        for thing in result:
            count += 1
        if count > 0:
            return True
        else:
            return False


    def GetUserData(self, phone):
        user = self.Find(phone)
        if user == None:
            return None
        
        return user
    

    def LogQuery(self, queryobj):
        self.mongo.db.Queries.insert_one(queryobj)


    def UpdateWithPost(self, data):
        try:
            current = self.Find(data['phone'])['items']

            if current == None:
                print("No results for storing data ...")
                return None

            current.append(data)
            self.mongo.db.Users.update({'phone' : data['phone']}, { '$set' : {'items' : current} }, upsert=False)

        except Exception as e:
            print('Mongo: ' + str(e))


    def UpdateTags(self, phone, tags):
        try:
            current = self.Find(phone)['tags']
        except:
            current = None
            return
        print(current)
        if current == None:
            print("No document found ...")
            return None
            
        for tag in tags:
            if tag in current:
                current[tag] =  current[tag] + 1
            else:
                current[tag] = 1

        self.mongo.db.Users.update({'phone' : phone}, { '$set' : {'tags' : current} }, upsert=False)



    def GetBalanceAndPrice(self, phone, url):

        user = self.Find(phone)
        balance = user['balance']
        items = user['items']

        for item in items:
            if item['image'] == url:
                return (balance, item['price'], item['title'], item['tokens'], item['url'])
        print("Returingn none")
        return None


    def DeleteItem(self, phone, url):
        
        return None


