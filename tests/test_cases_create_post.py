import pytest
from selenium.webdriver.chrome import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage


class TestCreatePostPage(BaseTest):

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

    def test_add_new_post(self, start_page, registered_user):
        """Add new post:
            - Log in user
            - Go to the Create Post
            - Add new post
            - Verify New post added message success"""
        title_post = 'Test'
        body_post = 'Text'

        # Init user data from fixture
        temp_username, _, temp_password = registered_user

        # Login as registered user
        main_page = start_page.login(temp_username, temp_password)
        self.log.info("Logged as '%s'", temp_username)

        # Go to the Create Post
        main_page.transition_to_create_post_page()

        # Add new post
        create_new_post = main_page.transition_to_create_post_page()
        self.log.info("Create page is opened")
        create_new_post.adding_new_post(title_post, body_post)
        self.log.info("New post is added")

        # Verify New post added message success"""
        create_new_post.verify_adding_post()
        self.log.info("Message New post successfully created is displayed")
