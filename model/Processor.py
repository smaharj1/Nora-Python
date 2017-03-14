from model.integration.google.Google import Google
from model.integration.amazon.AmazonController import AmazonController
#from model.integration.twilio.TwilioController import TwilioController
from model.integration.capitalone.CapitalOne import CapitalOne
from model.data.Mongo import Mongo


class Processor(object):

    def __init__(self, db):
        self.db = db

    def ProcessImage(self, req):
        # Get the image from the phone instead of twilio
        
        #info = TwilioController.getMessage(req)
        info = []
        #info[1] = 
        imageUrl = "https://www.sanrio.com/media/W1siZiIsIjIwMTYvMDYvMTMvMTQvMTEvNDAvMTQvY2hhcmFjdGVyX2Jhbm5lcl9oZWxsb2tpdHR5LnBuZyJdXQ/character_banner_hellokitty.png?sha=95006e8644727395"
        #info[0] = "+12016754068"
        #imageUrl = info[1]
        #phone = info[0]
        phone = "+12016754068"
        google = Google()
        #amazon = AmazonController()

        tokens = google.GetTokens(imageUrl)
        tags = google.GetLabels(imageUrl)
        #itemInfo = amazon.searchProduct(tokens)

        print('Storing process results ...')
        # Log the query
        #log = { 'phone' : phone,
        #        'image' : imageUrl,
        #        'url' : itemInfo['url'],
        #        'title' : itemInfo['title'],
        #        'tokens' : tokens,
        #        'tags' : tags,
        #        'price' : itemInfo['price'] }

        #self.db.LogQuery(log)
        #self.db.UpdateWithPost(log)
        #self.db.UpdateTags(phone, tags)


    
