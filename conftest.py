"""Conftest"""
import logging
import random


def pytest_runtest_setup(item):
    # item.cls.logger = logging.getLogger(".".join((item.module.__name__, item.cls.__name__, item.name)))
    item.cls.logger = logging.getLogger(item.name)


class BaseTest:
    """Set some fields to provide autocomplete for dynamically added fields"""
    log = logging.getLogger(__name__)

    def random_username(self):
        """Return random username"""
        str_abc = 'qwertyuioplkjhgfdsazxcvbnm'
        set_symbols = list(str_abc)
        random.shuffle(set_symbols)
        new_username = ''.join(set_symbols)
        index = random.choice(range(3, 20))
        return new_username.capitalize()[:index]

    def random_email(self):
        """Create random email"""
        str_abc = 'qwertyuioplkjhgfdsazxcvbnm'
        set_symbols = list(str_abc)
        random.shuffle(set_symbols)
        name = ''.join(set_symbols)
        index = random.choice(range(3, 20))
        email_item = ['@gmail.com', '@ukr.net', '@mail.com']
        new_email = name[:index] + random.choice(email_item)
        return new_email

    def random_password(self):
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
