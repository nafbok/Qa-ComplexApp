from selenium.webdriver.common.by import By

from constants.create_post import CreatePostConstants
from pages.base import BasePage
from pages.my_profile import MyProfile
from pages.utils import wait_until_ok, log_decorator


class CreatePost(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostConstants()

    @log_decorator
    def create_post_is_opened(self):
        """Verify create post page is opened"""
        new_post = self.wait_until_element_enabled(value=self.constants.TITLE_POST_XPATH)
        assert new_post.text == 'Title'

    @log_decorator
    def adding_new_post(self, title_value, body_content_value):
        """Add new post"""
        self.fill_field_post(by=By.XPATH, locator=self.constants.TITLE_INPUT_XPATH, value=title_value)
        self.fill_field_post(by=By.XPATH, locator=self.constants.BODY_CONTENT_XPATH, value=body_content_value)
        self.log.debug("Fields were filled")

        # click save new post button
        self._click_on_save_post_button()

    @log_decorator
    def delete_created_post(self):
        """Remove created post"""
        delete_post = self.wait_until_find_element(value=self.constants.REMOVE_ICON_XPATH)
        delete_post.click()
        self.log.info("Post was deleted")
        return MyProfile(self.driver)

    @wait_until_ok(timeout=10)
    def _click_on_save_post_button(self):
        """Click on button until it disappear"""
        # Perform click on button
        self.wait_until_find_element(value=self.constants.BUTTON_SAVE_NEW_POST_XPATH).click()

    @log_decorator
    def verify_adding_post(self):
        """Verify new post was added successfully"""
        message_added_post = self.wait_until_find_element(value=self.constants.MESSAGE_NEW_POST_CREATED_XPATH)
        assert message_added_post.text == 'New post successfully created.'
