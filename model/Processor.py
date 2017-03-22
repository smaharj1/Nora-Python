from model.integration.google.Google import Google
from model.integration.amazon.AmazonController import AmazonController
#from model.integration.twilio.TwilioController import TwilioController
from model.integration.capitalone.CapitalOne import CapitalOne
from model.data.Mongo import Mongo


class Processor(object):

    def __init__(self, db):
        self.db = db
        self.amazon = AmazonController()

    def SearchWithKeyword(self, keywords):
        itemInfo = self.amazon.searchProduct(keywords)
        
        print "Items are : "
        
        result = self.filterLowestPrice(itemInfo)

        return result


    def filterLowestPrice(self, item):
        lowNew = item['lowNew']
        lowUsed = item['lowUsed']
        lowRefurbished = item['lowRefurbished']

        minimumVal = min(lowNew, lowUsed, lowRefurbished)
        result = {}
        
        if (minimumVal == lowNew):
            result['condition'] = "New"
            result['price'] = item['lowNewFormatted']
        elif minimumVal == lowUsed:
            result['condition'] = "Used"
            result['price'] = item['lowUsedFormatted']
        else:
            result['condition'] = "Refurbished"
            result['price'] = item['lowRefurbishedFormatted']

        result['offerURL'] = item['offerURL']
        result['detail'] = item['detailPage']

        return result

    def ProcessImage(self, imageUrl):
        # Get the image from the phone instead of twilio

        google = Google()

        tokens = google.GetTokens(imageUrl)
        searchString = tokens['tokens'] 
        searchString = searchString.split(' ', 1)[0]
        #searchString += ", " + str(tokens['tags'])
        #tags = google.GetLabels(imageUrl)
        print "the tokens are: "
        print tokens
        #tokens = ["samsung", "mobile phone"]
        itemInfo = self.amazon.searchProduct(searchString)

        result = self.filterLowestPrice(itemInfo)

        return result
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


    
