import requests
import json
import config
import phonenumbers
from twilio.rest import Client
from pprint import pprint

# specify a Contact GUID or pass one to 'guid_var' from a function
guid_var = 'YOUR_GUID_GOES_HERE'

payload = {
	'key': config.ramco_api_key,
	'Operation':'GetEntity',
	'Entity':'Contact',
	'GUID':f'{guid_var}',
	'Attributes':'mobilephone'
	}
# fetch the Contact's mobile number from API
raw_number = requests.post(config.ramco_api_url,payload).json()['Data']['MobilePhone']

# parse it to the E164 format twilio needs
parsed_number = phonenumbers.parse(raw_number, 'US')
number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

# make the twilio API request
client = Client(config.twilio_account_sid, config.twilio_auth_token)

# compose or pass your message text to 'body'
message = client.messages.create(
    body = 'Test text for SMS goes here',
    from_= config.twilio_number,
    to = number
    )

# return the twilio SID for this message
print(message.sid)
