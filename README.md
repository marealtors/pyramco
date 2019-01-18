# pyramco

A collection of Python methods and functions for use with the RAMCO API 

AND NOW:

A new API wrapper module that defines some key functions and simplifies the process of calling them.  

More info about the API at: https://api.ramcoams.com/api/v2/ramco_api_v2_doc.pdf

- all require the `requests` module be installed in python http://docs.python-requests.org/en/master/ 
- all require Python 3.6+, mostly because of f-strings, adjust as needed
- most require `json` and `pprint` modules to be imported
- we demonstrate a couple different methods of calling the API, structuring requests, and parsing returns; see the syntax near `payload =`  and `requests.post` for examples/variations
- all scripts require a proper `config.py` file in the script directory and to be imported via `import config`. The API key/url should be defined there as shown below; you can define any other constants you want there, as well.
```
ramco_api_key = 'your_ramco_api_key_goes_here'
ramco_api_url = 'https://api.ramcoams.com/api/v2/'
```
I recommend https://www.pythonanywhere.com/ as a good testing environment to work with these scripts and experiment.

## Wrapper Module:

### pyramco.py
You can now call several functions more easily by importing pyramco and calling the functions defined there. 

For instance, to perform a GetEntityMetadata request for Contacts and print the result, the function goes from:
```
payload = {
    'key': config.ramco_api_key,
    'Operation':'GetEntityMetadata',
    'Entity':'Contact'
    } 
metadata = requests.post(url,payload).json()
pprint(metadata)
```
to:

```
metadata = get_entity_metadata('Contact')
pprint(metadata)
```

See the script for details, updates to add all RAMCO API functionality coming soon. 

## Functions: 
We'll add new functions to this section as they're available. 

### conn_test.py
Does your API Key work? Tests connectivity by querying for the metadata on the `cobalt_answer` entity, since it's small and not often customized. Looks at the `ResponseCode` contained in the jsonified reply from the server and returns either `ok` or `error` depending on if it gets `'200'` (which means OK) or any other response code in that reply.

### clear_cache.py
Simple operation to clear and rebuild the API cache so you can access fields you've just created via the API - use if you recently made a new field and you're getting a `400 invalid attribute` error and you know your fieldnames are correct.

### field_exist.py
Does `some field` exist? Tests for the existence of a given field, to use with custom fields or for testing.

### field_type.py
What field type is `some field` and does it exist? Tests for the type AND existence of a given custom field.

### multi_search.py
A simple multi-search input/output that finds contacts by matching a name, email, or NRDS ID entered by the user, or any partial match.

### get_name.py
Returns the `FullName` RAMCO Contact field for the Contact record matching the Contact GUID provided, and prints it to screen.

### get_metadata.py
Returns the full metadata for the specified entity in JSON format. Can be a LOT of data, as in this example for `Contact`.

### test_mysql.py
For use with an external MySQL database; tests your MySQL connection to verify you're able to connect to a specific host/database by returning a list of tables in the specified database. Can be used as the basis of more complex data connections. Requires `mysql-connector` - https://pypi.org/project/mysql-connector/

### fetch_meeting_attendees.py
An example of a more complex iterative function that first calls the API to fetch some details about a specified meeting, then uses part of those results (meeting registration ids) to call the API again for each registered attendee and fetch additional details. This example could be used for a simple (or even an interactive) roster.

### get_contacts_from_marketing_list.py
Given a valid Marketing List GUID, returns GUIDS and email addresses for the Contacts associated with the list.

### get_marketing_lists.py
Fetches all your active Marketing Lists from RAMCO. Marketing Lists use some vague attributes; `Type` returns `false` for Static lists, and `true` for Dynamic lists. The StatusCode for Lists is 0 for Active and 1 for inactive, and doesn't contain descriptive `Display` text like most entities do.


## Functions in progress / Requiring custom code

### create_committee_meeting_registrations.py
A function which takes a Meeting GUID as input, looks to see if a Committee has been added on the meeting record; and if so, fetches all the current members of that committee and creates Meeting Registrations for them on that meeting. *--still needs work to ensure existence of an associated committee on a meeting and to skip repeat registrations--*

### committee_positions.py
Populates a custom text field on Contact records with the Positions and Committee names of all the Contact's details; for example, the field might read: *Chair - Government Affairs Committee, Member - RPAC Committee* or just: *Member - Board of Directors*. This is used in our system for a custom merge field for emails to tell a member all the positions they have been appointed to. Also makes for a good summary of a member's current volunteer positions on the Contact form. Requires a custom text field on Contacts called `ramcosub_committee_positions`. The script is designed to preserve existing values and append to them, so you should remove all values in the field for all Contacts before use. (It overwrites `None` type values or values under 3 characters, so replace every value with an 'x', since it's not possible to set them to a null value in bulk.) This script is for a single membership, but you could pipe a list of Committee Memberships to it in a `FOR` loop easily. This version could be used to keep the field up to date throughout the year and run only when new Committee Members are added, for instance.

### committee_positions_bulk.py
As above, but will write for all Contacts having committee positions as defined in the first API call by filters. Make sure you use appropriate filters or you'll write every position they've ever had to every member who's ever held one. "Current" or "Pending" status would be the obvious choice here, plus some `<ne>` filters to remove committees you don't want to include.

### send_twilio_sms.py
Fetches a single Contact's mobile phone number from RAMCO (if present) and sends a text/SMS messsage with the specified text to it via the Twilio API. Requires a Twilio account, phone number, and for the SID, Account Token, and Twilio number to be specified in the config file properly. See: https://www.twilio.com/docs/sms/quickstart/python Requires the twilio helper library and the `phonenumbers` library. https://pypi.org/project/phonenumbers/

### twilio_sms_to_marketing_list.py
Fetches the mobile numbers for Contacts associated with a specified Marketing List and sends them an SMS message using Twilio. Requirements as above, only works on Static marketing lists, so not suitable for long-term automations on marketing lists that might change over time. RAMCO doesn't store the contacts of a Dynamic Marketing list as individual relationships; it instead saves an XML object in the field `Query` on the `list` entity that contains the query CRM uses to fetch the Contacts at the time the list is fired. To text to Dynamic lists, you'd have to find a way to either push the query back into CRM and have it return a set of Contacts, or to parse the query in Python into something you could make an API call for those Contacts accuratley with. We'll see.

### mailchimp_update_member_email.py
Requires a LOT of additional configuration, more a proof of concept than a practical function (although we've had it running with no problems in production for 8 months):

- You'll need a MailChimp API key and the list ID of a list that contains all your members in your `config.py` file https://developer.mailchimp.com/documentation/mailchimp/ 
- A new text/email address field on Contacts must be created called `ramcosub_mailchimp_sync_email`
- Initially, and on creation of all new Contacts, the new field must be populated with the same value in `EmailAddress1`
- A workflow must be created on Contacts that is triggered when the `EmailAddress1` (regular email) field is modified; this workflow does the following:

  - Uses a third-party tool available at: https://kaskelasolutions.com to get the Contact's GUID as a value available to the Workflow
  - Checks the email is not blank
  - Uses a custom tool to make an external API request - in this case, the code in this function lives at that endpoint. RAMCO calls the MAR API, the MAR API in turn runs `mailchimp_update_member_email.py`
  - Waits one minute; this gives the function time to run
  - Copies the value in `EmailAddress1` to the new `ramcosub_mailchimp_sync_email` field

![alt text](https://github.com/marealtors/pyramco/blob/master/mailchimp.PNG?raw=true)

The purpose of all this is that MailChimp stores your members and refers to them by the MD5-hash of their email address, after converting it to all lowercase. In the one minute delay above, you're storing both the "old" and "new" email addresses for your member. The function fetches the "old" address, hashes it, finds the user in MailChimp using their API, and then having identified the user, changes the value to the "new" address. Then about a minute later, both fields in RAMCO will be the same. This way, if the user changes their email in the future, you can repeat the process. 
