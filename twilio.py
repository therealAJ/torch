from twilio.rest import TwilioRestClient 
import re


phoneBook = {
    'ali' : '+14038708575',
    'dad' : '+17789879001',
    'brad' : '+14038771681' 
}

def sendTextMessage(messageBody , person , url):
	# put your own credentials here 
	ACCOUNT_SID = "AC8fe5a90a3b11f2cf374c968c64f9321e" 
	AUTH_TOKEN = "e0ac0d725fa05b89cebb961c4ec0bad0" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	
	if re.match(r'https?://.*\..*' , url):
		client.messages.create(
		    to=phoneBook[person.lower()], 
		    from_="+15873175980", 
		    body= messageBody,
			media_url = url
		)
	else:
		client.messages.create(
		    to=phoneBook[person.lower()], 
		    from_="+15873175980", 
		    body= messageBody
		)