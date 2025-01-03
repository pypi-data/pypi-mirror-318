from uuid_utils import uuid7
from dataclasses import dataclass, asdict
from typing import Any, Dict
from llq.clients import RestClient
from llq.schema import PostStatusEnum
from llq.type.job import CreateJobAcf


async def post_job(job: CreateJobAcf, client: RestClient) -> Dict:
    job_post = {
        "title": job.job_title_,
        "status": PostStatusEnum.DRAFT.lower(),
        "slug": str(uuid7()),
        "acf": asdict(job),
    }
    return await client.post("/job", json=job_post)
