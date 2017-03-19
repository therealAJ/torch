from flask import Flask
from flask_ask import Ask, statement, question, session
import subprocess as sp
import calendar, time, json
from analysis import vision
from read import read
from pprint import pprint

from tweepy import API
from tweepy import OAuthHandler
import requests
import os
import urlparse, urllib
from twitter import tweet_image
from twil import *

app = Flask(__name__)
ask = Ask(app, '/torch')

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
    return statement("Sick Tweet, Daredevil")


@ask.intent("Text")
def send_text(person):
    session.attributes['person'] = person
    return question("I am sending a message to "+ person + ". What should I send?")


@ask.intent("MessageIs")
def send_msg(msg):
    print "in message is"
    print session.attributes['person']
    print msg
    sendTextMessage(msg, session.attributes['person'], '')
    return statement("sent the message for you!")



@ask.intent("Read")
def read_and_describe():
    filepath = take_picture()
    text_description = read(filepath)
    # text_description = "I read: " + text_description + "from the image you sent me."
    return statement(text_description)


def get_description(data):
    python_obj = json.loads(data)
    pprint(python_obj)
    return python_obj['description']['captions'][0]['text']


if __name__ == '__main__':
    app.run(debug=True)
