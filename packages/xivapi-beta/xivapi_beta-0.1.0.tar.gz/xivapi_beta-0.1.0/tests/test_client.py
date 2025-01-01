import pytest
import asyncio
import json
import random

from aioresponses import aioresponses
from xivapi_beta.client import XIVAPIClient
from xivapi_beta.exceptions import XIVAPIError
from xivapi_beta.endpoints.search import XIVAPISearchResult

#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class TestXIVAPIClient:

    client = XIVAPIClient()

    @pytest.mark.asyncio
    async def test_sheets(self, sheets_list):
        sheets = await self.client.sheets

        assert sheets == sheets_list

    @pytest.mark.asyncio
    async def test_bad_sheets_search(self):
        with pytest.raises(XIVAPIError) as api_error:
            search_result = await self.client.search(['blah'],
                                                     [])
    @pytest.mark.asyncio
    async def test_bad_queries_search(self):
        with pytest.raises(XIVAPIError) as api_error:
            search_result = await self.client.search(['Item'],
                                                     [('Name', 'NOT', 'blah')])

    @pytest.mark.asyncio
    async def test_search_results_type(self, mocked_search, search_data):
        search_result = await self.client.search(search_data['sheets'],
                                                 search_data['queries'])
        assert type(search_result) is XIVAPISearchResult

    @pytest.mark.asyncio
    @pytest.mark.parametrize('limit,after',
                             [(random.randint(1,99),
                               random.randint(0, 99)) for _ in range(10)])
    async def test_get_sheet_rows_with_limit_and_after(self, mocked_response, item_sheet_data, limit, after):
        resp_rows = item_sheet_data['rows'].copy()[after:after + limit]
        resp_data = item_sheet_data.copy()
        resp_data['rows'] = resp_rows
        item_sheet_url = (f'{XIVAPIClient.base_url}/sheet/Item?'
                          f'limit={limit}&after={after}')
        mocked_response.get(item_sheet_url, status=200,
                            payload=resp_data)
        rows = await self.client.get_sheet_rows('Item', limit=limit, after=after)
        assert rows['rows'] == item_sheet_data['rows'][after:after + limit]

    @pytest.mark.asyncio
    @pytest.mark.parametrize('rows',
                             [[random.randint(0,99) for _ in range(10)] for _ in range(10)])
    async def test_get_sheet_rows_specific_rows(self, mocked_response, item_sheet_data, rows):
        resp_rows = [item_sheet_data['rows'][x] for x in rows]
        resp_data = item_sheet_data.copy()
        resp_data['rows'] = resp_rows
        item_sheet_url = f'{XIVAPIClient.base_url}/sheet/Item?rows={",".join(map(str,rows))}'
        mocked_response.get(item_sheet_url, status=200,
                            payload=resp_data)
        result_rows = await self.client.get_sheet_rows('Item', rows=rows)
        assert result_rows['rows'] == resp_rows

    @pytest.mark.asyncio
    async def test_get_sheet_rows_default(self, mocked_response, item_sheet_data):
        item_sheet_url = f'{XIVAPIClient.base_url}/sheet/Item'
        mocked_response.get(item_sheet_url, status=200, payload=item_sheet_data)
        result_rows = await self.client.get_sheet_rows('Item')
        assert result_rows == item_sheet_data