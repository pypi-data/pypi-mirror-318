"""amwater API Client."""
import logging

import httpx
import json
import datetime
import re
from bs4 import BeautifulSoup
from types import SimpleNamespace
from urllib.parse import urlparse,parse_qs

from .errors import AmwaterError
#from .models.base import 

_LOGGER = logging.getLogger(__name__)
_LOGGER.addHandler(logging.StreamHandler())
_LOGGER.setLevel(logging.INFO)

def _enable_debug_logging():
    _LOGGER.setLevel(logging.DEBUG)

class AmwaterClient():
    """amwater API Client"""
    def __init__(
        self,
        username,
        password,
        debug=False,
    ):
        if debug:
            _enable_debug_logging()
        
        self._username = username
        self._password = password
        self._auth_uri = 'https://auth.amwater.com'
        self._api_uri = 'https://mywaterv2.amwater.com/api/mso/data'

    async def _get_token (self,session):
        """ Get American Water API Token """
        try:
            req = await session.get(f'{self._auth_uri}/oauth2/aus29oxmv4bzpt55X5d7/v1/authorize?client_id=0oa29ovb79AWEoS8V5d7&redirect_uri=https://mywaterv2.amwater.com/openidlogin&response_type=code&scope=openid%20email%20%20profile%20%20UserContext%20offline_access%20GroupMembership&state=Ye1yPb')
            soup = BeautifulSoup(req.text, 'html.parser')
            data = soup.find_all('script')[2].string
            match = re.search(r'stateToken(.*?);', data)
            variable_value = match.group(1).encode().decode('unicode_escape')
            state = variable_value.replace("=","").replace("'","")

            payload = {
                'stateToken': state
            }
            headers = {
                'Content-Type': 'application/ion+json; okta-version=1.0.0',
                'Accept': 'application/ion+json; okta-version=1.0.0',
                'x-okta-user-agent-extended': 'okta-auth-js/7.9.0 okta-signin-widget-7.26.1'
            }

            introspect = await session.post(f'{self._auth_uri}/idp/idx/introspect',json=payload, headers=headers)

            nonce = await session.post(f'{self._auth_uri}/api/v1/internal/device/nonce')

            payload = {
                'identifier': self._username,
                'stateHandle': state
            }

            identify = await session.post(f'{self._auth_uri}/idp/idx/identify', json=payload)
            state = identify.json()['stateHandle'] 

            payload = {
                'credentials' : {
                    'passcode' : self._password
                },
                'stateHandle' : state
            }

            answer = await session.post(f'{self._auth_uri}/idp/idx/challenge/answer', json=payload)

            payload = {
                'stateHandle': state
            }
            redirect = await session.get(f'{self._auth_uri}/login/token/redirect?stateToken='+state)
            location = redirect.headers['Location']

            openidlogin = await session.get(location)
            bearer = session.cookies['mw_id_token']

            return bearer
        except Exception as error:
            raise AmwaterError(400, error)

    async def _get_query_parameters(self,session) -> dict:
        """Get the query parameters from the API."""
        try:
            headers = {
                'Authorization': f'Bearer {self._token}'
            }
            payload = {
                "pipelineId":"com::apporchid::cloudseer::mso::myaccountsummarypipeline",
                "requestParameters":{
                    "@class":"com.apporchid.common.UIRequestParameters",
                    "keyValueMap":{
                        "queryParams":None
                        }
                    }
                }
            params = await session.post('https://mywaterv2.amwater.com/api/mso/data',json=payload,headers=headers)
            params = params.json()['data'][0]['additionalInformation']['IntermediaryPageDetails'][0]
            return params
        except Exception as error:
            raise AmwaterError(400, error) 
               
    async def _get_request(self, payload: dict) -> dict:
        """Make a GET request to the API."""
        async with httpx.AsyncClient() as session:
            try:
               self._token = await self._get_token(session)
               headers = {
                     'Authorization': f'Bearer {self._token}',
               }

               self._query_params = await self._get_query_parameters(session)
               payload['requestParameters']['keyValueMap']['queryParams']['businessPartnerNumber'] = self._query_params['businessPartnerNumber']
               payload['requestParameters']['keyValueMap']['queryParams']['connectionContractNumber'] = self._query_params['contractAccountNumber']
               payload['requestParameters']['keyValueMap']['queryParams']['premiseId'] = self._query_params['premiseNumber']
               payload['requestParameters']['keyValueMap']['queryParams']['regionName'] = self._query_params['state']
               payload['requestParameters']['keyValueMap']['queryParams']['premiseStateCode'] = self._query_params['state']
               payload['requestParameters']['keyValueMap']['queryParams']['stateCode'] = self._query_params['state']

               response = await session.post(self._api_uri,json=payload,headers=headers)
               return response.text
            except Exception as error:
                raise AmwaterError(400, error)
            
    async def _get_24hr(self) -> dict:
        """Get 24 hour data."""
        payload = {
            "pipelineId":"com::apporchid::cloudseer::mso::HourlyConsumptionPipeline",
            "requestParameters":{
                "@class":"com.apporchid.common.UIRequestParameters",
                "keyValueMap":{
                    "queryParams":{
                        "businessPartnerNumber":None,
                        "connectionContractNumber":None,
                        "premiseId":None,
                        "billMonth":"",
                        "limitRecords":2,
                        "regionName":None,
                        "startDate":"",
                        "endDate":"",
                        "source":"",
                        "premiseStateCode":None,
                        "stateCode":None,
                        "serviceUrl":"",
                        "accountType":"",
                        "days":"24",
                        "selectedVal":"24"
                    }
                }
            }
        }
        return await self._get_request(payload)
    
    async def _get_30day(self) -> dict:
        """Get 24 hour data."""
        payload = {
            "pipelineId":"com::apporchid::cloudseer::mso::dailyconsumptionpipeline",
            "requestParameters":{
                "@class":"com.apporchid.common.UIRequestParameters",
                "keyValueMap":{
                    "queryParams":{
                        "businessPartnerNumber":None,
                        "connectionContractNumber":None,
                        "premiseId":None,
                        "billMonth":"",
                        "limitRecords":2,
                        "regionName":None,
                        "startDate":"",
                        "endDate":"",
                        "source":"",
                        "premiseStateCode":None,
                        "stateCode":None,
                        "serviceUrl":"",
                        "accountType":"",
                        "days":"30",
                        "selectedVal":"30"
                    }
                }
            }
        }
        return await self._get_request(payload)