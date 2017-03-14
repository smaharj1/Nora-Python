import os

class CredentialsExractor:

    @staticmethod
    def getAWSCredentials():
        credentials = {}
        credentials['ACCESS_KEY'] = os.environ['AWS_ACCESS_KEY']
        credentials['SECRET_KEY'] = os.environ['AWS_SECRET_ACCESS_KEY']
        credentials['LOCALE'] = "us"
        return credentials