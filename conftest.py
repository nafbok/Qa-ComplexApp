"""Conftest"""
import logging


def pytest_runtest_setup(item):
    # item.cls.logger = logging.getLogger(".".join((item.module.__name__, item.cls.__name__, item.name)))
    item.cls.logger = logging.getLogger(item.name)


class BaseTest:
    """Set some fields to provide autocomplete for dynamically added fields"""
    log = logging.getLogger(__name__)


    def title_post(self):
        """Title for new post"""
        title_post = "Test"
        return title_post

    def body_post(self):
        """Body content for new post"""
        body_post = "Vary long smart article"
        return body_post
