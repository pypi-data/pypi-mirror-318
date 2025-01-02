import logging

import aiohttp

from .exceptions import XIVAPIError


# configure module logging
module_logger = logging.getLogger(__name__)


class XIVAPIWrapper:
    """
    Wrapper class for XIVAPI Objects. Handles interacting with aiohttp ClientSession objects

    :param session: class:`aiohttp.ClientSession`
    :param base_url: the base url of the XIVAPI
    :param query_comparators: a list of valid search comparators
    """

    base_url = "https://beta.xivapi.com/api/1"
    query_comparators = [
        "=",
        "~",
        ">",
        ">=",
        "<",
        "<="
    ]
    _XIVAPIWrapper_logger = module_logger.getChild(__qualname__)

    def __init__(self, session: aiohttp.ClientSession | None = None):
        self._session = session
        # instance logger
        self._instance_logger = self._XIVAPIWrapper_logger.getChild(str(id(self)))

    @property
    def session(self) -> aiohttp.ClientSession:
        """
        Returns this object's aiohttp.ClientSession, or creates a new one if it's closed/doesn't exist yet
        :return:
        """
        if self._session is None or self._session.closed:
            self._instance_logger.debug("Creating new aiohttp ClientSession object")
            self._session = aiohttp.ClientSession()
        return self._session

    async def _process_response(self, response: aiohttp.ClientResponse) -> None:
        """
        Check response for error codes, and if none are found, pass along the response object.
        :param response: aiohttp.ClientResponse response from self.session.get()
        :return: ClientResponse
        :raise: XIVAPIError if non-200 status code, or if response could not be processed into JSON
        """
        if response.status == 400:
            self._instance_logger.warning("Error code 400")
            raise XIVAPIError(f"400 code received: {response.url} + {response.real_url}")
        elif response.status == 404:
            self._instance_logger.warning("Error code 404")
            raise XIVAPIError(f"404 code received: {response.url} + {response.real_url}")
        elif response.status != 200:
            self._instance_logger.warning("Non-200 response code received", extra={'response_code': response.status})
            raise XIVAPIError(f"{response.status} code received: {response.url} + {response.real_url}")
        else:
            self._instance_logger.info("200 code received, processing complete")
            return

    async def get_endpoint(self, endpoint: str, params: dict[str, str] = None, json: bool = True) -> dict | list | bytes:
        """
        Retrieve data from the given XIVAPI endpoint as JSON unless specified
        :param endpoint: the specific endpoint to request from
        :param params: optional parameters (added as ?key=value)
        :param json: bool representing type of data to retrieve
        :return: aiohttp.ClientResponse
        :raise: XIVAPIError if response cannot be read
        """
        #generate full url
        url = self.base_url + endpoint
        if params is None:
            params = {}
        self._instance_logger.debug("Sending endpoint request", extra={'url': url, 'params': params})
        async with self.session.get(url, params=params) as response:
            self._instance_logger.debug("Response created, processing object")
            await self._process_response(response)
            # try to get the data
            try:
                if json:
                    data = await response.json()
                else:
                    data = await response.read()
            except aiohttp.ContentTypeError as e:
                self._instance_logger.warning("JSON data expected, but not received",
                                              extra={'content-type': response.content_type,
                                                     'error': e})
                raise XIVAPIError(e)
            except aiohttp.ClientResponseError as e:
                self._instance_logger.warning("Bytestream could not be read",
                                              extra={'content-type': response.content_type,
                                                     'error': e})
                raise XIVAPIError(e)
            else:
                return data