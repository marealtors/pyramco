import json
import requests
from pprint import pprint

url = config.ramco_api_url
payload = {
    'key': config.ramco_api_key,
    'Operation':'GetEntityMetadata',
    'Entity':'contact'
    } 
metadata = requests.post(url,payload).json()
pprint(metadata)
