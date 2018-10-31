# get all contacts and their emails from a Marketing List

from pprint import pprint
import requests
import json
import config

list_id = 'YOUR_LIST_GUID_HERE'

payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntity',
    'Entity':'list',
    'Attributes':'ListName,listcontact_association/ContactId,listcontact_association/EmailAddress1',
    'Guid':list_id
    }
response = requests.post(config.ramco_api_url,payload)
raw = response.json()
pprint(raw)