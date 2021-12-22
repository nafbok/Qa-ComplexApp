from constants.header import HeaderConstants
from pages.base import BasePage
from pages.create_post_page import CreatePost
from pages.my_profile import MyProfile
from pages.utils import log_decorator


class Header(BasePage):
    """Stores actions from header panel"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConstants()

    @log_decorator
    def logout(self):
        """Log out from user account"""
        self.wait_until_element_enabled(value=self.constants.SIGN_OUT_BUTTON_XPATH).click()

    @log_decorator
    def refresh_main_page(self):
        """Refresh page by tapping logo-link"""
        self.wait_until_element_enabled(value=self.constants.LOGO_LINK_XPATH).click()

    @log_decorator
    def transition_to_search_bar(self):
        """Open search bar"""
        self.wait_until_element_enabled(value=self.constants.SEARCH_ICON_XPATH).click()

    @log_decorator
    def transition_to_chat_form(self):
        """Open Chat form"""
        self.wait_until_element_enabled(value=self.constants.CHAT_ICON_XPATH).click()

    @log_decorator
    def transition_to_my_profile(self):
        """Open my profile page"""
        self.wait_until_find_element(value=self.constants.MY_PROFILE_ICON_XPATH).click()
        return MyProfile(self.driver)

    @log_decorator
    def transition_to_create_post_page(self):
        """Open Create post page"""
        self.wait_until_find_element(value=self.constants.CREATE_POST_BUTTON_XPATH).click()
        return CreatePost(self.driver)
