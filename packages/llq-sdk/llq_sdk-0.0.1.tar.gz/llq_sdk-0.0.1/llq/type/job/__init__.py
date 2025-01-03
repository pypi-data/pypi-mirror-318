from dataclasses import dataclass
from llq.type import Node, Nodes, MediaItem
from typing import Optional


@dataclass
class JobAcf:
    job_title: str
    compagny_name: str
    localization: str
    apply_link: str


@dataclass
class OccupationKind:
    uri: str
    name: str


@dataclass
class JobMode:
    uri: str
    name: str


@dataclass
class ContractKind:
    uri: str
    name: str


@dataclass
class Job:
    uri: str
    job_acf: Optional[JobAcf]
    compagny_logo: Optional[Node[MediaItem]]
    occupation_kinds: Optional[Nodes[OccupationKind]]
    job_modes: Optional[Nodes[JobMode]]
    contract_kinds: Optional[Nodes[ContractKind]]

    @staticmethod
    def from_dict(data: dict) -> "Job":
        """
        Parse a dictionary into a Job instance.
        """
        return Job(
            uri=data["uri"],
            job_acf=JobAcf(
                job_title=data["job_acf"]["job_title"],
                compagny_name=data["job_acf"]["compagny_name"],
                localization=data["job_acf"]["localization"],
                apply_link=data["job_acf"]["apply_link"],
            )
            if data.get("job_acf")
            else None,
            compagny_logo=Node.from_dict(data.get("compagny_logo", {}), MediaItem)
            if data.get("compagny_logo")
            else None,
            occupation_kinds=Nodes.from_dict(
                data.get("occupationkinds", {}), OccupationKind
            )
            if data.get("occupationkinds")
            else None,
            job_modes=Nodes.from_dict(data.get("jobmodes", {}), JobMode)
            if data.get("jobmodes")
            else None,
            contract_kinds=Nodes.from_dict(data.get("contractkinds", {}), ContractKind)
            if data.get("contractkinds")
            else None,
        )


@dataclass
class CreateJobAcf:
    job_title_: str
    job_description_: str
    job_localization_: str
    job_type_of_contract_: list[str]
    job_type_of_post_: list[str]
    job_presence_: list[str]
    job_compagny_name_: str
    job_compagny_logo: int
    job_contact_email: Optional[str]
    job_apply_link: Optional[str]


__all__ = ["JobAcf", "OccupationKind", "JobMode", "ContractKind", "Job", "CreateJobAcf"]
