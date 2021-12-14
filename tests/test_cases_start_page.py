"""Stores tests related to Start page and Main Page"""

import pytest
from selenium.webdriver.chrome import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage(BaseTest):

    @pytest.fixture(scope='function')
    def driver(self):
        """Create and return driver, close after test"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return start page object"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def registered_user(self, start_page):
        """Registered user and return data"""
        temp_username = self.random_username()
        temp_email = self.random_email()
        temp_password = self.random_password()
        # Fill fields with provided  values
        main_page = start_page.register_user(temp_username, temp_email, temp_password)
        # Logout
        main_page.logout()
        return temp_username, temp_email, temp_password

    def test_start_page(self, start_page):
        """Test login with invalid values"""
        # Fill fields with invalid values
        start_page.login("JNnjndslv", "qwerrtr")
        self.log.info("Fields are filled with invalid values")

        # Verify error message
        start_page.verify_incorrect_login()
        self.log.info("Error message to expected")

    def test_empty_fields_value(self, start_page):
        """Test login with empty values"""
        start_page.login("", "")
        self.log.info("Fields are filled with invalid values")

        # Verify error message
        start_page.verify_incorrect_login()
        self.log.info("Error message to expected")

    def test_login_user(self, start_page):
        """Test  sign up new user successfully:"""
        temp_username = self.random_username()
        temp_email = self.random_email()
        temp_password = self.random_password()

        # Fill fields with provided  values
        main_page = start_page.register_user(temp_username, temp_email, temp_password)
        self.log.debug("Fields were filled")

        # Verify register message
        main_page.verify_welcome_message(temp_username)
        self.log.debug("Registration was success and verified")

    def test_success_login(self, start_page, registered_user):
        """
        - Pre-conditions:
            - Open start page
            - Register user
        - Steps:
            - Login as registered user
            - Verify welcome message
        """
        # Init user data from fixture
        temp_username, _, temp_password = registered_user
        # Login as registered user
        main_page = start_page.login(temp_username, temp_password)
        self.log.info("Logged as '%s'", temp_username)
        #  Verify welcome message
        main_page.verify_welcome_message(temp_username)
        self.log.info("Welcome message was verified")
