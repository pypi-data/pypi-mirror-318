from dataclasses import dataclass
from typing import Optional
from llq.type import Node, MediaItem


@dataclass
class PartnerAcf:
    partner_name: str
    partner_description: str
    partner_website_link: str
    technologie: list[str]
    type_of_company: list[str]
    partner_logo: Optional[Node[MediaItem]]


@dataclass
class Partner:
    id: str
    partner_acf: PartnerAcf

    @staticmethod
    def from_dict(data: dict) -> "Partner":
        partner_acf = PartnerAcf(
            partner_name=data["partner_acf"]["partner_name"],
            partner_description=data["partner_acf"]["partner_description"],
            partner_website_link=data["partner_acf"]["partner_website_link"],
            technologie=data["partner_acf"]["technologie"],
            type_of_company=data["partner_acf"]["type_of_company"],
            partner_logo=Node.from_dict(
                data["partner_acf"].get("partner_logo", {}), MediaItem
            )
            if data["partner_acf"].get("partner_logo")
            else None,
        )
        return Partner(id=data["id"], partner_acf=partner_acf)


__all__ = ["PartnerAcf", "Partner"]
