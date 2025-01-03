from sgqlc.operation import Fragment
from llq.schema import JobAcf, Job, Occupationkind, Jobmode, ContractKind
from llq.fragments.fragment_builder import FragmentBuilder
from llq.fragments.media_item import MediaItemFragment


class JobFragment(FragmentBuilder[JobAcf]):
    def get(self) -> Fragment:
        """
        Defines the JobFragment.

        :return: An sgqlc Fragment object.
        """
        fragment = Fragment(Job, "JobFragment")
        fragment.uri()

        # Nested Fragments
        job_acf = fragment.job_acf()
        job_acf.__fragment__(self._job_acf_fragment())

        image_node = fragment.compagny_logo().node
        media_item_frag = MediaItemFragment().get()
        image_node.__fragment__(media_item_frag)

        occupation_kind_nodes = fragment.occupation_kinds().nodes
        occupation_kind_nodes.__fragment__(self.occupation_kind_fragment())

        job_mode_nodes = fragment.job_modes().nodes
        job_mode_nodes.__fragment__(self.job_mode_fragment())

        contract_kind_nodes = fragment.contract_kinds().nodes
        contract_kind_nodes.__fragment__(self.contract_kind_fragment())

        return fragment

    def _job_acf_fragment(self) -> Fragment:
        fragment = Fragment(JobAcf, "JobAcfFragment")
        fragment.job_title()
        fragment.compagny_name()
        fragment.localization()
        fragment.apply_link()

        return fragment

    def occupation_kind_fragment(self) -> Fragment:
        fragment = Fragment(Occupationkind, "OccupationKindFragment")
        fragment.uri()
        fragment.name()
        return fragment

    def job_mode_fragment(self) -> Fragment:
        fragment = Fragment(Jobmode, "JobModeFragment")
        fragment.uri()
        fragment.name()
        return fragment

    def contract_kind_fragment(self) -> Fragment:
        fragment = Fragment(ContractKind, "ContractKindFragment")
        fragment.uri()
        fragment.name()
        return fragment
