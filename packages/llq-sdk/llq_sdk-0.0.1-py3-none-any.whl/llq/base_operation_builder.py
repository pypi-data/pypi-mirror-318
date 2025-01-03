from abc import ABC, abstractmethod
from typing import Dict
from sgqlc.operation import Operation
from llq.base_response import BaseResponse


class BaseOperationBuilder(ABC):
    """
    Abstract base class for all Query/Mutation Builders.
    """

    @abstractmethod
    def get(self, **kwargs) -> Operation:
        """
        Build a GraphQL query or mutation.

        :param kwargs: Parameters required to build the query or mutation.
        :return: An sgqlc Operation object representing the query or mutation.
        """
        pass

    @staticmethod
    @abstractmethod
    def parse(data: Dict) -> "BaseResponse":
        """
        Parse the GraphQL response data into a typed BaseResponse object.

        :param data: A dictionary representing the GraphQL response.
        :return: A BaseResponse instance.
        """
        pass
