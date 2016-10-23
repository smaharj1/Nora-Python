from model.integration.google.Google import Google
from model.integration.amazon.AmazonController import AmazonController
from model.integration.twilio.TwilioController import TwilioController
from model.integration.capitalone.CapitalOne import CapitalOne


class Processor(object):

    def __init__(self):
        pass

    def ProcessImage(self, imageUrl, phone):
        
        google = Google()
        amazon = AmazonController()

        tokens = google.GetTokens(imageUrl)
        itemInfo = amazon.searchProduct(tokens)[0]
        print(tokens)
        print(itemInfo)
    
