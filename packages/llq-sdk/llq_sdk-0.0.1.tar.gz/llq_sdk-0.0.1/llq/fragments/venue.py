from sgqlc.operation import Fragment
from sgqlc.types import Type as SGQLCType
from typing import List
from llq.schema import Venue
from llq.fragments.fragment_builder import FragmentBuilder


class VenueFragment(FragmentBuilder[Venue]):
    def get(self) -> Fragment:
        # Venue Fragment
        fragment = Fragment(Venue, "VenueFragment")
        fragment.uri()
        fragment.city()
        fragment.address()

        return fragment
