import requests
import json
import config
import phonenumbers
from twilio.rest import Client

# the GUID of the list, must be Static type
list_id = 'YOUR_LIST_GUID_HERE'

# set your SMS message text
message_body = 'Your message text goes here.'

# fetch all contacts on your list and their mobile number field
payload = {
'key':config.ramco_api_key,
'Operation':'GetEntity',
'Entity':'list',
'GUID':f'{list_id}',
'Attributes':'Type,ListName,MemberCount,listcontact_association/ContactId,listcontact_association/MobilePhone'
}
reply = requests.post(config.ramco_api_url,payload).json()
contacts = reply['Data']['listcontact_association']

# set blank dict to hold numbers
numbers = []

# iterate over your contacts to extract their mobile number to your list, if one exists
for number in contacts:
    # checks that a mobile number exists on this contact
    if number['MobilePhone']:
        mobile = number['MobilePhone']
        numbers.append(mobile)

for raw_number in numbers:
    # parses it to the E164 format twilio needs
    parsed_number = phonenumbers.parse(raw_number, 'US')
    clean_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

    # Add your Account SID and Auth Token from twilio.com/console to config.py
    client = Client(config.twilio_account_sid, config.twilio_auth_token)

    # compose or pass your message text to 'body'
    message = client.messages.create(
        body = message_body,
        from_= config.twilio_number,
        to = clean_number
        )

    # returns the twilio SID for this message
    print(message.sid)