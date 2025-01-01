import aiohttp
import pytest
import pytest_asyncio
import asyncio
import json
import random

from aioresponses import aioresponses
from xivapi_beta.client import XIVAPIClient
from xivapi_beta.endpoints.search import XIVAPISearchResult
from xivapi_beta.endpoints.search import XIVAPISearchError


class TestXIVAPISearchResult:
    client = XIVAPIClient()
    dummy_result = XIVAPISearchResult(None, {})

    @pytest.fixture
    def mocked_search_pages(self, mocked_response, search_data, search_results_payload, search_results_payload_2):
        search_url = f'{self.client.base_url}/search'
        query_string = ' '.join([f'{k}{c}"{v}"' for k, c, v in search_data['queries']])
        sheets_string = ','.join(search_data['sheets'])
        first_search_url = f'{search_url}?query={query_string}&sheets={sheets_string}'
        cursor_search_url = f'{search_url}?cursor={search_results_payload["next"]}'
        mocked_response.get(f'{first_search_url}', status=200, payload=search_results_payload)
        mocked_response.get(f'{first_search_url}', status=200, payload=search_results_payload)
        mocked_response.get(f'{cursor_search_url}', status=200,
                            payload=search_results_payload_2)

    @pytest.mark.asyncio
    async def test_data(self, mocked_search, search_data, search_results_payload):
        search_result = await self.client.search(search_data['sheets'],
                                                 search_data['queries'])
        data = search_result.data
        assert search_results_payload == data

    def test_data_set(self):
        with pytest.raises(XIVAPISearchError) as e:
            self.dummy_result.data = {}

    @pytest.mark.asyncio
    async def test_full_search(self, mocked_search_pages, search_data, search_results_payload, search_results_payload_2):
        search_result = await self.client.search(search_data['sheets'],
                                                 search_data['queries'])

        await search_result.search(full=True)

        pages = {1: search_results_payload,
                 2: search_results_payload_2}

        assert pages == search_result._pages