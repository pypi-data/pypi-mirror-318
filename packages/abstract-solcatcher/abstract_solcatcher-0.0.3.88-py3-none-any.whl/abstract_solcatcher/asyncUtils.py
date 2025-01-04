import asyncio,httpx
from .utils import *
from abstract_apis import get_headers
async def make_request(url, payload, headers=None):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return response.json()       # or just return response if you want the full object
    except Exception as e:
        print(f"HTTP request failed: {str(e)} - Payload: {payload}")
        return None


async def async_call_solcatcher_ts(endpoint,*args,**kwargs):
    payload = get_payload(*args,**kwargs)
    url = getSolcatcherTsUrl(endpoint=endpoint)
    return await  make_request(url, payload,headers=get_headers())

async def async_call_solcatcher_py(endpoint,*args,**kwargs):
    payload = get_payload(*args,**kwargs)
    url = getSolcatcherPairCatchUrl(endpoint=endpoint)
    return await make_request(url, payload,headers=get_headers())

async def async_call_solcatcher_db(endpoint,*args,**kwargs):
    payload = get_payload(*args,**kwargs)
    url = getSolcatcherDbCalls(endpoint=endpoint)
    return await make_request(url, payload,headers=get_db_header())

def call_solcatcher_py(endpoint,*args,**kwargs):
    return asyncio.run(async_call_solcatcher_py(endpoint,*args,**kwargs))

def call_solcatcher_ts(endpoint,*args,**kwargs):
    return asyncio.run(async_call_solcatcher_ts(endpoint,*args,**kwargs))

def call_solcatcher_db(endpoint,*args, **kwargs):
    return asyncio.run(async_call_solcatcher_db(endpoint,*args,**kwargs))

