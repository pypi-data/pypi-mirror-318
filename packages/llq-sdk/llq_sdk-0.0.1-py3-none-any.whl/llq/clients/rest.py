import aiohttp
from .base_client import BaseClient
from .exception import ClientException
from typing import Optional, Any, Dict


class RestClient(BaseClient):
    """
    A reusable asynchronous REST client extending the BaseClient.
    """

    def __init__(self, base_url: str, **kwargs):
        super().__init__(**kwargs)
        self.base_url = base_url.rstrip("/")
        self.session: Optional[aiohttp.ClientSession] = None

    async def connect(self):
        if not self.session:
            self.session = aiohttp.ClientSession(headers=self.headers)

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def request(self, method: str, endpoint: str, **kwargs) -> dict:
        if not self.session:
            raise ClientException("Client is not connected. Call 'connect()' first.")

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.log_request(method, url, **kwargs)

        @self.retry_request
        async def _make_request():
            async with self.session.request(method, url, **kwargs) as response:
                response.raise_for_status()
                data = await response.json()
                self.log_response(response.status, data)
                return data

        return await _make_request()

    async def get(self, endpoint: str, params: Optional[Dict] = None) -> dict:
        return await self.request("GET", endpoint, params=params)

    async def post(
        self, endpoint: str, data: Optional[Any] = None, json: Optional[Any] = None
    ) -> dict:
        return await self.request("POST", endpoint, data=data, json=json)

    async def put(
        self, endpoint: str, data: Optional[Any] = None, json: Optional[Any] = None
    ) -> dict:
        return await self.request("PUT", endpoint, data=data, json=json)

    async def delete(self, endpoint: str, params: Optional[Dict] = None) -> dict:
        return await self.request("DELETE", endpoint, params=params)
