#from amazon.api import AmazonAPI
import amazonproduct
from AWSCredentials import CredentialsExractor as AWSCredentials
import time




class AmazonController:

    def __init__(self):
        
        cred = AWSCredentials.getAWSCredentials()
        #self.amazon = amazonproduct.API(locale='us')
        self.amazon = amazonproduct.API(cfg='C:\Users\sujil\Documents\.amazon-product-api', locale='us')
        print("Amazon product API connected...")
        
        #self.amazon = AmazonAPI(cred['ACCESS_KEY'],cred['SECRET_KEY'],cred['LOCALE'])

    def searchProduct(self, product):

        #tokens = product['tokens']
        #tags = product['tags']

        tokens = ''.join([product[0]," ",product[1]])
        

        print("Searching for " + str(tokens))

        #result = self.amazon.search_n(5,Keywords=tokens, SearchIndex="All")
        
        result = self.amazon.item_lookup(tokens)


        #result = { 'title': query.title,
        #            'price': query.price_and_currency,
        #            'url': query.offer_url,
        #            'image': query.small_image_url}

        return result
