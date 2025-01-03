from sgqlc.operation import Operation
from sgqlc.types import Variable, Int
from dataclasses import dataclass
from typing import Optional
from llq.schema import RootQuery
from llq.fragments import EventFragment, JobFragment
from llq.base_operation_builder import BaseOperationBuilder
from llq.base_response import BaseResponse
from llq.type.job import JobAcf, JobMode, OccupationKind, MediaItem, ContractKind
from llq.type import Nodes


@dataclass
class TermsResponse(BaseResponse):
    occupation_kinds: Nodes[OccupationKind]
    job_modes: Nodes[JobMode]
    contract_kinds: Nodes[ContractKind]

    @staticmethod
    def from_dict(data: dict) -> "TermsResponse":
        """
        Parse a dictionary into a TermsResponse instance.
        """
        return TermsResponse(
            occupation_kinds=Nodes.from_dict(
                data.get("occupationkinds", {}), OccupationKind
            ),
            job_modes=Nodes.from_dict(data.get("jobmodes", {}), JobMode),
            contract_kinds=Nodes.from_dict(data.get("contractkinds", {}), ContractKind),
        )


class CustomTermsQuery(BaseOperationBuilder):
    """
    A builder for job custom term GraphQL queries.
    """

    def get(
        self,
        first: Optional[Int] = 1,
    ) -> Operation:
        """
        Build a GraphQL query to fetch contract-kinds.

        :param contract_kind_count: The number of contract_kind to fetch.
        :param job_mode_count: The number of job_mode to fetch.
        :param occupation_kind_count: The number of occupation_kind to fetch.
        :return: An sgqlc Operation object representing the query.
        """
        op = Operation(RootQuery, name="get_job_custom_terms")

        contract_kinds = op.contractkinds(first=first)

        modes = op.jobmodes(first=first)

        occupation_kinds = op.occupationkinds(first=first)

        contract_kinds_nodes = contract_kinds.nodes.__fragment__(
            JobFragment().contract_kind_fragment()
        )

        job_modes_nodes = modes.nodes.__fragment__(JobFragment().job_mode_fragment())

        occupation_kinds_nodes = occupation_kinds.nodes.__fragment__(
            JobFragment().occupation_kind_fragment()
        )

        return op

    @staticmethod
    def parse(data: dict) -> TermsResponse:
        return TermsResponse.from_dict(data)
