"""Conftest"""
import logging

import pytest
from selenium.webdriver.chrome import webdriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


def pytest_runtest_setup(item):
    # item.cls.logger = logging.getLogger(".".join((item.module.__name__, item.cls.__name__, item.name)))
    item.cls.logger = logging.getLogger(item.name)


class BaseTest:
    """Set some fields to provide autocomplete for dynamically added fields"""
    log = logging.getLogger(__name__)

    @pytest.fixture(scope='function')
    def driver(self):
        """Create and return driver, close after test"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        driver.maximize_window()
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        """Creates values object for random user"""
        user = User()
        user.fill_properties()
        return user

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, random_user):
        """Registered user and return data"""
        # Fill fields with provided  values
        main_page = start_page.register_user(random_user)
        # Logout
        main_page.logout()
        return random_user

    def title_post(self):
        """Title for new post"""
        title_post = "Test"
        return title_post

    def body_post(self):
        """Body content for new post"""
        body_post = "Vary long smart article"
        return body_post
