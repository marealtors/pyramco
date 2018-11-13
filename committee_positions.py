# imports
import config
import requests
import json
from pprint import pprint

committee_membership_guid = 'put_a_valid_committee_membership_guid_here'

# make request to get details of the committee membership and contact 
payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntity',
    'Entity':'cobalt_committeemembership',
    'Attributes':'cobalt_CommitteeMembershipId,cobalt_contact_cobalt_committeemembership/ContactId,cobalt_contact_cobalt_committeemembership/ramcosub_committee_positions,cobalt_CommitteePositionId,cobalt_CommitteeId',
    'GUID':f'{committee_membership_guid}'
    }
api_reply = requests.post(config.ramco_api_url,payload).json()
data = api_reply['Data']

# set some values from 'Data'
old_positions = data['cobalt_contact_cobalt_committeemembership']['ramcosub_committee_positions']
committee = data['cobalt_CommitteeId']['Display']
position = data['cobalt_CommitteePositionId']['Display']
contact_id = data['cobalt_contact_cobalt_committeemembership']['ContactId']

# evaluate the contents of the current committee positions field and decide how to update it
if old_positions == None:
    revised = f'{position}: {committee}'
elif len(old_positions) < 3:
    revised = f'{position}: {committee}'
else:
    revised = f'{old_positions}, {position}: {committee}'

# make another request to update the field
payload2 = {
    'key':config.ramco_api_key,
    'Operation':'UpdateEntity',
    'Entity':'Contact',
    'AttributeValues':f'ramcosub_committee_positions=#{revised}#',
    'GUID':f'{contact_id}'
    }
api_reply2 = requests.post(config.ramco_api_url,payload2).json()