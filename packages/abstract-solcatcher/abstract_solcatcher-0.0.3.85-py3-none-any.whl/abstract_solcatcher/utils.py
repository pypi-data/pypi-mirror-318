import json
from abstract_utilities import eatAll
from abstract_security import get_env_value
def getSolcatcherUrl(endpoint=None):
  return getEndpointUrl(endpoint=endpoint,url='https://solcatcher.io')
def getSolcatcherPairCatchUrl(endpoint=None):
  return getEndpointUrl(endpoint=endpoint,url='https://solcatcher.io/pairCatch')
def getSolcatcherTsUrl(endpoint=None):
  return getEndpointUrl(endpoint=endpoint,url='https://solcatcher.io/ts')
def getSolcatcherDbCalls(endpoint=None):
  return getEndpointUrl(endpoint=endpoint,url="https://solcatcher.io/dbCalls")
def get_db_header():
    # Retrieve the key from environment variable or config
    api_key = get_env_value('SOLCATCHER_DB_API_KEY')
    # Make sure the server sees this header as "X-API-KEY"
    return {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"  # if your endpoint expects JSON
    }
def post_request(endpoint, **kwargs):
    url = getSolcatcherDbCalls(endpoint=endpoint)
    response = requests.post(url=url, data=json.dumps(kwargs), headers=get_headers())
    return get_response(response)
def getEndpointUrl(endpoint=None,url=None):
  if endpoint:
    url = eatAll(url,['/'])
    endpoint = eatAll(endpoint,['/'])
    url= f"{url}/{endpoint}"
  return url
def try_json_dumps(data):
  if isinstance(data,dict):
    try:
      data = json.dumps(data)
    except:
      pass
    return data
def get_url(url=None):
    if isinstance(url,dict):
      url = url.get('url',url)
    return url
def getCallArgs(endpoint):
  return {'getMetaData': ['signature'], 'getPoolData': ['signature'], 'getTransactionData': ['signature'], 'getPoolInfo': ['signature'], 'getMarketInfo': ['signature'], 'getKeyInfo': ['signature'], 'getLpKeys': ['signature'], 'process': ['signature']}.get(get_endpoint(endpoint))
def ifListGetSection(listObj,section=0):
  if isinstance(listObj,list):
      if len(listObj)>section:
          return listObj[section]
  return listObj
def updateData(data,**kwargs):
  data.update(kwargs)
  return data
def get_method(method=None):
  return method or 'default_method'
def get_resp(response=None):
  response = response or {}
  if isinstance(response,dict):
    response = {"response":response}
  return response
def get_payload(*args,**kwargs):
    payload = args
    if args and kwargs:
        payload.append(kwargs)
    else:
        payload = kwargs
    return payload
