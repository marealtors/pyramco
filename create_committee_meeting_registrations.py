import requests
import config
import json

# set or import your meeting GUID
meeting_guid = 'PUT_YOUR_MEETING_GUID_HERE'

# make request for meeting's associated committee
payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntity',
    'Entity':'Cobalt_Meeting',
    'Attributes':'ramco_Committee',
    'GUID':meeting_guid
    } 
api_reply = requests.post(config.ramco_api_url,payload).json()

# get the guid of the associated committee
committee_guid = api_reply['Data']['ramco_Committee']['Value']

# make a request for that meeting's associated committee's members contact records
payload2 = {
    'key':config.ramco_api_key,
    'Operation':'GetEntities',
    'Entity':'cobalt_committeemembership',
    'Attributes':'cobalt_ContactId,statuscode',
    'Filter':f'cobalt_CommitteeId<eq>{committee_guid} AND statuscode<eq>533470000' #only fetch current members
    } 
api_reply2 = requests.post(config.ramco_api_url,payload2).json()

# get your contact info as an iterable
contacts = api_reply2['Data']

# for each contact returned, create a new meeting registration for the meeting
for guids in contacts:
    contact_guid = guids['cobalt_ContactId']['Value']
    payload3 = {
    'key':config.ramco_api_key,
    'Operation':'CreateEntity',
    'Entity':'cobalt_meetingregistration',
    'AttributeValues':f'cobalt_meetingid={meeting_guid},cobalt_contactid={contact_guid}'
    }
    api_reply3 = requests.post(config.ramco_api_url,payload3).json()