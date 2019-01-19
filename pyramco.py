import json
import requests
import config

# a partial wrapper class for simplifying RAMCO API calls in Python 3.6+
# returns jsonified but otherwise untouched responses


# no arguments are accepted. clears the server-side metadata cache. 204 is the expected return code.
def clear_cache():
    payload = {
        'key': config.ramco_api_key,
        'Operation':'ClearCache'
        }
    reply = requests.post(config.ramco_api_url,payload).json()
    return(reply)


# no arguments are accepted. fetches all entities in the system.
def get_entity_types():
    payload = {
        'key': config.ramco_api_key,
        'Operation':'GetEntityTypes'
        }
    reply = requests.post(config.ramco_api_url,payload).json()
    return(reply)


# accepts a valid entity name enclosed in apostrophes, like: 'Contact'. returns all metadata on that entity.
def get_entity_metadata(entity):
    payload = {
        'key': config.ramco_api_key,
        'Operation':'GetEntityMetadata',
        'Entity': entity
        }
    reply = requests.post(config.ramco_api_url,payload).json()
    return(reply)


# accepts a valid entity name, GUID, and a tuple of comma-separated attribute names, returns attribute values for the specified contact matching the GUID
def get_entity(entity, guid, *attributes):
    payload = {
        'key': config.ramco_api_key,
        'Operation':'GetEntity',
        'Entity': entity,
        'GUID': guid,
        'Attributes': attributes
        }
    reply = requests.post(config.ramco_api_url,payload).json()
    return(reply)


# accepts a valid entity name, a tuple of comma-separated attribute names, and (optionally) a valid filters string, a string delimiter character, and an integer value for the max results.  
def get_entities(entity, *attributes, filters='', string_delimiter='', max_results=''):
    payload = {
        'key': config.ramco_api_key,
        'Operation':'GetEntities',
        'Entity': entity,
        'Filter': filters,
        'Attributes': attributes,
        'StringDelimiter': string_delimiter,
        'MaxResults': max_results
        }
    reply = requests.post(config.ramco_api_url,payload).json()
    return(reply)


# accepts a valid streamtoken string and resumes the get_entities request that generated it.
def resume_streamtoken(streamtoken):
    payload = {
        'key': config.ramco_api_key,
        'Operation':'GetEntities',
        'StreamToken': streamtoken
        }
    reply = requests.post(config.ramco_api_url,payload).json()
    return(reply)
