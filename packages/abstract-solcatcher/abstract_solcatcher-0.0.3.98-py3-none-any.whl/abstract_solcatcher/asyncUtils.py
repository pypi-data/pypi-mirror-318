import asyncio,httpx
from .utils import *
from abstract_apis import get_headers,get_response
async def make_request(url, payload, headers=None):
    final_headers = headers or get_headers()
    print("DEBUG: final headers ->", final_headers)
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(url, json=json.dumps(payload), headers=final_headers)
        response.raise_for_status()
        return await response.json()

def get_solcatcherSettings(getApi=False,**kwargs):
    solcatcherSettings = kwargs.get('solcatcherSettings')
    if solcatcherSettings:
        del kwargs['solcatcherSettings']
    headers = kwargs.get('headers')
    if 'headers' in kwargs:
        del kwargs['headers']
    headers = headers or {"Content-Type": "application/json"}
    apiKey = kwargs.get('solcatcherApiKey')
    if 'solcatcherApiKey' in kwargs:
        del kwargs['solcatcherApiKey']
    if apiKey or getApi:
        apiKey = apiKey or getApi
        if isinstance(apiKey,bool):
            apiKey=None
        headers = get_db_header(headers=headers,api_key=apiKey)
    headers = headers or get_headers()
    return kwargs,solcatcherSettings,headers
def runSolcatcherSettings(response,solcatcherSettings):
    usedKeys = []
    if solcatcherSettings:
        for key,value in solcatcherSettings.items():
            if key == 'getResponse':
                response = get_response(response)
                usedKeys.append(key)
            if key == 'getResult':
                result = response
                values = ['result',value] 
                if 'getResponse' not in usedKeys:
                    response = get_response(result)
                for value in values:
                    if result and isinstance(result,dict) and value in result:
                        result = result.get(value)
                response = result
                usedKeys.append(key)
    return response

async def async_call_solcatcher_ts(endpoint,*args,**kwargs):
    kwargs,solcatcherSettings,headers = get_solcatcherSettings(**kwargs)
    payload = get_payload(*args,**kwargs)
    url = getSolcatcherTsUrl(endpoint=endpoint)
    response = await  make_request(url, payload,headers=headers)
    result = runSolcatcherSettings(response,solcatcherSettings)
    return result

async def async_call_solcatcher_py(endpoint,*args,**kwargs):
    kwargs,solcatcherSettings,headers = get_solcatcherSettings(**kwargs)
    payload = get_payload(*args,**kwargs)
    url = getSolcatcherPairCatchUrl(endpoint=endpoint)
    response = await  make_request(url, payload,headers=headers)
    result = runSolcatcherSettings(response,solcatcherSettings)
    return result

async def async_call_solcatcher_db(endpoint,*args,**kwargs):
    kwargs,solcatcherSettings,headers = get_solcatcherSettings(True,**kwargs)
    payload = get_payload(*args,**kwargs)
    url = getSolcatcherDbCalls(endpoint=endpoint)
    response = await  make_request(url, payload,headers=headers)
    result = runSolcatcherSettings(response,solcatcherSettings)
    return result

def call_solcatcher_py(endpoint,*args,**kwargs):
    return asyncio.run(async_call_solcatcher_py(endpoint,*args,**kwargs))

def call_solcatcher_ts(endpoint,*args,**kwargs):
    return asyncio.run(async_call_solcatcher_ts(endpoint,*args,**kwargs))

def call_solcatcher_db(endpoint,*args, **kwargs):
    return asyncio.run(async_call_solcatcher_db(endpoint,*args,**kwargs))

