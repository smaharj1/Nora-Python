from amazon.api import AmazonAPI
from AWSCredentials import CredentialsExractor as AWSCredentials





class AmazonController:

    def __init__(self):
        cred = AWSCredentials.getAWSCredentials()
        self.amazon = AmazonAPI(cred['ACCESS_KEY'],cred['SECRET_KEY'],cred['LOCALE'])

    def searchProduct(self,product,category):

        tokens = product['tokens']
        tags = product['tags']

        results = []

        for token in tokens:
            query = self.amazon.search_n(1,Keywords=token, SearchIndex="All")
            if len(query) > 0:
                results.append(query[0])
        
        finalResults = []

        for result in results:
            finalResults.append({ 'title': result.title,
                        'price': result.price_and_currency,
                        'url': result.offer_url,
                        'image': result.small_image_url})

        return finalResults



a = AmazonController()
print(a.searchProduct({'tokens': ['PS4'], 'tags' : ['herp']}, "blerp"))
