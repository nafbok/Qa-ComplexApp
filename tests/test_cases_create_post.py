import pytest
from selenium.webdriver.chrome import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestCreatePostPage(BaseTest):

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

    def test_add_new_post(self, start_page, registered_user):
        """Add new post:
            - Log in user
            - Go to the Create Post
            - Add new post
            - Verify New post added message success"""
        title_post_value = self.title_post()
        body_post_value = self.body_post()
        # Login as registered user
        main_page = start_page.login(registered_user)

        # Go to the Create Post
        main_page.transition_to_create_post_page()

        # Add new post
        create_new_post = main_page.transition_to_create_post_page()

        create_new_post.adding_new_post(title_post_value, body_post_value)

        # Verify New post added message success"""
        create_new_post.verify_adding_post()

    def test_remove_post(self, start_page, registered_user):
        """Remove created post:
            Steps:
                - Log in
                - Go to Create Post page
                - Create post
                - Verify New post added message success
                - Delete post
                - Verify New post deleted message success"""

        title_post_value = self.title_post()
        body_post_value = self.body_post()

        # Login as registered user
        main_page = start_page.login(registered_user)

        # Go to the Create Post
        main_page.transition_to_create_post_page()

        # Add new post
        create_new_post = main_page.transition_to_create_post_page()
        create_new_post.adding_new_post(title_post_value, body_post_value)

        # Verify New post added message success"""
        create_new_post.verify_adding_post()

        # Delete Post
        my_profile = create_new_post.delete_created_post()

        # Verify Post was deleted successfully
        my_profile.verify_message_deleted_post()
