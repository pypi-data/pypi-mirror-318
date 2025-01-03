from abc import ABC, abstractmethod


class BaseResponse(ABC):
    """
    Abstract base class for all response objects.
    """

    @staticmethod
    @abstractmethod
    def from_dict(data: dict) -> "BaseResponse":
        """
        Parse a dictionary into an instance of the response class.

        :param data: A dictionary representing the response data.
        :return: An instance of the implementing response class.
        """
        pass
