import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, timeout=5)

    def fill_field(self, by, locator, value):
        """Fill field using provided variables"""
        username = self.driver.find_element(by=by, value=locator)
        username.clear()
        username.send_keys(value)

    def is_element_exists(self, value, by=By.XPATH):
        """Return True if element could be find otherwise False"""
        try:
            self.wait_until_find_element(by=by, value=value)
            return True
        except TimeoutException:
            return False

    def wait_until_find_element(self, value, by=By.XPATH):
        """Wait until find element"""
        return self.wait.until(EC.visibility_of_element_located(locator=(by, value)))

    def wait_until_element_enabled(self, value, by=By.XPATH):
        """Wait until element enabled"""
        element = self.wait_until_find_element(by=by, value=value)
        return self.wait.until(EC.element_to_be_clickable(element))
