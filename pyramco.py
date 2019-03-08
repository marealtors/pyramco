import json
import requests
import config

# a partial wrapper class for simplifying RAMCO API calls in Python 3.6+
# returns jsonified but otherwise untouched responses

#### base functions

### clear_cache
# no arguments are accepted. clears the server-side metadata cache. 204 is the expected return code.
def clear_cache():
    payload = {
        'key': ramco_api_key,
        'Operation':'ClearCache'
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

### get_entity_types
# no arguments are accepted. fetches all entities in the system.
def get_entity_types():
    payload = {
        'key': ramco_api_key,
        'Operation':'GetEntityTypes'
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

### get_entity_metadata
# accepts a valid entity name enclosed in apostrophes, like: 'Contact'. returns all metadata on that entity.
def get_entity_metadata(entity):
    payload = {
        'key': ramco_api_key,
        'Operation':'GetEntityMetadata',
        'Entity': entity
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

### get_entity
# accepts a valid entity name, GUID, and a tuple of comma-separated attribute names, returns attribute values for the specified contact matching the GUID
def get_entity(entity, guid, *attributes):
    payload = {
        'key': ramco_api_key,
        'Operation':'GetEntity',
        'Entity': entity,
        'GUID': guid,
        'Attributes': attributes
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

### get_entities
# accepts a valid entity name, a tuple of comma-separated attribute names, and (optionally) a valid filters string, a string delimiter character, and an integer value for the max results.
def get_entities(entity, *attributes, filters='', string_delimiter='', max_results=''):
    payload = {
        'key': ramco_api_key,
        'Operation':'GetEntities',
        'Entity': entity,
        'Filter': filters,
        'Attributes': attributes,
        'StringDelimiter': string_delimiter,
        'MaxResults': max_results
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

### resume_streamtoken
# accepts a valid streamtoken string and resumes the get_entities request that generated it.
def resume_streamtoken(streamtoken):
    payload = {
        'key': ramco_api_key,
        'Operation':'GetEntities',
        'StreamToken': streamtoken
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

### create_entity
# accepts a valid entity name, a tuple of comma separated attribute=value pairs, and optionally a string delimiter character
def create_entity(entity, *attributes, string_delimiter=''):
    payload = {
        'key': ramco_api_key,
        'Operation':'CreateEntity',
        'Entity': entity,
        'Attributes': attributes,
        'StringDelimiter': string_delimiter
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

### delete_entity
# accepts a guid and deletes the corresponding record
def delete_entity(entity, guid):
    payload = {
        'key': ramco_api_key,
        'Operation':'DeleteEntity',
        'Entity': entity,
        'GUID': guid
        }
    reply = requests.post(ramco_api_url,payload).json()
    return(reply)

#### additional functions

### fetch_profile
# fetches common member info to populate a "profile" page, accepts a Contact GUID

def fetch_profile(guid):
    profile_data = get_entity('Contact', guid,'ContactId,\
address1_city,\
cobalt_password,\
cobalt_username,\
Contact_Annotation/FileName,\
Contact_Annotation/DocumentBody,\
donotbulkemail,\
donotemail,\
emailaddress1,\
firstname,\
lastname,\
mobilephone,\
parentcustomerid,\
ramco_lastcoedate,\
ramco_nrdsid,\
ramco_nrdsmembertype,\
ramco_nrdsprimaryassociation,\
ramco_primaryassociationid')
    committees = get_entities('cobalt_committeemembership','cobalt_CommitteePositionId,cobalt_committeemembershipid',filters=f'statuscode<eq>533470000 AND cobalt_ContactId<eq>{guid}')
    return(profile_data,committees)
