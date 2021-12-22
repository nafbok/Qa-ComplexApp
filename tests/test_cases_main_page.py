"""Stores tests related to Start page and Main Page"""

import pytest

from conftest import BaseTest


class TestMainPage(BaseTest):

    @pytest.fixture(scope="function")
    def main_page(self, start_page, random_user):
        """Register user and return data"""
        # Fill email, login and password fields
        main_page = start_page.register_user(random_user)
        return main_page

    def test_refresh_first_page(self, main_page, random_user):
        """Refresh first page:
            - Find the logo "Complex app for testing - QA" 
            - Click the logo
            - Check refresh page successful   
        """
        main_page.header.refresh_main_page()
        # verify refresh page successful
        main_page.verify_welcome_message(random_user.username)

    def test_transition_to_search_bar(self, main_page):
        """Transition to the search bar:
            - Find search icon
            - Click search icon
            - Check search bar is opened successful   
        """
        # find and click search icon
        main_page.header.transition_to_search_bar()

        # verify search bar is opened successful
        main_page.verify_search_bar_opened()

    def test_transition_to_chat_form(self, main_page):
        """Transition to the char form:
            - Find chat icon
            - Click chat icon
            - Check chat form is opened successful   
        """
        # find and click chat icon
        main_page.header.transition_to_chat_form()

        # verify chat form is opened successful
        main_page.verify_chat_form_opened()

    def test_transition_to_my_profile(self, main_page):
        """Transition to my profile page:
            - Find my profile icon
            - Click my profile icon
            - Check my profile page is opened successful   
        """
        # transition to My profile page
        my_profile = main_page.header.transition_to_my_profile()
        # verify chat form is opened successful
        my_profile.my_profile_is_opened()

    def test_transition_to_create_post(self, main_page):
        """Transition to my profile page:
            - Find Create post button
            - Click Create post button
            - Check Create post is opened successful   
        """
        # transition to create post
        create_post = main_page.header.transition_to_create_post_page()
        # verify create post is opened successful
        create_post.create_post_page_is_opened()
