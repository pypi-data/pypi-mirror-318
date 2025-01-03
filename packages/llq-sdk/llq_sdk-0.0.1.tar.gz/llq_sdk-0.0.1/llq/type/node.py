from dataclasses import dataclass, is_dataclass
from typing import TypeVar, Generic, List, Type, Union

T = TypeVar("T")


def _parse_dict(data: Union[dict, List[dict]], item_type: Type[T]) -> Union[T, List[T]]:
    """
    Parse a dictionary or list of dictionaries into an instance or list of instances of type T.
    If `item_type` is callable (e.g., a custom parsing function), it will use that directly.
    """

    def is_callable_type(item_type):
        return callable(item_type) and not is_dataclass(item_type)

    if isinstance(data, list):
        return [
            item_type(item)
            if is_callable_type(item_type)
            else item_type(
                **{
                    key: value
                    for key, value in item.items()
                    if key in item_type.__annotations__
                }
            )
            for item in data
        ]
    return (
        item_type(data)
        if is_callable_type(item_type)
        else item_type(
            **{
                key: value
                for key, value in data.items()
                if key in item_type.__annotations__
            }
        )
    )


@dataclass
class Node(Generic[T]):
    """
    Class to represent a single node.
    """

    node: T

    @staticmethod
    def from_dict(data: dict, item_type: Type[T]) -> "Node[T]":
        """
        Parse a dictionary into a single Node instance of type T.
        """
        return Node(node=_parse_dict(data.get("node", {}), item_type))


@dataclass
class Nodes(Generic[T]):
    """
    Class to represent multiple nodes.
    """

    nodes: List[T]

    @staticmethod
    def from_dict(data: dict, item_type: Type[T]) -> "Nodes[T]":
        """
        Parse a dictionary into a Nodes instance containing a list of items of type T.
        """
        return Nodes(nodes=_parse_dict(data.get("nodes", []), item_type))
