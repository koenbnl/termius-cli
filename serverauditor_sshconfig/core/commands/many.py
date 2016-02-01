# -*- coding: utf-8 -*-
"""Module with base commands for list entries."""
import logging
# pylint: disable=import-error
from cliff.lister import Lister
from ..settings import Config
from ..storage import ApplicationStorage
from .mixins import GetRelationMixin, PrepareResultMixin


# pylint: disable=too-few-public-methods, abstract-method
class ListCommand(GetRelationMixin, PrepareResultMixin, Lister):
    """Command for listing storage content."""

    log = logging.getLogger(__name__)

    def __init__(self, app, app_args, cmd_name=None):
        """Create new command instance."""
        super(ListCommand, self).__init__(app, app_args, cmd_name)
        self.config = Config(self.app.NAME)
        self.storage = ApplicationStorage(self.app.NAME)

    def get_parser(self, prog_name):
        """Create command line argument parser.

        Use it to add extra options to argument parser.
        """
        parser = super(ListCommand, self).get_parser(prog_name)
        parser.add_argument('--log-file', help='Path to log file.')
        return parser