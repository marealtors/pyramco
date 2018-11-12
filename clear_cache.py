# imports
import config
import requests
import json

# make request
payload = {
    'key':config.ramco_api_key,
    'Operation':'clearCache'
    } 
api_reply = requests.post(config.ramco_api_url,payload).json()
print(api_reply)