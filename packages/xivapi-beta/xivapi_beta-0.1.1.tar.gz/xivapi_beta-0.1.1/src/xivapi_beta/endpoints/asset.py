import logging
import asyncio
import os.path

import aiohttp
from pythonjsonlogger.json import JsonFormatter

from ..exceptions import XIVAPIError
from ..wrapper import XIVAPIWrapper

# Configure module logging
module_logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
log_formatter = JsonFormatter()
log_handler.setFormatter(log_formatter)
module_logger.addHandler(log_handler)

class XIVAPIAsset(XIVAPIWrapper):
    """
    An object representing the response of a request to the /asset endpoint
    """
    # class logger
    _XIVAPIAsset_logger = module_logger.getChild(__qualname__)

    def __init__(self, asset_path: str, session: aiohttp.ClientSession = None, fmt: str = 'png'):
        super().__init__(session)
        # logger
        self._instance_logger = self._XIVAPIAsset_logger.getChild(str(id(self)))

        self._data = None

        self.asset_path = asset_path
        self.asset_name = self.asset_path.split('/')[3].split('.')[0]
        self.fmt = fmt
        self.params = {'path': asset_path, 'format': fmt}

    async def _get_asset_data(self):
        self._data = await self.get_endpoint('/asset', self.params, False)

    async def create_asset_file(self, base_path: str) -> str:
        """
        Create an icon file from this object's data
        :param base_path: the base path to create the icon in
        :return: path to icon
        """
        icon_path = f'{base_path}/{self.asset_name}.{self.fmt}'
        if os.path.isfile(icon_path):
            # return the path if we've already got this icon file
            return icon_path
        else:
            with open(icon_path, 'wb') as icon_file:
                if self._data is None:
                    await self._get_asset_data()
                icon_file.write(self._data)
            return icon_path

    async def asset_bytes(self) -> bytes:
        if self._data is None:
            await self._get_asset_data()
        return self._data


class XIVAPIAssetMap(XIVAPIAsset):

    def __init__(self, territory: str, index: str, session: aiohttp.ClientSession = None):
        fmt = 'jpg'

        asset_path = f'/asset/map/{territory}/{index}'
        super().__init__(asset_path, session, fmt)

        self.asset_name = f'{territory}_{index}'

    async def _get_asset_data(self):
        self._data = await self.get_endpoint(self.asset_path, json=False)