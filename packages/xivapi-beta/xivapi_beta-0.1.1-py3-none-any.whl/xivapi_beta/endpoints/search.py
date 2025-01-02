import logging
import asyncio

import aiohttp
from pythonjsonlogger.json import JsonFormatter

from ..wrapper import XIVAPIWrapper
from ..exceptions import XIVAPIError

# Configure module logging
module_logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
log_formatter = JsonFormatter()
log_handler.setFormatter(log_formatter)
module_logger.addHandler(log_handler)


class XIVAPISearchResult(XIVAPIWrapper):
    """
    An object representing the results of a search on XIVAPI's data
    """
    _XIVAPISearchResult_logger = module_logger.getChild(__qualname__)

    def __init__(self,
                 session: aiohttp.ClientSession,
                 params: dict):
        # wrapper setup
        super().__init__(session)
        # logger
        self._instance_logger = self._XIVAPISearchResult_logger.getChild(str(id(self)))

        # initialize private vars
        self._data = {}
        self._pages = {}

        self.params = params
        self._instance_logger.debug("Search object created successfully")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        raise XIVAPISearchError("Altering search result data is disallowed")

    async def _get_next_page(self, page: int):
        """
        Gets the next page of results and stores it in self._pages
        :param page: the current page
        """
        # check if the page is already cached
        if self._pages.get(page + 1) is not None:
            return
        # otherwise, fetch it if there is a next page
        next_page_cursor = self._pages[page].get('next')
        if next_page_cursor is None:
            raise XIVAPISearchError("No next page to get")
        else:
            next_page_data = await self.get_endpoint('/search', params={'cursor': next_page_cursor})
            self._pages[page + 1] = next_page_data

    async def _get_pages(self, n: int = 10):
        """
        Gets the first n pages of the result that exist.
        """
        current_page = 1
        while current_page <= n:
            try:
                await self._get_next_page(current_page)
            except XIVAPISearchError:
                break
            current_page += 1

    async def search(self, full=False):
        """
        Run this search again, taking into account any param changes
        :param full: if True, search until there are no more "next" pages in the data (max 10 pages)
        :return: None
        """
        # get data from the client
        self._instance_logger.debug("Initiating first search")
        try:
            self._instance_logger.debug("Sending request")
            data = await self.get_endpoint('/search', params=self.params)
        except XIVAPIError as e:
            self._instance_logger.warning("XIVAPIError received", extra={'error': str(e)})
            raise XIVAPISearchError(e)
        else:
            self._data = data
            # store the first page of data (we fully reset the _pages here because it's a new search)
            self._pages = {1: data.copy()}

        if full:
            await self._get_pages()

    async def get_results(self, limit: int = 0):
        # initialize loop vars
        total_results = 0                                       # num results seen
        limited = limit > 0                                     # if this gen is limited or not
        current_page = 1                                        # the current page of data
        results = self._pages[current_page]['results'].copy()   # a copy of the list of results from page 1

        while not limited or total_results < limit:
            if not results:
                # if the results list is empty, get the next page of results
                try:
                    await self._get_next_page(current_page)
                except XIVAPISearchError:
                    # if there's no next page, break the loop
                    break
                else:
                    current_page += 1
                    results = self._pages[current_page]['results'].copy()
            # yield the best result and pop it off the list, then iterate total
            yield results.pop(0)
            total_results += 1

    async def best_results(self, count: int = 1) -> list[dict]:
        """
        Return a list of the first count results from the search. If the search yielded fewer results than count, will
        return the full list of results.
        :return:
        """
        cur_page = 1
        results = []
        num_results = 0
        while count > num_results:
            if cur_page not in self._pages:
                try:
                    await self._get_next_page(cur_page - 1)
                except XIVAPISearchError:
                    break
            results.extend(self._pages[cur_page]['results'][:count - num_results])
            cur_page += 1
            num_results = len(results)
        return results

    async def best_result(self):
        results = await self.best_results()
        return results[0]


class XIVAPISearchError(Exception):
    pass