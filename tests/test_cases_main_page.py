"""Stores tests related to Start page and Main Page"""

import pytest
from selenium.webdriver.chrome import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestMainPage(BaseTest):

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

    def test_refresh_first_page(self, start_page, registered_user):
        """Refresh first page:
            - Log in user
            - Find the logo "Complex app for testing - QA" 
            - Click the logo
            - Check refresh page successful   
        """
        # Login as registered user
        main_page = start_page.login(registered_user)

        main_page.refresh_main_page()
        # verify refresh page successful
        main_page.verify_welcome_message(registered_user.username)

    def test_transition_to_search_bar(self, start_page, registered_user):
        """Transition to the search bar:
            - Log in user
            - Find search icon
            - Click search icon
            - Check search bar is opened successful   
        """
        # Login as registered user
        main_page = start_page.login(registered_user)

        # find and click search icon
        main_page.transition_to_search_bar()

        # verify search bar is opened successful
        main_page.verify_search_bar_opened()


    def test_transition_to_chat_form(self, start_page, registered_user):
        """Transition to the char form:
            - Find chat icon
            - Click chat icon
            - Check chat form is opened successful   
        """
        # Login as registered user
        main_page = start_page.login(registered_user)

        # find and click chat icon
        main_page.transition_to_chat_form()

        # verify chat form is opened successful
        main_page.verify_chat_form_opened()

    def test_transition_to_my_profile(self, start_page, registered_user):
        """Transition to my profile page:
            - Log in user
            - Find my profile icon
            - Click my profile icon
            - Check my profile page is opened successful   
        """
        # Login as registered user
        main_page = start_page.login(registered_user)

        main_page.transition_to_my_profile()
        # verify chat form is opened successful
        my_profile = main_page.transition_to_my_profile()
        my_profile.my_profile_is_opened()

    def test_transition_to_create_post(self, start_page, registered_user):
        """Transition to my profile page:
            - Log in user
            - Find Create post button
            - Click Create post button
            - Check Create post is opened successful   
        """
        # Login as registered user
        main_page = start_page.login(registered_user)

        # transition to create post
        main_page.transition_to_create_post_page()

        # verify create post is opened successful
        create_post = main_page.transition_to_create_post_page()
        create_post.create_post_is_opened()
