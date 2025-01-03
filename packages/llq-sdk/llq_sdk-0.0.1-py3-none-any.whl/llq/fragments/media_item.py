from sgqlc.operation import Fragment
from llq.schema import MediaItem
from llq.fragments.fragment_builder import FragmentBuilder


class MediaItemFragment(FragmentBuilder[MediaItem]):
    def get(self) -> Fragment:
        """
        Defines the MediaItemFragment.

        :return: An sgqlc Fragment object.
        """
        fragment = Fragment(MediaItem, "MediaItemFragment")
        fragment.uri()
        fragment.source_url()
        fragment.alt_text()
        fragment.database_id()
        fragment.media_item_url()
        return fragment
