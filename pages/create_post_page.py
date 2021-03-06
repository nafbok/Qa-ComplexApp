from selenium.webdriver.common.by import By

from constants.create_post_page import CreatePostConstants
from pages.base import BasePage
from pages.utils import log_decorator


class CreatePost(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostConstants()
        from pages.header import Header
        self.header = Header(self.driver)

    @log_decorator
    def adding_new_post(self, title_value, body_content_value):
        """Add new post"""
        from pages.post_page import PostPage
        # Fill required fields
        self.fill_field_post(by=By.XPATH, locator=self.constants.TITLE_INPUT_XPATH, value=title_value)
        self.fill_field_post(by=By.XPATH, locator=self.constants.BODY_CONTENT_XPATH, value=body_content_value)

        # click save new post button
        self.wait_until_element_enabled(value=self.constants.BUTTON_SAVE_NEW_POST_XPATH).click()

        return PostPage(self.driver)

    @log_decorator
    def create_post_page_is_opened(self):
        """Create post page is opened"""
        page_is_opened = self.wait_until_find_element(value=self.constants.TITLE_POST_XPATH)
        assert page_is_opened.text == 'Title'

