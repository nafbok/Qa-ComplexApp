from constants.main_page import MainPageConstants
from pages.base import BasePage
from pages.create_post import CreatePost
from pages.my_profile import MyProfile


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def verify_welcome_message(self, username):
        """Verify welcome message for the user"""
        hello_user = self.wait_until_find_element(value=self.constants.WELCOME_MESSAGE_XPATH)
        assert hello_user.text == f"Hello {username.lower()}, your feed is empty."

    def logout(self):
        """Log out from user account"""
        self.wait_until_element_enabled(value=self.constants.SIGN_OUT_BUTTON_XPATH).click()

    def refresh_main_page(self):
        """Refresh page by tapping logo-link"""
        self.wait_until_element_enabled(value=self.constants.LOGO_LINK_XPATH).click()

    def transition_to_search_bar(self):
        """Open search bar"""
        self.wait_until_element_enabled(value=self.constants.SEARCH_ICON_XPATH).click()

    def verify_search_bar_opened(self):
        """Verify search bar is opened"""
        search_bar = self.wait_until_find_element(value=self.constants.PLACEHOLDER_SEARCH_BAR_XPATH)
        assert search_bar.is_displayed()

    def transition_to_chat_form(self):
        """Open Chat form"""
        self.wait_until_element_enabled(value=self.constants.CHAT_ICON_XPATH).click()

    def verify_chat_form_opened(self):
        chat_form = self.wait_until_find_element(value=self.constants.CHAT_FORM_XPATH)
        assert chat_form.text == "Chat"

    def transition_to_my_profile(self):
        """Open my profile page"""
        self.wait_until_find_element(value=self.constants.MY_PROFILE_ICON_XPATH).click()
        return MyProfile(self.driver)

    def transition_to_create_post_page(self):
        """Open Create post page"""
        self.wait_until_find_element(value=self.constants.CREATE_POST_BUTTON_XPATH).click()
        return CreatePost(self.driver)
