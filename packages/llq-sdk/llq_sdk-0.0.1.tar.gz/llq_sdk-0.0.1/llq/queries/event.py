from sgqlc.operation import Operation
from sgqlc.types import Variable, Int
from llq.schema import (
    RootQuery,
    Event,
    DateQueryInput,
    OrderEnum,
    PostObjectsConnectionOrderbyEnum,
)
from llq.fragments import EventFragment
from llq.base_operation_builder import BaseOperationBuilder
from llq.type import Nodes
from llq.type.event import Event
from llq.base_response import BaseResponse
from dataclasses import dataclass


@dataclass
class EventByStartDateResponse(BaseResponse):
    events: Nodes[Event]

    @staticmethod
    def from_dict(data: dict) -> "EventByStartDateResponse":
        """
        Parse a dictionary response into an EventByStartDateResponse instance.
        """
        return EventByStartDateResponse(
            events=Nodes.from_dict(data.get("events", {}), Event.from_dict)
        )


class EventByStartDateQuery(BaseOperationBuilder):
    """
    A builder for event-related GraphQL queries.
    """

    def get(self, first: Int, start_date: DateQueryInput) -> Operation:
        """
        Build a GraphQL query to fetch the next events.

        :param first: The number of events to fetch.
        :param start_date: The starting date for the events.
        :return: An sgqlc Operation object representing the query.
        """
        op = Operation(RootQuery, name="get_next_event")

        events = op.events(
            first=first,
            where={
                "start_date_query": start_date,
                "order_by": {
                    "field": PostObjectsConnectionOrderbyEnum.DATE,
                    "order": OrderEnum.ASC,
                },
            },
        )

        nodes = events.nodes

        # Retrieve and attach the EventFragment from the registry
        event_frag = EventFragment().get()
        nodes.__fragment__(event_frag)

        return op

    @staticmethod
    def parse(data: dict) -> EventByStartDateResponse:
        return EventByStartDateResponse.from_dict(data)
