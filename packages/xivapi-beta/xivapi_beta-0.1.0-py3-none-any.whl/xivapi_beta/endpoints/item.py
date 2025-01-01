import logging
import asyncio
from collections.abc import Iterable

import aiohttp
import async_property
from pythonjsonlogger.json import JsonFormatter

from ..exceptions import XIVAPIError
from ..endpoints.asset import XIVAPIAsset
from ..wrapper import XIVAPIWrapper

# Configure module logging
module_logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
log_formatter = JsonFormatter()
log_handler.setFormatter(log_formatter)
module_logger.addHandler(log_handler)

class XIVAPIItem(XIVAPIWrapper):
    # class logger
    _XIVAPIItem_logger = module_logger.getChild(__qualname__)

    def __init__(self, session, item_data):
        super().__init__(session)
        # instance logger
        self._instance_logger = self._XIVAPIItem_logger.getChild(str(id(self)))

        self._data = item_data

        self.icon_data = item_data['fields']['Icon']
        self.icon = XIVAPIAsset(self.session, self.icon_data['path_hr1'])
        self.name = item_data['fields']['Name']
        self.item_id = item_data['row_id']

    async def get_icon_file(self, path: str) -> str:
        """
        Create a file for this asset's icon starting at path
        """
        return await self.icon.create_asset_file(path)

    async def get_icon_data(self) -> bytes:
        """
        Returns the raw bytes data of this item's icon
        """
        return await self.icon.asset_bytes()


class XIVAPIItemError(Exception):
    pass