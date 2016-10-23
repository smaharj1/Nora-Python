from amazon.api import AmazonAPI
from AWSCredentials import CredentialsExractor as AWSCredentials
import time




class AmazonController:

    def __init__(self):
        cred = AWSCredentials.getAWSCredentials()
        self.amazon = AmazonAPI(cred['ACCESS_KEY'],cred['SECRET_KEY'],cred['LOCALE'])

    def searchProduct(self, product):

        tokens = product['tokens']
        tags = product['tags']

        print("Searching for " + str(tokens))

        query = self.amazon.search_n(1,Keywords=tokens, SearchIndex="All")[0]
        
        result = { 'title': query.title,
                    'price': query.price_and_currency,
                    'url': query.offer_url,
                    'image': query.small_image_url}

        return result
