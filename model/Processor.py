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
        imageUrl = "http://compass.xbox.com/assets/23/0d/230dc52a-8f0e-40bf-bbd1-c51fdb8371e3.png?n=Homepage-360-UA_Upgrade-big_1056x594.png"
        #info[0] = "+12016754068"
        #imageUrl = info[1]
        #phone = info[0]
        phone = "+12016754068"
        #google = Google()
        amazon = AmazonController()

        #tokens = google.GetTokens(imageUrl)
        #tags = google.GetLabels(imageUrl)

        tokens = ["samsung", "mobile phone"]
        itemInfo = amazon.searchProduct(tokens)

        print("Item info")
        print (itemInfo)

        return itemInfo
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


    
