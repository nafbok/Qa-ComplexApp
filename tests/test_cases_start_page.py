"""Stores tests related to Start page and Main Page"""

import pytest

from conftest import BaseTest
from pages.utils import User


class TestStartPage(BaseTest):

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, random_user):
        """Registered user and return data"""
        # Fill fields with provided  values
        main_page = start_page.register_user(random_user)
        # Logout
        main_page.header.logout()
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
