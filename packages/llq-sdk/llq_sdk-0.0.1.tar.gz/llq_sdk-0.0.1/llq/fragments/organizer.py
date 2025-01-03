from sgqlc.operation import Fragment
from sgqlc.types import Type as SGQLCType
from typing import List
from llq.schema import Organizer, MediaItem
from llq.fragments.fragment_builder import FragmentBuilder
from llq.fragments.media_item import MediaItemFragment


class OrganizerFragment(FragmentBuilder[Organizer]):
    def get(self) -> Fragment:
        # Organizer Fragment
        fragment = Fragment(Organizer, "OrganizerFragment")
        fragment.uri()
        fragment.title()
        fragment.content()

        # Nested MediaItem Fragment
        media_item_frag = MediaItemFragment().get()
        image = fragment.featured_image
        image_node = image.node
        image_node.__fragment__(media_item_frag)

        return fragment
