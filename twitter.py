from tweepy import API
from tweepy import OAuthHandler
import requests
import os
import urlparse, urllib

ckey = 'tC8oIP1dzUVB0j54V2RPmgkim'
csecret = 'oH6os7iZBJKeJm4k8BED6z9vLRthc8ne82qUZTHgRKe6KAr9Vj'
atoken = '843351930999001088-IvK8bbBP3yONpMBOJXMJIWJ1B99OEuF'
asecret = '0gPmC4qKGJgMsM82wJGSirUOoVcppm9CyqoppdVssOI0g'

def twitter_api():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = API(auth)
    return api

def tweet_image(message, filepath):
    api = twitter_api()
    media = api.media_upload(filepath)
    api.update_status(status=message, media_ids=[media.media_id])
