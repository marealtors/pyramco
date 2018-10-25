import json
import requests

# 'guid_var' is the guid of the contact record you're looking for
guid_var = 'CONTACT_GUID_GOES_HERE'

# make request
url = config.ramco_api_url
payload = {
    'key': config.ramco_api_key,
    'Operation':'GetEntity',
    'Entity':'contact',
    'GUID':f'{guid_var}', # this inserts the GUID
    'Attributes':'FullName'
    } 
name = requests.post(url,payload).json()

# print results
print(name)