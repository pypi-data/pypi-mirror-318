from dataclasses import dataclass
from typing import Optional
from llq.type import Node, Nodes, MediaItem


@dataclass
class Organizer:
    uri: str
    title: str
    content: Optional[str]
    featured_image: Node[MediaItem]


@dataclass
class EventsCategory:
    name: str


@dataclass
class Venue:
    uri: str
    city: Optional[str]
    address: Optional[str]


@dataclass
class Event:
    uri: str
    title: str
    duration: Optional[int]
    start_date: str
    end_date: Optional[str]
    date: Optional[str]
    all_day: bool
    url: str
    link: Optional[str]
    organizers: Optional[Nodes[Organizer]]
    events_categories: Optional[Nodes[EventsCategory]]
    featured_image: Optional[Node[MediaItem]]
    venue: Optional[Venue]

    @staticmethod
    def from_dict(data: dict) -> "Event":
        return Event(
            uri=data["uri"],
            title=data["title"],
            duration=data.get("duration"),
            start_date=data["start_date"],
            end_date=data.get("end_date"),
            date=data.get("date"),
            all_day=data["all_day"],
            url=data["url"],
            link=data.get("link"),
            organizers=Nodes.from_dict(data.get("organizers", {}), Organizer)
            if data.get("organizers")
            else None,
            events_categories=Nodes.from_dict(
                data.get("events_categories", {}), EventsCategory
            )
            if data.get("events_categories")
            else None,
            featured_image=Node.from_dict(data.get("featured_image", {}), MediaItem)
            if data.get("featured_image")
            else None,
            venue=Venue(
                uri=data["venue"]["uri"],
                city=data["venue"].get("city"),
                address=data["venue"].get("address"),
            )
            if data.get("venue")
            else None,
        )


__all__ = ["Event", "Venue", "EventsCategory", "Organizer"]
