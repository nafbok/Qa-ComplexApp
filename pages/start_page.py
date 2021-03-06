from selenium.webdriver.common.by import By

from constants.main_page import MainPageConstants
from constants.start_page import StartPageConstants
from pages.base import BasePage
from pages.utils import wait_until_ok, log_decorator


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_decorator
    def login(self, user):
        """Login using provided password and username"""
        from pages.main_page import MainPage
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_IN_USERNAME_XPATH, value=user.username)
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_IN_PASSWORD_XPATH, value=user.password)

        self.log.debug("Fields are filled with invalid values")

        # Find Sign In button
        sign_in_button = self.wait_until_element_enabled(value=self.constants.SIGN_IN_BUTTON_XPATH)
        # Click button
        sign_in_button.click()
        self.log.debug("Clicked on 'Sign in'")
        return MainPage(self.driver)

    @log_decorator
    def verify_incorrect_login(self):
        """Verify error message an invalid login"""
        # Find error message
        message = self.wait_until_find_element(value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        # Verify message
        assert message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT

    @log_decorator
    def register_user(self, user):
        """Register user using provided data"""
        from pages.main_page import MainPage
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(by=By.XPATH, locator=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        self.log.debug("Fields were filled")

        # Find Sign Up button
        self._click_on_sign_up_button()
        self.log.debug("User was registered")
        return MainPage(self.driver)

    @wait_until_ok(timeout=10)
    def _click_on_sign_up_button(self):
        """Click on button until it disappear"""
        # Perform click on button
        self.wait_until_element_enabled(value=self.constants.SIGN_UP_BUTTON_XPATH).click()

        # Verify welcome message
        assert self.is_element_exists(value=MainPageConstants.WELCOME_MESSAGE_XPATH)
