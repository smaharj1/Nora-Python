
from flask import Flask
from flask_pymongo import PyMongo

class Mongo(object):
    
    def __init__(self, app):
        app.config['MONGO_DBNAME'] = 'Nora'
        self.mongo = PyMongo(app, config_prefix='MONGO')

    
    



