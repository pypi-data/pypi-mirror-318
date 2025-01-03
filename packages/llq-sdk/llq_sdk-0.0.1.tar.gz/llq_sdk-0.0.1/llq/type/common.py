from dataclasses import dataclass
from typing import Optional


@dataclass
class MediaItem:
    uri: str
    source_url: Optional[str]
    alt_text: Optional[str]
    database_id: int
    media_item_url: str
