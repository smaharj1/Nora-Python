from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import twilio.twiml
from twilio.rest import TwilioRestClient
from model.integration.twilio.TwilioController import TwilioController
from model.data.Mongo import Mongo
from model.Accounts import Accounts


app = Flask(__name__)
db = Mongo(app)

@app.route('/hello', methods=['POST'])
def Hello():
    data = TwilioController.getMessage(request)
    print(data)
    return data

@app.route('/createUser', methods=['GET', 'POST'])
def CreateUser():
    result = Accounts.CreateNewUser(db, {'name' : 'Herb Muddlefoot', 
                    'phone': '908-477-4708', 
                    'account_id' : '56c66be6a73e492741507558', 
                    'account_number': '580bb39d360f81f104544dc0', 
                    'items' : []})
    
    if result == 0:
        print('User created.\n')
    if result == 1:
        print('Inavid user data.\n')
    if result == 2:
        print('User already exists.\n')
    if result == 3:
        print('User bank account could not be found.\n')

    return str(result) + '\n'


@app.route('/updateUser', methods=['GET', 'POST'])
def UpdateUserBankInfo():
    Accounts.UpdateBankInfo(db, '908-477-4708')
    return "Updated."
    

@app.route('/getUserData', methods=['GET'])
def GetUserData():
    phone = '908-477-4708'
    return str(Accounts.GetUserData(db, phone))







if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



