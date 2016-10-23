from model.integration.google.Google import Google
from model.integration.amazon.AmazonController import AmazonController
from model.integration.twilio.TwilioController import TwilioController
from model.integration.capitalone.CapitalOne import CapitalOne
from model.data.Mongo import Mongo


class Processor(object):

    def __init__(self, db):
        self.db = db

    def ProcessImage(self, req):
        info = TwilioController.getMessage(req)
        imageUrl = info[1]
        phone = info[0]
        google = Google()
        amazon = AmazonController()

        tokens = google.GetTokens(imageUrl)
        itemInfo = amazon.searchProduct(tokens)

        print('Storing process results ...')
        # Log the query
        log = {
            'phone' : phone,
            'image' : imageUrl,
            'url' : itemInfo['url'],
            'title' : itemInfo['title'],
            'tokens' : tokens }

        self.db.LogQuery(log)
        self.db.UpdateWithPost(log)


    
