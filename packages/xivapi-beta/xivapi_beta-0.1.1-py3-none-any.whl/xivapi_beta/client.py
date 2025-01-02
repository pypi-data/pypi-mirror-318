import logging
import asyncio
from collections.abc import Iterable

import aiohttp
import async_property
from pythonjsonlogger.json import JsonFormatter

from .exceptions import XIVAPIError
from .endpoints.asset import XIVAPIAsset, XIVAPIAssetMap
from .endpoints.search import XIVAPISearchResult
from .endpoints.item import XIVAPIItem
from .wrapper import XIVAPIWrapper

# Configure module logging
module_logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
log_formatter = JsonFormatter()
stream_handler.setFormatter(log_formatter)
module_logger.addHandler(stream_handler)

class XIVAPIClient(XIVAPIWrapper):
    """
    Asynchronous client for accessing XIVAPI's beta endpoints. Must await instance creation.

    Supported endpoints:
        - assets
            - XIVAPIClient.assets will return an XIVAPIAsset object for general assets, maps to /asset endpoint
            - XIVAPIClient.map_assets will return an XIVAPIAssetMap object for map jpgs, maps to /asset/map endpoint
        - search
            - XIVAPIClient.search will perform a search query on XIVAPI's sheets, maps to /search endpoint
        - sheets
            - XIVAPIClient.sheets will return a list[str] of sheet names in XIVAPI, maps to /sheets endpoint
            - XIVAPIClient.get_sheet_rows maps to /sheets/{sheet} endpoint
            - XIVAPIClient.get_row maps to /sheets/{sheet}/{row_id} endpoint

    Various abstraction methods are provided as well, such as XIVAPIClient.get_item.

    :param session: aiohttp.ClientSession (will create if not provided)
    """

    _XIVAPIClient_logger = module_logger.getChild(__qualname__)

    def __init__(self, session: aiohttp.ClientSession | None = None):
        super().__init__(session)
        self._sheets = []
        # instance logger
        self._instance_logger = self._XIVAPIClient_logger.getChild(str(id(self)))
        self._instance_logger.debug("XIVAPIClient Created")

    @async_property.async_cached_property
    async def sheets(self) -> list[str]:
        """
        List of searchable sheets on XIVAPI

        Will cache this list in self._sheets, but retrieves the list asynchronously the first time
        :return: list[str] of XIVAPI data sheets
        """
        if not self._sheets:
            self._instance_logger.debug("Fetching /sheet endpoint")
            self._sheets = await self.get_endpoint('/sheet')
        return self._sheets

    async def assets(self, asset_path: str, fmt: str = 'png') -> XIVAPIAsset:
        """
        Return an XIVAPIAsset object representing the asset at the given path in the given format
        :param asset_path: the path (including .tex extension) to the desired asset, which can be found in relevant requests
        :param fmt: the format [png or jpg] to return (png is default)
        :return: xivapi.endpoints.XIVAPIAsset
        """
        return XIVAPIAsset(asset_path, self.session, fmt)

    async def map_assets(self, territory: str, index: str) -> XIVAPIAssetMap:
        """
        Return an XIVAPIAssetMap object representing the map with the given map_id and index
        :param territory:
        :param index:
        :return:
        """
        return XIVAPIAssetMap(territory, index, self.session)

    async def search(self,
                     sheets: list[str],
                     queries: list[tuple[str, str, str | int | float | bool]],
                     limit: int = 0,
                     fields: list[str] = None,
                     transient: list[str] = None) -> XIVAPISearchResult:
        """
        Perform a search on the XIVAPI on the given sheets with the given queries
        :param sheets: a list of sheets to perform the search on. valid sheets can be found from XIVAPIClient.sheets
        :param queries: a list of tuples, where each tuple is a query in the form of (key, comparator, value)
        :param limit: a limit on the number of items to return per page; if 0, defaults to 100
        :param fields: a list of fields to return for each result
        :param transient: a list of transients to return for each result
        """
        # sanitize the sheets and queries by checking that each sheet provided is valid and each query uses valid comparators
        self._instance_logger.debug("Starting sanitization")
        sheets = await self._sanitize_sheets(sheets)
        queries = self._sanitize_queries(queries)
        self._instance_logger.debug("Sanitization complete", extra={'sheets': sheets, 'queries': queries})

        # create the params to be passed to the ClientSession
        sheets_string = ','.join(sheets)
        query_string = ' '.join([f'{k}{c}"{v}"' for k, c, v in queries])
        params = {
            'sheets': sheets_string,
            'query': query_string
        }
        if fields:
            params['fields'] = ','.join(fields)
        if transient:
            params['transient'] = ','.join(transient)
        if limit > 0:
            params['limit'] = limit

        self._instance_logger.debug("Search params constructed", extra={'params': params})

        # generate the search object
        result = XIVAPISearchResult(self.session, params)
        # run the search
        self._instance_logger.debug("Search object created, running the search")
        await result.search()
        return result

    async def _sanitize_sheets(self, sheets: list[str]) -> list[str]:
        """
        Check the given list of sheets against the list of valid sheets, and discard any bad sheets
        :param sheets:
        :return: list of a valid sheets in the provided list
        """
        allowed_sheets = await self.sheets
        sanitized_sheets = []
        for sheet in sheets:
            if sheet not in allowed_sheets:
                self._instance_logger.warning("Found sheet that's not in list of valid sheets",
                                              extra={'sheet': sheet})
                pass
            else:
                sanitized_sheets.append(sheet)
        if not sanitized_sheets:
            raise XIVAPIError("No valid searchable sheets provided")
        return sanitized_sheets

    def _sanitize_queries(self,
                          queries: list[tuple[str, str, str | int | float | bool]]
                          ) -> list[tuple[str, str, str | int | float | bool]]:
        """
        Check the given list of queries to determine if they are correctly formed
        :param queries:
        :return: list of valid query tuples from the provided list
        """
        sanitized_queries = []
        for key, comparator, value in queries:
            if comparator not in self.query_comparators:
                self._instance_logger.warning("Unsupported comparator",
                                              extra={'key': key, 'comparator': comparator, 'value': value})
                pass
            else:
                sanitized_queries.append((key, comparator, value))
        if not sanitized_queries:
            raise XIVAPIError("All queries malformed")
        return sanitized_queries

    async def get_sheet_rows(self,
                             sheet: str,
                             rows: list[int] = None,
                             limit: int = 0,
                             after: int = None,
                             fields: list[str] = None,
                             transient: list[str] = None) -> list:
        """
        Returns a list of rows from the given sheet. If no other parameters are specified, returns the first 100 rows.
        :param sheet: the sheet (from self.sheets) to get rows from
        :param rows: a list of rows to retrieve. if None, returns first 100
        :param limit: the number of rows to retrieve. if 0, returns 100
        :param after: only retrieve rows after this number. if None, starts at 0
        :param fields: a list of fields from each row to return
        :param transient: a list of fields from each row's transient row to return
        :return: a list of the specific rows (or the first limit rows) in the given sheet
        """
        # make sure sheets are cached
        sheets = await self.sheets
        # check sheet validity
        if sheet not in sheets:
            self._instance_logger.warning("Requested sheet is invalid", extra={'sheet': sheet})
            raise XIVAPIError(f"{sheet} is not a valid XIVAPI sheet")

        params = {}
        if rows:
            params['rows'] = ','.join(map(str,rows))
        if limit > 0:
            params['limit'] = limit
        # required to check if not none, since after = 0 is valid and different from omitting after
        if after is not None:
            params['after'] = after
        if fields:
            params['fields'] = ','.join(fields)
        if transient:
            params['transient'] = ','.join(transient)

        url = f"/sheet/{sheet}"

        # endpoint returns a dict with schema and rows, we just want rows
        resp_dict = await self.get_endpoint(url, params=params)
        return resp_dict['rows']

    async def get_row(self,
                      sheet: str,
                      row: int,
                      fields: list[str] = None,
                      transient: list[str] = None) -> dict:
        """
        Return the requested row from the requested sheet with the given fields and transient data.
        :param sheet: the sheet (from self.sheets) to get the row from
        :param row: the row to request
        :param fields: a list of fields from the row to return. if None, returns all fields
        :param transient:
        :return:
        """
        # make sure sheets are cached
        sheets = await self.sheets
        # check sheet validity
        if sheet not in sheets:
            self._instance_logger.warning("Requested sheet is invalid", extra={'sheet': sheet})
            raise XIVAPIError(f"{sheet} is not a valid XIVAPI sheet")

        params = {}
        if fields:
            params['fields'] = ','.join(fields)
        if transient:
            params['transient'] = ','.join(transient)

        url = f"/sheet/{sheet}/{row}"

        return await self.get_endpoint(url, params=params)

    async def get_result_row(self, result: dict) -> dict:
        """
        Gets the sheet row of the given search result dict
        :param result: a dict containing at least 'sheet' and 'row_id' keys, usually from a list of results from an
        XIVAPISearchResult object
        :return: the full JSON response from XIVAPI for the given result's sheet and row_id
        """
        return await self.get_row(result['sheet'], result['row_id'])


    async def get_item(self, item_name: str) -> XIVAPIItem:
        """
        Returns an XIVAPIItem object that best matches the given item name

        This is an abstraction layer for performing an api search with the given item name, retrieving the best result,
        and getting the full result row and storing it in an XIVAPIItem object
        :param item_name: the item name to search for
        :return: XIVAPIItem, an interactive object with all the API data about the requested item
        """
        # search time
        search_obj = await self.search(['Item'], [('Name', '~', item_name)])
        result = await search_obj.best_results()
        if not result:
            raise XIVAPIError("Item not found")
        item = await self.get_result_row(result[0])
        return XIVAPIItem(self.session, item)