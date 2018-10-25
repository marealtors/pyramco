# pyramco
a collection of python methods and functions for use with the RAMCO API

all require the 'requests' module be installed in python http://docs.python-requests.org/en/master/ 

all require config.py in the script folder, and the API key/url defined there as: 

ramco_api_key = 'your_ramco_api_key_goes_here'
ramco_api_url = 'https://api.ramcoams.com/api/v2/'


conn_test.py
Does your API Key work? Tests connectivity by querying for the metadata on the 'cobalt_answer' entity, since it's small and not often customized. Looks at the 'ResponseCode' contained in the jsonified reply from the server and returns either 'ok' or 'error' depending on if it gets '200' (which means OK) or any other response code in that reply
