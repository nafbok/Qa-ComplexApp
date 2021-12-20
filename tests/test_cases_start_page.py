"""Stores tests related to Start page and Main Page"""

import pytest
from selenium.webdriver.chrome import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage(BaseTest):

    @pytest.fixture(scope='function')
    def driver(self):
        """Create and return driver, close after test"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
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

    def test_invalid_login(self, start_page, random_user):
        """Test login with invalid values"""
        # Fill fields with invalid values
        start_page.login(random_user)

        # Verify error message
        start_page.verify_incorrect_login()

    def test_empty_fields_value(self, start_page):
        """Test login with empty values"""
        start_page.login(User())

        # Verify error message
        start_page.verify_incorrect_login()

    def test_login_user(self, start_page, random_user):
        """Test  sign up new user successfully:"""
        # Fill fields with provided  values
        main_page = start_page.register_user(random_user)

        # Verify register message
        main_page.verify_welcome_message(random_user.username)

    def test_success_login(self, start_page, registered_user):
        """
        - Pre-conditions:
            - Open start page
            - Register user
        - Steps:
            - Login as registered user
            - Verify welcome message
        """
        # Login as registered user
        main_page = start_page.login(registered_user)
        #  Verify welcome message
        main_page.verify_welcome_message(registered_user.username)
