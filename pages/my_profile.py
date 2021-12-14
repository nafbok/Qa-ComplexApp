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
