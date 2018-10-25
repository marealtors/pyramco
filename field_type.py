import config
import requests

# ramco api query fields
key = config.ramco_api_key
operation = 'GetEntityMetadata'
entity = 'Contact' # set this to the appropriate entity your field lives on
url = config.ramco_api_url
field = 'YOUR_FIELD_HERE' # field you want to verify exists and find type for

# make ramco api request
payload = {'key':key,'Operation':operation,'Entity':entity}
reply = requests.post(url,payload).json()

if field in reply['Data']['Attributes']: # looks for your fieldname as a key in the iterable
    status = 'ok'
    type = reply['Data']['Attributes'][field]['Type'] 
    print(field+' exists')
    print('type: '+type)
else:
    status = 'error'
    type = 'error'
    print(status+' '+field+' does not exist')
    print('type: '+type)