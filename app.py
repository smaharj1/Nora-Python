from flask import Flask, render_template, url_for, request, session, redirect, Response
from flask_pymongo import PyMongo
import twilio.twiml
from twilio.rest import TwilioRestClient
from model.data.Mongo import Mongo
from model.Accounts import Accounts
import json, random
from model.integration.twilio.TwilioController import TwilioController
from model.Processor import Processor

app = Flask(__name__)
db = Mongo(app)
PROCESSOR = Processor(db)

DemoURLs = [
    "http://compass.xbox.com/assets/23/0d/230dc52a-8f0e-40bf-bbd1-c51fdb8371e3.png?n=Homepage-360-UA_Upgrade-big_1056x594.png",
    "https://upload.wikimedia.org/wikipedia/commons/4/47/Soylent_2.0_2016.JPG",
    "https://tctechcrunch2011.files.wordpress.com/2015/08/tesla_model_s.jpg?w=738",
    "https://i.kinja-img.com/gawker-media/image/upload/s--6ERv6sIr--/18mjutor80kqxjpg.jpg",
    "http://media.bestofmicro.com/4/0/442080/original/Samsung-UHD.jpg",
    "http://lgcdn.baseballmonkey.com/80A850/magento/media/catalog/product/cache/5/small_image/600x/9df78eab33525d08d6e5fb8d27136e95/h/o/homerun-mizuno-baseball-glove-311808-pro-limited-edition-gmp300.jpg",
    "http://weknowyourdreams.com/images/scooter/scooter-08.jpg",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Coldplay_-_Ghost_Stories.png",
    "https://www.taylorguitars.com/sites/default/files/styles/multi_column_guitar_three/public/responsive-guitar-detail/Taylor-214ce-SB-DLX-fr-2014.png?itok=h5-4e-YW",
    "http://www.swstrings.com/image/GP-120?imageSize=4&index=0",
    "https://upload.wikimedia.org/wikipedia/en/2/2c/Skittles-Wrapper-Small.jpg",
    "http://images.asos-media.com/inv/media/3/1/1/0/3930113/black/image1xl.jpg",
    "https://images-na.ssl-images-amazon.com/images/I/71TtQbuOTgL._SL1000_.jpg"
]


@app.route('/', methods=['GET', 'POST'])
def Rootaschen():
    return render_template('index.html')


@app.route('/hello', methods=['POST'])
def Hello():
    data = TwilioController.getMessage(request)
    print(data)
    return data

@app.route('/createDemoUser', methods=['GET', 'POST'])
def CreateDemoUser():
    result = Accounts.CreateNewUser(db, {'name' : 'Herb Muddlefoot', 
        'phone': '+19084774708', 
        'account_id' : '56c66be6a73e492741507558', 
        'account_number': '580bb39d360f81f104544dc0', 
        'items' : [],
        'tags' : {}})
    
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
    Accounts.UpdateBankInfo(db, '+19084774708')
    return "Updated."
    

@app.route('/getUserData', methods=['GET'])
def GetUserData():
    phone = '+19084774708'
    result = Accounts.GetUserData(db, phone)

    if not result == None:
        del result['_id']

        for i in range(0, len(result['items'])):
            try:
                del result['items'][i]['_id']
            except:
                pass
        resp = Response(json.dumps(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    resp = Response(json.dumps({}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/ProcessImage', methods=['GET', 'POST'])
def ProcessImage():
    PROCESSOR.ProcessImage(request)
    return "Good stuff\n"


@app.route('/bankAnalytics', methods=['POST'])
def BankAnalytics():
    print("Her we go")
    phone = request.values.get('phone')
    image = request.values.get('url')
    Accounts.UpdateBankInfo(db, phone)
    results = Accounts.GetBankStats(db, phone, image)
    resp = Response(json.dumps(results))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/deleteItem', methods=['POST'])
def DeleteItem():
    phone = request.values.get('phone')
    image = request.values.get('url')