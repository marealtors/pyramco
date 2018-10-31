# update a member email address in MailChimp

from mailchimp3 import MailChimp
import requests
import json
import hashlib
import config

# define your mailchimp api connection params
client = MailChimp(mc_api = config.mc_api_key, mc_user='null')

# define the type of request and parameters
payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntity',
    'Entity':'Contact',
    'GUID':f'{guid}',
    'Attributes':'EMailAddress1,ramcosub_mailchimp_sync_email'} # this is a custom field
response = requests.post(config.ramco_api_url,payload)
api_reply = response.json()['Data']

# requires a workflow affecting these 2 fields to function properly
new_email = api_reply['EMailAddress1']
old_email = api_reply['ramcosub_mailchimp_sync_email']

# convert the old email to lowercase
lowercase_email = old_email.lower()

# md5 hash it for mailchimp - their "user id" for the member is this value
hashed = (hashlib.md5(lowercase_email.encode('utf-8')).hexdigest())

# make the request to the mailchimp api
client.lists.members.update(list_id = config.mc_list_id, subscriber_hash = hashed, data= {'email_address':new_email})