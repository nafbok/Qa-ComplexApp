from selenium.webdriver.common.by import By

from constants.main_page import MainPageConstants
from pages.base import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def verify_welcome_message(self, username):
        """Verify welcome message for the user"""

        hello_user = self.driver.find_element(by=By.XPATH, value=self.constants.WELCOME_MESSAGE_XPATH)
        assert hello_user.text == f"Hello {username.lower()}, your feed is empty."

    def logout(self):
        """Log out from user account"""
        self.driver.find_element(by=By.XPATH, value=self.constants.SIGH_OUT_BUTTON_XPATH).click()
