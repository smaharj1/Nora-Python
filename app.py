from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import twilio.twiml
from twilio.rest import TwilioRestClient


app = Flask(__name__)

@app.route('/hello')
def Hello(methods='GET'):
    return "Hey there"





