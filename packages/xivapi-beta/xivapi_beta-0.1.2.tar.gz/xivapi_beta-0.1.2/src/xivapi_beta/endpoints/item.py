import logging

from ..endpoints.asset import XIVAPIAsset
from ..wrapper import XIVAPIWrapper


# Configure module logging
module_logger = logging.getLogger(__name__)


class XIVAPIItem(XIVAPIWrapper):
    """
    An abstraction for interacting with specific rows from the Item sheet of XIVAPI

    :param icon: an XIVAPIAsset object with this item's icon data
    :param name: the name of this item
    :param item_id: the row ID of this item from XIVAPI's Item sheet
    :param market_info: the ItemSearchCategory field from the Item sheet
    :param item_level_info: the LevelItem field from the Item sheet
    """
    # class logger
    _XIVAPIItem_logger = module_logger.getChild(__qualname__)

    def __init__(self, session, item_data):
        super().__init__(session)
        # instance logger
        self._instance_logger = self._XIVAPIItem_logger.getChild(str(id(self)))

        self._data = item_data

        self.icon_data = item_data['fields']['Icon']
        self.icon = XIVAPIAsset(self.icon_data['path_hr1'], self.session)
        self.name = item_data['fields']['Name']
        self.item_id = item_data['row_id']
        self.market_info = item_data['fields']['ItemSearchCategory']
        self.item_level_info = item_data['fields']['LevelItem']

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