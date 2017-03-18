#from amazon.api import AmazonAPI
import amazonproduct
from AWSCredentials import CredentialsExractor as AWSCredentials
import time

from lxml import etree
import xmltodict
import json

class AmazonController:

    def __init__(self):
        
        cred = AWSCredentials.getAWSCredentials()
        #self.amazon = amazonproduct.API(locale='us')
        self.amazon = amazonproduct.API(cfg='C:\Users\sujil\Documents\.amazon-product-api', locale='us')
        print("Amazon product API connected...")
        
        #self.amazon = AmazonAPI(cred['ACCESS_KEY'],cred['SECRET_KEY'],cred['LOCALE'])

    def searchProduct(self, product):

        tokens = product['tokens']
        #tags = product['tags'][0]

        #tokens = ''.join([product[0]," ",product[1]])
        
        #tokens = ''.join(tokens + " " + tags)

        print("Searching for " + str(tokens))

        result = self.amazon.item_search('All', Keywords=tokens)

        count = 0
        asin = ""
        for item in result:
            if count < 1:
               
                asin= item.ASIN
                count += 1
            else:
                break

        result = self.amazon.item_lookup(str(asin), ResponseGroup="Offers")

        #o = xmltodict.parse(etree.tostring(result.Items))
        #print(json.dumps(o,indent=4, separators=(',', ': ')))

        summary = result.Items.Item.OfferSummary
        offers = result.Items.Item.Offers

        data = {}

        if summary.TotalNew > 0 :
            data['lowNew'] = int(summary.LowestNewPrice.Amount)
            data['lowNewFormatted'] = str(summary.LowestNewPrice.FormattedPrice)

        if summary.TotalUsed > 0 :
            data['lowUsed'] = int(summary.LowestUsedPrice.Amount)
            data['lowUsedFormatted'] = str(summary.LowestUsedPrice.FormattedPrice)
        
        if summary.TotalNew > 0 :
            data['lowRefurbished'] = int(summary.LowestNewPrice.Amount)
            data['lowRefurbishedFormatted'] = str(summary.LowestNewPrice.FormattedPrice)

        data['offerURL'] = str(offers.MoreOffersUrl)


        return data
