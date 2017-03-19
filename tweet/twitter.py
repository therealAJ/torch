from tweepy import API
from tweepy import OAuthHandler
import requests
import os

ckey = 'tC8oIP1dzUVB0j54V2RPmgkim'
csecret = 'oH6os7iZBJKeJm4k8BED6z9vLRthc8ne82qUZTHgRKe6KAr9Vj'
atoken = '843351930999001088-IvK8bbBP3yONpMBOJXMJIWJ1B99OEuF'
asecret = '0gPmC4qKGJgMsM82wJGSirUOoVcppm9CyqoppdVssOI0g'



def twitter_api():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = API(auth)
    return api

def capture_and_tweet():
    view_description = "This Description"
    filepath = 'car.png';
    tweet_image(url, view_description, filepath)
    print("Sick tweet")

def tweet_image(url, message, filepath):
    api = twitter_api()
    filename = filepath
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
                api.update_with_media(filename, status=message)
                os.remove(filename)
            else:
                print("Unable to download image")

url ="http://pngimg.com/uploads/mercedes/mercedes_PNG1898.png"
capture_and_tweet()
