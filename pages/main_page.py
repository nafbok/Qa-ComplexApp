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

    def refresh_main_page(self):
        """Refresh page by tapping logo-link"""
        self.driver.find_element(by=By.XPATH, value=self.constants.LOGO_LINK_XPATH).click()

    def transition_to_search_bar(self):
        """Open search bar"""
        self.driver.find_element(by=By.XPATH, value=self.constants.SEARCH_ICON_XPATH).click()

    def verify_search_bar_opened(self):
        """Verify search bar is opened"""
        search_bar = self.driver.find_element(by=By.XPATH, value=self.constants.PLACEHOLDER_SEARCH_BAR_XPATH)
        assert search_bar.is_displayed()

    def transition_to_chat_form(self):
        """Open Chat form"""
        self.driver.find_element(by=By.XPATH, value=self.constants.CHAT_ICON_XPATH)

    def verify_chat_form_opened(self):
        chat_form = self.driver.find_element(by=By.XPATH, value=self.constants.CHAT_FORM_XPATH)
        assert chat_form.text == "Chat"

    def transition_to_my_profile(self):
        """Open my profile page"""
        self.driver.find_element(by=By.XPATH, value=self.constants.MY_PROFILE_ICON_XPATH)

    def transition_to_create_post_page(self):
        """Open Create post page"""
        self.driver.find_element(by=By.XPATH, value=self.constants.CREATE_POST_BUTTON_XPATH)
