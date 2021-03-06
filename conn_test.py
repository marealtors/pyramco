# Does your API Key work?
# requires the 'requests' module be installed in python http://docs.python-requests.org/en/master/ requires config.py in path and the API key defined in it as: ramco_api_key = 'your_ramco_api_key_goes_here', and the RAMCO API url defined as: ramco_api_url = 'https://api.ramcoams.com/api/v2/'

# Tests connectivity by querying for the metadata on the 'cobalt_answer' entity, since it's small and not often customized. Looks at the 'ResponseCode' contained in the jsonified reply from the server and returns either 'ok' or 'error' depending on if it gets '200' (which means OK) or any other response code in that reply.

# imports
import config
import requests

# ramco api query fields
key = config.ramco_api_key
operation = 'GetEntityMetadata'
entity = 'cobalt_answer'
url = config.ramco_api_url

# prints the info for verification
print('Your API URL is set to: '+url)
print('Your API key is set to: '+key)

# make ramco api request
payload = {'key':key,'Operation':operation,'Entity':entity}
reply = requests.post(url,payload).json()

# if it works, say OK, otherwise print the error returned
if reply['ResponseCode'] == 200:
    status = 'ok'
    print('Your status is: '+status)
else:
    status = 'error'
    print('Your status is: '+status)