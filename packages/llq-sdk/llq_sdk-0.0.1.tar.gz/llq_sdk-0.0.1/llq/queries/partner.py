from sgqlc.operation import Operation, Fragment
from sgqlc.types import Variable, Int
from llq.schema import (
    RootQuery,
    Partner,
    ID,
)
from llq.fragments import PartnerFragment
from llq.base_operation_builder import BaseOperationBuilder
from dataclasses import dataclass
from typing import Any
from llq.base_response import BaseResponse
from llq.type import Nodes, Node, MediaItem
from llq.type.partner import PartnerAcf, Partner as PartnerType


@dataclass
class PartnersResponse(BaseResponse):
    partners: Nodes[PartnerType]

    @staticmethod
    def from_dict(data: dict) -> "PartnersResponse":
        """
        Parse a dictionary into a PartnersResponse instance.
        """
        return PartnersResponse(
            partners=Nodes.from_dict(data.get("partners", {}), PartnerType.from_dict)
        )


@dataclass
class PartnerByIdResponse(BaseResponse):
    partner: PartnerType

    @staticmethod
    def from_dict(data: dict) -> "PartnerByIdResponse":
        """
        Parse a dictionary into a PartnerByIdResponse instance.
        """
        return PartnerByIdResponse(
            partner=PartnerType.from_dict(data.get("partner", {}))
        )


class PartnerByIdQuery(BaseOperationBuilder):
    """
    A builder for partner-related GraphQL queries.
    """

    def get(self, id: ID) -> Operation:
        """
        Build a GraphQL query to fetch a partner by id.

        :param id: The ID of partner.
        :return: An sgqlc Operation object representing the query.
        """
        op = Operation(RootQuery, name="get_partner_by_id")

        partner = op.partner(id=id)
        partner.id()

        partner_acf = partner.partner_acf
        partner_frag = PartnerFragment().get()
        partner_acf.__fragment__(partner_frag)

        return op

    @staticmethod
    def parse(data: dict) -> PartnerByIdResponse:
        return PartnerByIdResponse.from_dict(data)


class PartnersQuery(BaseOperationBuilder):
    """
    A builder for partners-related GraphQL queries.
    """

    def get(self, first: Int) -> Operation:
        """
        Build a GraphQL query to fetch all partners.

        :param first: The number of partners to fetch.
        :return: An sgqlc Operation object representing the query.
        """

        op = Operation(RootQuery, name="get_partners")

        partners = op.partners(first=first)

        nodes = partners.nodes
        nodes.id()
        partner_node_frag = Fragment(Partner, "PartnerNodeFragment")
        partner_acf = partner_node_frag.partner_acf

        partner_acf_frag = PartnerFragment().get()
        partner_acf.__fragment__(partner_acf_frag)

        if partner_node_frag:
            nodes.__fragment__(partner_node_frag)

        return op

    @staticmethod
    def parse(data: dict) -> PartnersResponse:
        return PartnersResponse.from_dict(data)
