"""Stores tests related to Start page and Main Page"""
from time import sleep

from tests.test_cases_start_page import TestStartPage


class TestMainPage(TestStartPage):

    def test_refresh_first_page(self, start_page, registered_user):
        """Refresh first page:
            - Log in user
            - Find the logo "Complex app for testing - QA" 
            - Click the logo
            - Check refresh page successful   
        """
        # Init user data from fixture
        temp_username, _, temp_password = registered_user

        # Login as registered user
        main_page = start_page.login(temp_username, temp_password)
        self.log.info("Logged as '%s'", temp_username)

        main_page.refresh_main_page()
        # verify refresh page successful
        main_page.verify_welcome_message(temp_username)
        self.log.info("Welcome message was verified")

    def test_transition_to_search_bar(self, start_page, registered_user):
        """Transition to the search bar:
            - Log in user
            - Find search icon
            - Click search icon
            - Check search bar is opened successful   
        """
        # Init user data from fixture
        temp_username, _, temp_password = registered_user

        # Login as registered user
        main_page = start_page.login(temp_username, temp_password)
        self.log.info("Logged as '%s'", temp_username)

        # find and click search icon
        main_page.transition_to_search_bar()
        sleep(3)

        # verify search bar is opened successful
        main_page.verify_search_bar_opened()
        self.log.debug("Search bar was opened")
        sleep(3)

    def test_transition_to_chat_form(self, start_page, registered_user):
        """Transition to the char form:
            - Find chat icon
            - Click chat icon
            - Check chat form is opened successful   
        """
        # Init user data from fixture
        temp_username, _, temp_password = registered_user

        # Login as registered user
        main_page = start_page.login(temp_username, temp_password)
        self.log.info("Logged as '%s'", temp_username)

        # find and click chat icon
        main_page.transition_to_chat_form()
        sleep(2)

        # verify chat form is opened successful
        main_page.verify_chat_form_opened()
        self.log.debug("Chat form is opened")
        sleep(2)

    def test_transition_to_my_profile(self, start_page, registered_user):
        """Transition to my profile page:
            - Log in user
            - Find my profile icon
            - Click my profile icon
            - Check my profile page is opened successful   
        """
        # Init user data from fixture
        temp_username, _, temp_password = registered_user

        # Login as registered user
        main_page = start_page.login(temp_username, temp_password)
        self.log.info("Logged as '%s'", temp_username)

        main_page.transition_to_my_profile()
        # verify chat form is opened successful
        my_profile = main_page.transition_to_my_profile()
        my_profile.my_profile_is_opened()
        self.log.info("My profile page is opened")

    def test_transition_to_create_post(self, start_page, registered_user):
        """Transition to my profile page:
            - Log in user
            - Find Create post button
            - Click Create post button
            - Check Create post is opened successful   
        """
        # Init user data from fixture
        temp_username, _, temp_password = registered_user

        # Login as registered user
        main_page = start_page.login(temp_username, temp_password)
        self.log.info("Logged as '%s'", temp_username)

        # transition to create post
        main_page.transition_to_create_post_page()
        # verify create post is opened successful
        sleep(2)
        create_post = main_page.transition_to_create_post_page()
        create_post.create_post_is_opened()
        self.log.info("Create post page is opened")
