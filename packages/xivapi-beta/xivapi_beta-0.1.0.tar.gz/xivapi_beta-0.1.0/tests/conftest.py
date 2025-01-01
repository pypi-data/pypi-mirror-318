import pytest
import json

from aioresponses import aioresponses
from xivapi_beta.client import XIVAPIClient

@pytest.fixture
def sheet_url():
    return XIVAPIClient.base_url + '/sheet'

@pytest.fixture
def search_url():
    return XIVAPIClient.base_url + '/search'

with open('sheet.json', 'r') as f:
    SHEETS_LIST_GLOBAL = json.load(f)

@pytest.fixture
def sheets_list():
    return SHEETS_LIST_GLOBAL

with open('search_results.json', 'r') as f:
    SEARCH_RESULTS_PAYLOAD_GLOBAL = json.load(f)

with open('search_results_2.json', 'r') as f:
    SEARCH_RESULTS_PAYLOAD_2_GLOBAL = json.load(f)

@pytest.fixture
def search_results_payload():
    return SEARCH_RESULTS_PAYLOAD_GLOBAL

@pytest.fixture
def search_results_payload_2():
    return SEARCH_RESULTS_PAYLOAD_2_GLOBAL

with open('Item.json', 'r') as f:
    ITEM_SHEET_DATA_GLOBAL = json.load(f)

@pytest.fixture
def item_sheet_data():
    return ITEM_SHEET_DATA_GLOBAL

@pytest.fixture
def search_data():
    return {
        'sheets': ['Item'],
        'queries': [('Name', '~', 'archeo')]
    }

@pytest.fixture
def mocked_response():
    with aioresponses() as m:
        yield m

@pytest.fixture(autouse=True)
def mocked_sheets(mocked_response, sheet_url, sheets_list):
    mocked_response.get(sheet_url, status=200, payload=sheets_list)

@pytest.fixture
def mocked_search(mocked_response, search_data, search_url, search_results_payload):
    sheets_string = ','.join(search_data['sheets'])
    query_string = ' '.join([f'{k}{c}"{v}"' for k, c, v in search_data['queries']])
    search_url_string = f'{search_url}?query={query_string}&sheets={sheets_string}'
    mocked_response.get(search_url_string, status=200,
                        payload=search_results_payload)