from flask import Flask
from flask_ask import Ask, statement, question, session
import subprocess as sp
import calendar, time, json
from analysis import vision

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
    view_description = "Insert the description received from the API here."
    print("youre on a roll")
    filepath = take_picture()
    data = send_picture(filepath)
    view_description = get_description(data)
    return statement(view_description)

def take_picture():
    filepath =  str(calendar.timegm(time.gmtime()))+ '.jpg'
    print filepath
    sp.call(['fswebcam' , filepath ])
    return filepath

def send_picture(filepath):
    return vision(filepath)

def get_description(data):
    python_obj = json.loads(data)
    return python_obj.description.captions[0].text


if __name__ == '__main__':
    app.run(debug=True)
