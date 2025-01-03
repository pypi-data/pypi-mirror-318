import abc

from ... import errors

import logging  # isort:skip
_log = logging.getLogger(__name__)


class TrackerRuleBase(abc.ABC):
    @property
    def reference(self):
        """Short reference to the relevant rule on the tracker's website"""

    required_jobs = ()
    """..."""

    def __init__(self, tracker_jobs):
        self._tracker_jobs = tracker_jobs

    @property
    def tracker_jobs(self):
        """:class:`~.TrackerJobsBase` instance"""
        return self._tracker_jobs

    @property
    def release_name(self):
        """:class:`~.ReleaseName` instance"""
        return self._tracker_jobs.release_name

    @property
    def tracker(self):
        """:class:`~.TrackerBase` instance"""
        return self._tracker_jobs.tracker

    def check_if_possible(self, job_):
        _log.debug('RULE: %s finished', job_)
        if self._required_jobs_finished():
            self.check()

    def _required_jobs_finished(self):
        ok = True
        for job_name in self.required_jobs:
            job = getattr(self.tracker_jobs, job_name)
            if not job.is_finished:
                ok = False
            _log.debug('RULE CHECK: %r: %r -> %r', job.name, job.is_finished, ok)
        return ok

    @abc.abstractmethod
    def check(self):
        """
        ...
        """

class BannedGroup(TrackerRuleBase):

    required_jobs = (
        'release_name_job',
    )

    banned_groups = {}
    """:class:`set` of banned group names"""

    def is_group(self, group_name):
        """
        Return whether `group_name` is equal to the :attr:`~.ReleaseName.group` of
        :attr:`~.TrackerRuleBase.release_name`
        """
        return self.release_name.group.lower() == group_name.lower()

    def check(self):
        self.custom_check()

        # Case-insensitively match group name against `banned_groups`.
        for banned_group in self.banned_groups:
            _log.debug(f'if self.is_group({banned_group!r}): {self.is_group(banned_group)}')
            if self.is_group(banned_group):
                raise errors.BannedGroup(banned_group)

    def custom_check(self):
        """
        Match group name plus some other attributes (e.g. no encodes from a certain group)

        :raise RuleBroken: if the group is banned under specific conditions
        """
