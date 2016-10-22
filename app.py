from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import twilio.twiml
from twilio.rest import TwilioRestClient
from model.integration.twilio.TwilioController import TwilioController


app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def Hello():
    data = TwilioController.getMessage(request)
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')





