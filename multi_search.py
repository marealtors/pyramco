#a multi-search input box that finds contacts by matching a name, email, or nrds ID, or portion of one

import json
import requests
import config
from pprint import pprint

# creates the initial input prompt
input_string = input("Enter first, last, email or NRDS ID")

#ramco api request
url = config.ramco_api_url
payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntities',
    'Entity':'contact',
    'Attributes':'ContactId,FullName,ramco_nrdsid,ramco_nrdsprimaryassociation,Address1_City,Emailaddress1',
    'MaxResults':'10', # set this to the number you want to return
    'Filter':f'FullName<sc>#{input_string}# OR EMailAddress1<sc>#{input_string}# OR ramco_nrdsid<sc>#{input_string}#'
    }

matches = requests.post(url,payload).json()
pprint(matches)