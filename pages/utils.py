import datetime
import logging
import random
from time import sleep

from selenium.webdriver.chrome import webdriver as chrome
from selenium.webdriver.firefox import webdriver as firefox

from constants.base import BaseConstants


def wait_until_ok(timeout=5, period=0.25):
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(orig_func):
    """Creates logs based on docstrings"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecor]")
        result = orig_func(*args, **kwargs)
        log.info("%s", orig_func.__doc__)
        return result

    return wrapper


def random_username():
    """Return random username"""
    str_abc = 'qwertyuioplkjhgfdsazxcvbnm'
    set_symbols = list(str_abc)
    random.shuffle(set_symbols)
    new_username = ''.join(set_symbols)
    index = random.choice(range(3, 20))
    return new_username.capitalize()[:index]


def random_email():
    """Create random email"""
    str_abc = 'qwertyuioplkjhgfdsazxcvbnm'
    set_symbols = list(str_abc)
    random.shuffle(set_symbols)
    name = ''.join(set_symbols)
    index = random.choice(range(3, 20))
    email_item = ['@gmail.com', '@ukr.net', '@mail.com']
    new_email = name[:index] + random.choice(email_item)
    return new_email


def random_password():
    """Create random password"""
    str_abc = 'qwertyuioplkjhgfdsazxcvbnm'
    str_abc_upper = str_abc.upper()
    str_num = '1234567890'
    str_symbols = '!#$%^&*()_?><'
    str_set_symbols = str_abc + str_abc_upper + str_num + str_symbols
    set_symbols = list(str_set_symbols)
    random.shuffle(set_symbols)
    new_pas = ''.join(set_symbols)
    return new_pas[:12]


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password

    def fill_properties(self):
        self.username = random_username()
        self.email = random_email()
        self.password = random_password()


def create_driver(browser):
    """Create driver according to browser"""
    if browser == BaseConstants.CHROME:
        driver = chrome.WebDriver()
    elif browser == BaseConstants.FIREFOX:
        driver = firefox.WebDriver()
    else:
        raise RuntimeError(f"Unknown browser name: {browser}")
    return driver
