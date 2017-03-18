from model.integration.google.GoogleVision import *
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
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.17')]
    google_url = "http://www.google.com/searchbyimage?image_url="
    #google_url="http://www.google.com/"

    def __init__(self):
        self.pattern = re.compile('([^\s\w]|_)+')

    
    def GetTokens(self, encodedImage):
        result = {'tokens' : [],
                    'tags' : []}
        
        result['tokens'] = self.SearchImage(encodedImage)
        result['tags'] = self.GetLabels(encodedImage)
        print("Result token:" + result['tokens'])
        print("Result tags: " + result['tags'])
        
        return result



    def GetLabels(self, encodedImage):
        return get_photo_description(encodedImage)


    def SearchImage(self, encodedImage):

        path = Google.google_url + encodedImage

        sourceCode = Google.opener.open(path).read()
        soup = BeautifulSoup(sourceCode)
        remember = soup.select('.g > .rc > .r > a')
        remember += soup.select('span.st')

        emphases = soup.select('em')
        
        tokens = [item.text for item in emphases]
        print("TOKENS: ")
        print(tokens)

        corpus = []

        for elem in remember:
            corpus.append(self.pattern.sub('', elem.text).lower())

        #print(corpus)
        #words = TopicExtractor.Extract(corpus)[:3]
        
        
        return tokens[0]
