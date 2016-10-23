from GoogleVision import *
import pysftp as sftp
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
from bs4 import BeautifulSoup
import random
import re, string
import scipy
from extraction import TopicExtractor

class Google(object):

    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
    google_url = "http://www.google.com/searchbyimage?image_url="

    def __init__(self):
        self.pattern = re.compile('([^\s\w]|_)+')

    
    def GetTokens(self, imageUrl):
        result = {'tokens' : [],
                    'tags' : []}
        
        result['tokens'] = self.SearchImage(imageUrl)
        result['tags'] = self.GetLabels(imageUrl)

        return result



    def GetLabels(self, imageUrl):
        return get_photo_description(imageUrl)


    def SearchImage(self, imageUrl):

        path = Google.google_url + imageUrl
        #print(path)
        sourceCode = Google.opener.open(path).read()
        soup = BeautifulSoup(sourceCode)
        remember = soup.select('.g > .rc > .r > a')
        remember += soup.select('span.st')

        emphases = soup.select('em')
        
        tokens = [item.text for item in emphases]
        print(tokens)

        corpus = []

        for elem in remember:
            corpus.append(self.pattern.sub('', elem.text).lower())

        #print(corpus)
        #words = TopicExtractor.Extract(corpus)[:3]

        return tokens[0]
