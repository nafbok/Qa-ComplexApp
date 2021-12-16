from constants.my_profile import MyProfileConstants
from pages.base import BasePage


class MyProfile(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MyProfileConstants()

    def my_profile_is_opened(self):
        """Verify my profile is opened"""
        username_text = self.wait_until_find_element(value=self.constants.USER_NAME_XPATH)
        assert username_text.is_displayed

    def verify_message_deleted_post(self):
        """Verify post was deleted successfully"""
        message_text = self.wait_until_find_element(value=self.constants.MESSAGE_DELETED_POST_XPATH)
        assert message_text == 'Post successfully deleted'
