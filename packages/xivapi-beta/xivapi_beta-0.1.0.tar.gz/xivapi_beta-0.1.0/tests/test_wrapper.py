import asyncio

import aiohttp
import pytest
from aioresponses import aioresponses

from xivapi_beta.wrapper import XIVAPIWrapper


@pytest.fixture
def mocked_response():
    with aioresponses() as m:
        yield m

@pytest.mark.asyncio
async def test_get_endpoint(sheets_list):
    wrapper = XIVAPIWrapper()

    resp = await wrapper.get_endpoint('/sheet')
    assert resp == sheets_list