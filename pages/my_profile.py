from selenium.webdriver.common.by import By

from constants.my_profile import MyProfileConstants
from pages.base import BasePage


class MyProfile(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MyProfileConstants

    def my_profile_is_opened(self, username):
        """Verify my profile is opened"""
        username_text = self.driver.find_element(by=By.XPATH, value=self.constants.USER_NAME_XPATH)
        assert username_text.text == f'{username}'
