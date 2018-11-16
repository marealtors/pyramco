# fetch all contacts with pending committee memberships,
# overwrite the custom Contact field 'ramcosub_committee_positions' with the values from each of those memberships

import config
import requests
import json

# make request to get all pending committee memberships
payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntities',
    'Entity':'cobalt_committeemembership',
    'Attributes':'cobalt_contact_cobalt_committeemembership/ContactId,cobalt_CommitteePositionId,cobalt_CommitteeId',
    'Filter':'statuscode<eq>1' # '1' is 'pending' in our system, check your value in RAMCO if you want 'current'
    }
reply = requests.post(config.ramco_api_url,payload).json()

# for each membership you fetched, combine the member's position and committee name plus the Contact's guid
for each in reply['Data']:
    committee = each['cobalt_CommitteeId']['Display']
    position = each['cobalt_CommitteePositionId']['Display']
    contact_id = each['cobalt_contact_cobalt_committeemembership']['ContactId']

    # make the request to get contact info
    payload2 = {
        'key':config.ramco_api_key,
        'Operation':'GetEntity',
        'Entity':'Contact',
        'GUID':f'{contact_id}',
        'Attributes':'ramcosub_committee_positions'
        }
    reply2 = requests.post(config.ramco_api_url,payload2).json()
    
    # evaluate the contents of the committee positions field and decide how to update it
    # prior to this you should reset all committee position fields that contain data to 'x' via advanced find    
    
    # if it's null, write 'x' to your variable
    if reply2['Data']['ramcosub_committee_positions'] == None:
        old_positions = 'x'
    # if not, write the value to your variable
	else:    
        old_positions = reply2['Data']['ramcosub_committee_positions']
    
    # if it's 'x', clear it and insert the first position for this member
    if old_positions.startswith('x'):
        revised = f'{position}: {committee}'
    # if it's something else (another position has been written), concatenate them
    else:
        revised_position = f'{old_positions}, {position} - {committee}'
    
    # display the change for testing
    print(revised_position)

    # make request to update the field
    payload3 = {
        'key':config.ramco_api_key,
        'Operation':'UpdateEntity',
        'Entity':'Contact',
        'AttributeValues':f'ramcosub_committee_positions=#{revised_position}#',
        'Guid':f'{contact_id}'
        }
    api_reply3 = requests.post(config.ramco_api_url,payload3).json()
    
    # the reply it prints if successful should be: {'ResponseCode': 204, 'ResponseText': 'OK - No Data'}
    print(api_reply3)
