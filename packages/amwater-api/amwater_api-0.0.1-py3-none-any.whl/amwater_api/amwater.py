""" Base American Water Missouri Class """
import logging

from .amwater_client import AmwaterClient

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

class Amwater():
    """ Define amwater Class """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._query_params = None
        self._token = None
        self._api_client = AmwaterClient(username, password)
        debug = False
        if debug:
            _LOGGER.setLevel(logging.DEBUG)

    async def get_token(self,session):
        """ Get Token """
        return await self._api_client._get_token(session)
    
    async def get_params(self,session):
        """ Get Params """
        return await self._api_client._get_query_parameters(session)

    async def get_request(self,strin):
        """ Get Token """
        return await self._api_client._get_request(strin)
    
    async def get_24hr(self):
        """ Get 24 Hour Data """
        return await self._api_client._get_24hr()
    
    async def get_30day(self):
        """ Get 24 Hour Data """
        return await self._api_client._get_30day()
