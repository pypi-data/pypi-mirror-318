from sgqlc.operation import Fragment
from sgqlc.types import Type as SGQLCType
from typing import List
from llq.schema import Event, EventsCategory, MediaItem, Venue, PartnerAcf
from llq.fragments.fragment_builder import FragmentBuilder
from llq.fragments.media_item import MediaItemFragment


class PartnerFragment(FragmentBuilder[PartnerAcf]):
    def get(self) -> Fragment:
        # Partner (ACF) Fragment
        fragment = Fragment(PartnerAcf, "PartnerFragment")
        fragment.partner_name()
        fragment.partner_description()
        fragment.partner_website_link()
        fragment.technologie()
        fragment.type_of_company()

        # Nested Fragments

        image_node = fragment.partner_logo().node
        media_item_frag = MediaItemFragment().get()
        image_node.__fragment__(media_item_frag)

        return fragment
