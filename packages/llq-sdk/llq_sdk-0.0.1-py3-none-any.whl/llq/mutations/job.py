from sgqlc.operation import Operation
from llq.schema import (
    RootMutation,
    ID,
    JobContractkindsInput,
    JobJobmodesInput,
    JobOccupationkindsInput,
    PostStatusEnum,
)
from llq.base_operation_builder import BaseOperationBuilder
from llq.fragments import JobFragment
from typing import Optional
from llq.type.job import Job
from dataclasses import dataclass

@dataclass
class UpdateJobMutationResponse:
    job: Optional[Job]

    @staticmethod
    def from_dict(data: dict) -> "UpdateJobMutationResponse":
        """
        Parse a dictionary into an UpdateJobMutationResponse instance.
        """
        return UpdateJobMutationResponse(
            job=Job.from_dict(data.get("job", {})) if data.get("job") else None
        )


class UpdateJobMutation(BaseOperationBuilder):
    """
    A builder for job update-related GraphQL mutation.
    """

    def get(
        self,
        job_id: ID,
        status: PostStatusEnum,
        contract_kinds: JobContractkindsInput,
        job_modes: JobJobmodesInput,
        occupation_kinds: JobOccupationkindsInput,
    ) -> Operation:
        """
        Build a GraphQL mutation to update a job.

        :param job_id: The ID of the job to update.
        :param status: The status of the job.
        :param contract_kinds: A dictionary defining contract kinds to update.
        :param job_modes: A dictionary defining job modes to update.
        :param occupation_kinds: A dictionary defining occupation kinds to update.
        :return: An sgqlc Operation object representing the mutation.
        """
        op = Operation(RootMutation, name="update_job_mutation")
        job = op.update_job(
            input={
                "id": job_id,
                "status": status,
                "ignore_edit_lock": True,
                "contractkinds": contract_kinds,
                "jobmodes": job_modes,
                "occupationkinds": occupation_kinds,
            }
        ).job
        job.__fragment__(JobFragment().get())
        return op

    @staticmethod
    def parse(data: dict) -> UpdateJobMutationResponse:
        return UpdateJobMutationResponse.from_dict(data)


@dataclass
class UpdateJobStatusMutationResponse:
    job: Optional[Job]

    @staticmethod
    def from_dict(data: dict) -> "UpdateJobStatusMutationResponse":
        """
        Parse a dictionary into an UpdateJobStatusMutationResponse instance.
        """
        return UpdateJobStatusMutationResponse(
            job=Job.from_dict(data.get("job", {})) if data.get("job") else None
        )


class UpdateJobStatusMutation(BaseOperationBuilder):
    """
    A Builder for job update status GraphQL mutation
    """

    def get(self, id: ID, status: PostStatusEnum) -> Operation:
        """
        Build a GraphQL mutation to update a job.

        :param job_id: The ID of the job to update.
        :param status: The status of the job.
        :return: An sgqlc Operation object representing the mutation.
        """
        op = Operation(RootMutation, name="update_job_mutation")
        job = op.update_job(
            input={
                "id": job_id,
                "status": status,
                "ignore_edit_lock": True,
            }
        ).job
        job.__fragment__(JobFragment().get())
        return op

    @staticmethod
    def parse(data: dict) -> UpdateJobStatusMutationResponse:
        return UpdateJobStatusMutationResponse.from_dict(data)


@dataclass
class DeleteJobMutationResponse:
    job: Optional[Job]

    @staticmethod
    def from_dict(data: dict) -> "DeleteJobMutationResponse":
        """
        Parse a dictionary into a DeleteJobMutationResponse instance.
        """
        return DeleteJobMutationResponse(
            job=Job.from_dict(data.get("job", {})) if data.get("job") else None
        )


class DeleteJobMutation(BaseOperationBuilder):
    """
    A Builder for job update status GraphQL mutation
    """

    def get(self, id: ID) -> Operation:
        """
        Build a GraphQL mutation to update a job.

        :param job_id: The ID of the job to update.
        :return: An sgqlc Operation object representing the mutation.
        """

        op = Operation(RootMutation, name="update_job_mutation")
        job = op.delete_job(
            input={
                "id": job_id,
                "ignore_edit_lock": True,
                "force_delete": True,
            }
        ).job
        job.__fragment__(JobFragment().get())

        return op

    @staticmethod
    def parse(data: dict) -> DeleteJobMutationResponse:
        return DeleteJobMutationResponse.from_dict(data)
