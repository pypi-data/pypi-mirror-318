import random

import aiohttp
import pytest

from xivapi_beta.exceptions import XIVAPIError
from xivapi_beta.wrapper import XIVAPIWrapper


class TestXIVAPIWrapper:
    wrapper = XIVAPIWrapper()

    @pytest.mark.asyncio
    async def test_session(self):
        session = self.wrapper.session
        assert isinstance(session, aiohttp.ClientSession)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("code", [404, 400, 301])
    async def test_process_response_failure(self, code, mocked_response):
        mocked_response.get(f'{self.wrapper.base_url}/test', status=code)
        with pytest.raises(XIVAPIError):
            async with self.wrapper.session.get(f'{self.wrapper.base_url}/test') as response:
                print(response.status)
                await self.wrapper._process_response(response)

    @pytest.mark.asyncio
    async def test_get_endpoint(self, sheets_list):
        resp = await self.wrapper.get_endpoint('/sheet')
        assert resp == sheets_list