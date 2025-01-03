from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from sgqlc.operation import Fragment
from sgqlc.types import Type as SGQLCType

T = TypeVar("T", bound=SGQLCType)


class FragmentBuilder(ABC, Generic[T]):
    """
    Abstract base class for building GraphQL fragment.
    """

    @abstractmethod
    def get(self) -> Fragment:
        """
        Build and return a of GraphQL fragment.

        :return: A sgqlc Fragment object.
        """
        pass
