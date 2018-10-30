#imports
import requests
import json
from time import strftime
from datetime import datetime

meeting_guid = 'PUT_YOUR_MEETING_GUID_HERE'
c_r = 'cobalt_contact_cobalt_meetingregistrations' # Contact relationship string shorthand
m_r = 'cobalt_Meeting_Cobalt_MeetingRegistrations' # Meeting relationship string shorthand

# make request for meeting
url = config.ramco_api_url
payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntity',
    'Entity':'Cobalt_Meeting',
    'Attributes':f'cobalt_name,cobalt_BeginDate,{m_r}/cobalt_meetingregistrationId',
    'GUID':meeting_guid
    } 
api_reply = requests.post(url,payload).json()
data = api_reply['Data']

# iterate through 'data' for meeting details
registrations = data['cobalt_Meeting_Cobalt_MeetingRegistrations']
meeting_name = data['cobalt_name']

# we'll convert the RAMCO 10-digit time string to a readable format with datetime and strftime
timestamp = data['cobalt_BeginDate']['Value']
date = datetime.fromtimestamp(int(timestamp)).strftime('%B %d, %Y')

# output meeting name and date to screen
print(meeting_name)
print(date)

# iterate through all registrations for the meeting and fetch Contact details
for k, guid in [(k, guid) for x in registrations for (k, guid) in x.items()]:
    
    # make request for each Contact
    payload2 = {
    'key':'MassARInternal-MassAR-Prod-bb4168fd6bf097c9433653bef6235bae8cfb2ca1',
    'Operation':'GetEntity',
    'Entity':'Cobalt_MeetingRegistration',
    'GUID':f'{guid}',
    'Attributes':f'{c_r}/ContactId,{c_r}/FirstName,{c_r}/LastName,{c_r}/MobilePhone,{c_r}/EMailAddress1,{c_r}/ramco_nrdsid,{c_r}/ramco_primaryassociationid',
    'Expand':'cobalt_contact_cobalt_meetingregistrations'
    }
    api_reply2 = requests.post(url,payload2).json()
    attendee_details = api_reply2['Data']
    
    # iterate through 'data' for Contact details
    contact_id = attendee_details[f'{c_r}']['ContactId'] # not shown below in 'print'
    first = attendee_details[f'{c_r}']['FirstName']
    last = attendee_details[f'{c_r}']['LastName']
    assoc = attendee_details[f'{c_r}']['ramco_primaryassociationid']['Display']
    cell = attendee_details[f'{c_r}']['MobilePhone']
    email = attendee_details[f'{c_r}']['EMailAddress1']
    nrds = attendee_details[f'{c_r}']['ramco_nrdsid']
    
    # print each Contact's details to screen
    print(first,last,assoc,cell,email,nrds)