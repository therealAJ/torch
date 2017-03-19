from flask import Flask
from flask_ask import Ask, statement, question, session
import subprocess as sp
import calendar, time, json
from analysis import vision
import read
from pprint import pprint

from tweepy import API
from tweepy import OAuthHandler
import requests
import os
import urlparse, urllib

app = Flask(__name__)
ask = Ask(app, '/torch')


ckey = 'tC8oIP1dzUVB0j54V2RPmgkim'
csecret = 'oH6os7iZBJKeJm4k8BED6z9vLRthc8ne82qUZTHgRKe6KAr9Vj'
atoken = '843351930999001088-IvK8bbBP3yONpMBOJXMJIWJ1B99OEuF'
asecret = '0gPmC4qKGJgMsM82wJGSirUOoVcppm9CyqoppdVssOI0g'



@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, when you\'re ready, ask me to take a picture!'
    return statement(welcome_message)

@ask.intent("ViewDescription")
def describe_view():
    view_description = "In front of you there is: "
    print("youre on a roll")
    filepath = take_picture()
    data = send_picture(filepath)
    view_description = view_description + get_description(data)
    return statement(view_description)

def take_picture():
    filepath =  str(calendar.timegm(time.gmtime()))+ '.jpg'
    print filepath
    sp.call(['fswebcam' , filepath ])
    return filepath

def send_picture(filepath):
    return vision(filepath)

@ask.intent("Tweet")
def capture_and_tweet():
    filepath = take_picture()
    data = send_picture(filepath)
    view_description = get_description(data)
    tweet_image(view_description, filepath)
    print("Sick tweet")

@ask.intent("Read")
    filepath = take_picture()
    text_description = read(filepath)
    text_description = "I read: " + text_description + "from the image you sent me."
    return statement(text_description)

def tweet_image(message, filepath):
    api = twitter_api()
    media = api.media_upload(filepath)
    api.update_status(status=message, media_ids=[media.media_id])

def twitter_api():
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = API(auth)
    return api


def get_description(data):
    python_obj = json.loads(data)
    pprint(python_obj)
    return python_obj['description']['captions'][0]['text']


if __name__ == '__main__':
    app.run(debug=True)
