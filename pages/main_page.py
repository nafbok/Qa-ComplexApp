from constants.main_page import MainPageConstants
from pages.base import BasePage
from pages.header import Header
from pages.utils import log_decorator


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()
        self.header = Header(self.driver)

    @log_decorator
    def verify_welcome_message(self, username):
        """Verify welcome message for the user"""
        hello_user = self.wait_until_find_element(value=self.constants.WELCOME_MESSAGE_XPATH)
        assert hello_user.text == f"Hello {username.lower()}, your feed is empty."

    @log_decorator
    def verify_search_bar_opened(self):
        """Verify search bar is opened"""
        search_bar = self.wait_until_find_element(value=self.constants.PLACEHOLDER_SEARCH_BAR_XPATH)
        assert search_bar.is_displayed()

    @log_decorator
    def verify_chat_form_opened(self):
        chat_form = self.wait_until_find_element(value=self.constants.CHAT_FORM_XPATH)
        assert chat_form.text == "Chat"


