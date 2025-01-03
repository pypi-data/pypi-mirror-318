import logging
import backoff
from typing import Optional, Dict


class BaseClient:
    """
    A base class for shared functionality between GraphQL and REST clients.
    """

    def __init__(
        self,
        headers: Optional[Dict[str, str]] = None,
        retry_connect=None,
        retry_request=None,
    ):
        """
        Initialize the base client with common attributes.

        :param headers: Optional headers for HTTP requests.
        :param retry_connect: Custom retry logic for connection retries.
        :param retry_request: Custom retry logic for request retries.
        """
        self.headers = headers or {}
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.retry_connect = retry_connect or backoff.on_exception(
            backoff.expo, Exception, max_value=60
        )
        self.retry_request = retry_request or backoff.on_exception(
            backoff.expo, Exception, max_tries=5
        )

    def log_request(self, method: str, url: str, **kwargs):
        """
        Log the details of an HTTP request.
        """
        self.logger.debug(f"Requesting {method.upper()} {url} with {kwargs}")

    def log_response(self, status: int, response: str):
        """
        Log the details of an HTTP response.
        """
        self.logger.debug(f"Response status: {status}, response: {response}")
