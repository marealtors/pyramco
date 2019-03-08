import requests
import config
import json
import pyramco

# set or import your meeting GUID
guid = 'PUT_YOUR_MEETING_GUID_HERE'

# make request for meeting and the committee set to it, if any
reply = pyramco.get_entity('Cobalt_Meeting', guid, ('ramco_Committee'))
if ['Data']['ramco_Committee']:
	committee_guid = reply['Data']['ramco_Committee']['Value']
	# make request for committee memberships and their related contacts for the committee
	reply2 = pyramco.get_entities('cobalt_committeemembership', ('cobalt_ContactId,statuscode'), filters=f'cobalt_CommitteeId<eq>{committee_guid} AND statuscode<eq>533470000')
	contacts = reply2['Data']

	for guids in contacts:
		contact_guid = guids['cobalt_ContactId']['Value']
		# create a meeting registration for each contact
		reply3 = pyramco.create_entity('cobalt_meetingregistration',(f'cobalt_meetingid={meeting_guid},cobalt_contactid={contact_guid}'))
		# acknowledge it worked
		return ('meeting registrations added successfully', 204)

# or acknowledge it didn't work
else:
	return ('no committee associated with that meeting', 404)
