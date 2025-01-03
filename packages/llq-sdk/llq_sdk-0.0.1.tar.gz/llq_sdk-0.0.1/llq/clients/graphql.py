from gql import Client as GqlClient, gql
from gql.transport.aiohttp import AIOHTTPTransport
from sgqlc.operation import Operation
from typing import Optional
from .base_client import BaseClient
from .exception import ClientException
import inflection


def to_snake_case(data):
    """
    Recursively converts dictionary keys to snake case.
    """
    if isinstance(data, dict):
        return {
            inflection.underscore(key): to_snake_case(value)
            for key, value in data.items()
        }
    elif isinstance(data, list):
        return [to_snake_case(item) for item in data]
    return data


class GraphQLClient(BaseClient):
    """
    A reusable asynchronous GraphQL client extending the BaseClient.
    """

    def __init__(self, endpoint_url: str, **kwargs):
        super().__init__(**kwargs)
        self.transport = AIOHTTPTransport(url=endpoint_url, headers=self.headers)
        self.client = GqlClient(transport=self.transport)
        self.session = None

    async def connect(self):
        self.session = await self.client.connect_async(reconnecting=True)

    async def close(self):
        if self.session:
            await self.client.close_async()

    async def execute(
        self, operation: Operation, variables: Optional[dict] = None
    ) -> dict:
        if not self.session:
            raise ClientException("Client is not connected. Call 'connect()' first.")

        gql_operation = gql(str(operation))
        response = await self.session.execute(gql_operation, variable_values=variables)
        return to_snake_case(response)
