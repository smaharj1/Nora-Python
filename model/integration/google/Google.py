from GoogleVision import *
import pysftp as sftp
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time

class Google(object):

    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
    
    def __init__(self):
        pass