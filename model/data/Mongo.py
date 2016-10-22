
from flask import Flask
from flask_pymongo import PyMongo


class Mongo(object):
    
    def __init__(self, app):
        app.config['MONGO_DBNAME'] = 'Nora'
        self.mongo = PyMongo(app, config_prefix='MONGO')

    def UpdateFields(self, phone, fields):
        self.mongo.db.Users.update({'phone' : phone}, { '$set' : {'balance' : fields['balance'], 'rewards' : fields['rewards']} }, upsert=False)

    def Find(self, phone):
        cursor = self.mongo.db.Users.find({'phone' : phone})
        if(cursor.count() == 0):
            return None
        else:
            return cursor[0]


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

    


