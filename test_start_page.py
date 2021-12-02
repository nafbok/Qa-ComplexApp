"""Stores tests related to Start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_start_page(self):
        """Sample test"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open Start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clear Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        sleep(3)
        # Find and clear Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(3)
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//*[text()='Sign In']")
        # Click button
        button.click()
        # Find error message
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == 'Error'
        sleep(10)

    def test_invalid_value(self):
        """Test invalid password and username"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open Start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clear Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()
        username.send_keys('Admin')
        sleep(3)
        # Find and clear Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys('qwerty')
        sleep(3)
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//*[text()='Sign In']")
        # Click button
        button.click()
        # Find error message
        message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # Verify message
        assert message.text == 'Error'
        sleep(10)

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

    def test_login_user(self):
        """Test  sign up new user successfully"""
        """
        - Create driver
        - Open start page
        - Find and clear username 
        - Pick  new username
        - Find and clear email 
        - Set valid email 
        - Find and clear password
        - Create password
        - Click Sign up button
        - Verify success sign up
        """
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver.exe")
        # Open Start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # Find and clear Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username.clear()
        # Set new username
        temp_username = self.random_username()
        username.send_keys(temp_username)
        sleep(3)
        # Find and clear email
        email = driver.find_element(by=By.XPATH, value=".//input[@placeholder='you@example.com']")
        email.clear()
        # Set email
        email.send_keys(self.random_email())
        # Find and clear Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password.clear()
        password.send_keys(self.random_password())
        sleep(3)
        # Find Sign Up button
        button = driver.find_element(by=By.XPATH, value=".//*[text()='Sign up for OurApp']")
        # Click button
        button.click()
        # Verify Sign up is successfully
        hello_user = driver.find_element(by=By.XPATH, value=".//h2[contains(text(), 'Hello')]")
        assert hello_user.text == f"Hello {temp_username.lower()}, your feed is empty."
