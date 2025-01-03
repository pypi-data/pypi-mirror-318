from sgqlc.operation import Fragment
from sgqlc.types import Type as SGQLCType
from typing import List
from llq.schema import Event, EventsCategory, MediaItem, Venue
from llq.fragments.fragment_builder import FragmentBuilder
from llq.fragments.organizer import OrganizerFragment
from llq.fragments.media_item import MediaItemFragment
from llq.fragments.venue import VenueFragment


class EventFragment(FragmentBuilder[Event]):
    def get(self) -> Fragment:
        # Event Fragment
        fragment = Fragment(Event, "EventFragment")
        fragment.uri()
        fragment.title()
        fragment.duration()
        fragment.start_date()
        fragment.end_date()
        fragment.date()
        fragment.all_day()
        fragment.url()
        fragment.link()

        # Nested Fragments
        organizers = fragment.organizers
        organizer_nodes = organizers.nodes
        organizer_frag = OrganizerFragment().get()
        organizer_nodes.__fragment__(organizer_frag)

        # EventsCategories Fragment
        category_frag = self.events_category_fragment()
        events_categories = fragment.events_categories
        category_nodes = events_categories.nodes
        category_nodes.__fragment__(category_frag)

        # FeaturedImage Fragment
        featured_image = fragment.featured_image
        image_node = featured_image.node
        media_item_frag = MediaItemFragment().get()
        image_node.__fragment__(media_item_frag)

        # Venue Fragment
        venue = fragment.venue
        venue_frag = VenueFragment().get()
        venue.__fragment__(venue_frag)

        return fragment

    def events_category_fragment(self) -> Fragment:
        category_frag = Fragment(EventsCategory, "EventsCategoryFragment")
        category_frag.name()
        return category_frag
