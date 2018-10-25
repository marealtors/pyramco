# pyramco

a collection of python methods and functions for use with the RAMCO API - more info at: https://api.ramcoams.com/api/v2/ramco_api_v2_doc.pdf

-all require the 'requests' module be installed in python http://docs.python-requests.org/en/master/ 

-all require config.py in the script folder, and the API key/url defined there as: 

ramco_api_key = 'your_ramco_api_key_goes_here'
ramco_api_url = 'https://api.ramcoams.com/api/v2/'


Functions: 

# conn_test.py
Does your API Key work? Tests connectivity by querying for the metadata on the 'cobalt_answer' entity, since it's small and not often customized. Looks at the 'ResponseCode' contained in the jsonified reply from the server and returns either 'ok' or 'error' depending on if it gets '200' (which means OK) or any other response code in that reply.

# field_exist.py
Does { some field } exist? Tests for the existence of a given field, to use with custom fields or for testing.

# field_type.py
What field type is { some field } and does it exist? Tests for the type AND existence of a given custom field, requirements same as previous script

# multi_search.py
A multi-search input box that finds contacts by matching a name, email, or NRDS ID, or any string contained in one

# get_name.py
Returns the 'FullName' RAMCO Contact field for the Contact record matching "guid_var" and prints it to screen
