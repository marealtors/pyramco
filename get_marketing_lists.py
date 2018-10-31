# get all your active Marketing Lists from RAMCO

from pprint import pprint
import requests
import json
import config

payload = {
    'key':config.ramco_api_key,
    'Operation':'GetEntities',
    'Entity':'list',
    'Attributes':'ListId,ListName,Type', # 'Type' returns false for Static, true for Dynamic
    'Filter':'StatusCode<eq>0' # 0 is the value for active
    }
response = requests.post(config.ramco_api_url,payload)
raw = response.json()
pprint(raw)