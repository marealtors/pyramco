# pyramco

A collection of python methods and functions for use with the RAMCO API from MAR

More info abnout the API at: https://api.ramcoams.com/api/v2/ramco_api_v2_doc.pdf

- all require the 'requests' module be installed in python http://docs.python-requests.org/en/master/ 
- all require Python 3.6+, mostly because of f-strings, adjust as needed
- most require json and pprint modules to be imported
- we demonstrate a couple methods of calling the API and parsing returns, see the syntax near 'payload ='  and 'requests.post'
- all require config.py in the script folder, and the API key/url defined there as shown below; you can define any constants you want here.
```
ramco_api_key = 'your_ramco_api_key_goes_here'
ramco_api_url = 'https://api.ramcoams.com/api/v2/'
```
I recommend https://www.pythonanywhere.com/ as a good testing environment to work with these scripts and experiment.

We'll add new functions to this as they're available. 

## Functions: 

### conn_test.py
Does your API Key work? Tests connectivity by querying for the metadata on the 'cobalt_answer' entity, since it's small and not often customized. Looks at the 'ResponseCode' contained in the jsonified reply from the server and returns either 'ok' or 'error' depending on if it gets '200' (which means OK) or any other response code in that reply.

### field_exist.py
Does { some field } exist? Tests for the existence of a given field, to use with custom fields or for testing.

### field_type.py
What field type is { some field } and does it exist? Tests for the type AND existence of a given custom field, requirements same as previous script

### multi_search.py
A multi-search input box that finds contacts by matching a name, email, or NRDS ID, or any string contained in one

### get_name.py
Returns the 'FullName' RAMCO Contact field for the Contact record matching "guid_var" and prints it to screen

### get_metadata.py
Returns the full metadata for the specified entity in JSON format. Can be a LOT of data, like in this example for Contact.

### test_mysql.py
Tests your mysql connection to verify you're able to connect to a specific host/db/table by returning a list of tables in the specified db. Requires mysql-connector - https://pypi.org/project/mysql-connector/

### fetch_meeting_attendees.py
An example of a more complex iterative function that first calls the API to fetch some details about a specified meeting, then uses part of those results (meeting registration ids) to call the API again for each registered attendee and fetch additional details. This example could be used for a simple (or even an interactive) roster.
