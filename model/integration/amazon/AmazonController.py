from amazon.api import AmazonAPI
from AWSCredentials import CredentialsExractor as AWSCredentials

class AmazonController:

    def __init__(self):
        cred = AWSCredentials.getAWSCredentials()
        self.amazon = AmazonAPI(cred['ACCESS_KEY'],cred['SECRET_KEY'],cred['LOCALE'])

    def searchProduct(self,product,category):
        self.product = self.amazon.search_n(1,Keywords = product, SearchIndex = category, Sort="price")
        returnProd={ 'title': self.product[0].title,
                      'price': self.product[0].price_and_currency,
                      'url': self.product[0].offer_url,
                      'image': self.product[0].small_image_url,
         }
        return returnProd
