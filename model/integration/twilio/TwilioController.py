import twilio.twiml
import requests
import json
from twilio.rest import TwilioRestClient

class TwilioController:

    client = TwilioRestClient()

    @staticmethod
    def getMessage(req):
        from_number = req.values.get('From')
        """for key, val in req.values.iteritems():
            print(str(key) + " : " + str(val))
        response = requests.get(req.values.get('MediaUrl0') + '.json')
        print(response.text)
        json_data = json.loads(response.text)
        messageURL = json_data['Location']
        print(messageURL)"""
        messageURL = req.values.get('MediaUrl0')
        return (from_number,messageURL)




   