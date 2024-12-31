import datetime
from typing import Literal, overload
import aiohttp
from multidict import CIMultiDictProxy, CIMultiDict
from . import error as exceptions
import json


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "x-csrftoken": "a",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://scratch.mit.edu",
}

def create_ClientSession(inp:"ClientSession|None"=None) -> "ClientSession":
    return inp if isinstance(inp,ClientSession) else ClientSession(header=headers)

json_resp = dict[str,"json_resp"]|list["json_resp"]|str|float|int|bool|None
class Response:
    def __str__(self) -> str:
        return f"<Response [{self.status_code}] {self.text}>"

    def __init__(self,status:int,text:str,headers:CIMultiDictProxy[str]) -> None:
        self.status_code:int = status
        self.text:str = text
        self.headers:CIMultiDict[str] = headers.copy()
    
    def json(self) -> json_resp:
        return json.loads(self.text)
    
class BytesResponse(Response):
    def __str__(self) -> str:
        return f"<BytesResponse [{self.status_code}] {len(self.text)}bytes> "
    
    def __init__(self,status:int,data:bytes,headers:CIMultiDictProxy[str]) -> None:
        self.status_code:int = status
        self.text:bytes = data
        self.headers:CIMultiDict[str] = headers.copy()

    def json(self) -> None:
        return None

class ClientSession(aiohttp.ClientSession):

    def __init__(self,header:dict) -> None:
        super().__init__()
        self._header = header
        self._cookie = {}
    
    @property
    def header(self) -> dict:
        return self._header.copy()
    
    @property
    def cookie(self) -> dict:
        return self._cookie.copy()
    
    async def _check(self,response:Response) -> None:
        if response.status_code in [403,401]:
            raise exceptions.Unauthorized(response.status_code,response)
        if response.status_code in [429]:
            raise exceptions.TooManyRequests(response.status_code,response)
        if response.status_code in [404]:
            raise exceptions.HTTPNotFound(response.status_code,response)
        if response.status_code // 100 == 4:
            raise exceptions.BadRequest(response.status_code,response)
        if response.status_code // 100 == 5:
            raise exceptions.ServerError(response.status_code,response)
        if response.text == '{"code":"BadRequest","message":""}':
            raise exceptions.BadResponse(response.status_code,response)

    async def _send_requests(
        self,obj:"ClientSession.get|ClientSession.post|ClientSession.put|ClientSession.delete",url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:bool=False
    ):
        if self.closed: raise exceptions.SessionClosed
        if header is None: header = self._header.copy()
        if cookie is None: cookie = self._cookie.copy()
        try:
            async with obj(
                url,data=data,json=json,timeout=timeout,params=params,headers=header,cookies=cookie
            ) as response:
                response:aiohttp.ClientResponse
                if is_binary: r = BytesResponse(response.status,await response.read(),response.headers)
                else: r = Response(response.status,await response.text(),response.headers)
                response.close()
        except Exception as e:
            raise exceptions.HTTPFetchError(e)
        if check: await self._check(r)
        return r

    @overload
    async def get(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[False]=False
    ) -> Response: ...
    
    @overload
    async def get(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[True]
    ) -> BytesResponse: ...

    async def get(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:bool=False
    ) -> Response|BytesResponse:
        return await self._send_requests(
            super().get,url=url,
            data=data,json=json,timeout=timeout,params=params,
            header=header,cookie=cookie,check=check,is_binary=is_binary
        )
    
    @overload
    async def post(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[False]=False
    ) -> Response: ...
    
    @overload
    async def post(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[True]
    ) -> BytesResponse: ...

    async def post(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:bool=False
    ) -> Response|BytesResponse:
        return await self._send_requests(
            super().post,url=url,
            data=data,json=json,timeout=timeout,params=params,
            header=header,cookie=cookie,check=check,is_binary=is_binary
        )
    
    @overload
    async def put(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[False]=False
    ) -> Response: ...
    
    @overload
    async def put(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[True]
    ) -> BytesResponse: ...

    async def put(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:bool=False
    ) -> Response|BytesResponse:
        return await self._send_requests(
            super().put,url=url,
            data=data,json=json,timeout=timeout,params=params,
            header=header,cookie=cookie,check=check,is_binary=is_binary
        )
    
    @overload
    async def delete(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[False]=False
    ) -> Response: ...
    
    @overload
    async def delete(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:Literal[True]
    ) -> BytesResponse: ...

    async def delete(
        self,url:str,*,
        data=None,json:dict=None,timeout:float=None,params:dict[str,str]=None,
        header:dict[str,str]=None,cookie:dict[str,str]=None,check:bool=True,is_binary:bool=False
    ) -> Response|BytesResponse:
        return await self._send_requests(
            super().delete,url=url,
            data=data,json=json,timeout=timeout,params=params,
            header=header,cookie=cookie,check=check,is_binary=is_binary
        )



async def api_iterative(
        session:ClientSession,
        url:str,
        *,
        limit:int|None=None,
        offset:int=0,
        max_limit=40,
        add_params:dict={}
    ) -> list[dict]:
    """
    APIを叩いてリストにして返す
    """
    if offset < 0:
        raise ValueError("offset parameter must be >= 0")
    if limit < 0:
        raise ValueError("limit parameter must be >= 0")
    if limit is None:
        limit = max_limit
    
    api_data = []
    for i in range(offset,offset+limit,max_limit):
        r = await session.get(
            url,timeout=10,
            params=dict(limit=max_limit,offset=i,**add_params)
        )
        jsons = r.json()
        if not isinstance(jsons,list):
            raise exceptions.HTTPError
        api_data.extend(jsons)
        if len(jsons) < max_limit:
            break
    return api_data[:limit]



def split_int(raw:str, text_before:str, text_after:str) -> int|None:
    try:
        return int(raw.split(text_before)[1].split(text_after)[0])
    except Exception:
        return None
    
def split(raw:str, text_before:str, text_after:str) -> str:
    try:
        return raw.split(text_before)[1].split(text_after)[0]
    except Exception:
        return None
    
def to_dt(text:str,default:datetime.datetime|None=None) -> datetime.datetime|None:
    try:
        return datetime.datetime.fromisoformat(f'{text.replace("Z","")}+00:00')
    except Exception:
        return default
    
def no_data_checker(obj) -> None:
    if obj is None:
        raise exceptions.NoDataError
    
def try_int(inp:str|int) -> int:
    try:
        return int(inp)
    except Exception:
        raise ValueError

empty_project_json = {
    'targets': [
        {
            'isStage': True,
            'name': 'Stage',
            'variables': {
                '`jEk@4|i[#Fk?(8x)AV.-my variable': [
                    'my variable',
                    0,
                ],
            },
            'lists': {},
            'broadcasts': {},
            'blocks': {},
            'comments': {},
            'currentCostume': 0,
            'costumes': [
                {
                    'name': '',
                    'bitmapResolution': 1,
                    'dataFormat': 'svg',
                    'assetId': '14e46ec3e2ba471c2adfe8f119052307',
                    'md5ext': '14e46ec3e2ba471c2adfe8f119052307.svg',
                    'rotationCenterX': 0,
                    'rotationCenterY': 0,
                },
            ],
            'sounds': [],
            'volume': 100,
            'layerOrder': 0,
            'tempo': 60,
            'videoTransparency': 50,
            'videoState': 'on',
            'textToSpeechLanguage': None,
        },
    ],
    'monitors': [],
    'extensions': [],
    'meta': {
        'semver': '3.0.0',
        'vm': '2.3.0',
        'agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    },
}

BIG = 99999999