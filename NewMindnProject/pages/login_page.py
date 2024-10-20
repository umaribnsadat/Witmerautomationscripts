from selenium.webdriver.common.by import By

from NewMindnProject.pages.base_page import BasePage
from NewMindnProject.utils.config_loader import ConfigLoader
from NewMindnProject.Objectproperties.ObjectProperties import ObjectRepository

config = ConfigLoader()


class LoginPage(BasePage):
    def login(self, email=None, password=None):
        if email is None:
            email = ObjectRepository.login_email
        if password is None:
            password = ObjectRepository.login_password

        print("Navigating to login page")
        self.driver.get(ObjectRepository.login_url)

        print("Waiting for login button")
        login_button = self.wait_for_element(ObjectRepository.login_button_css)

        print("Entering email")
        email_field = self.wait_for_element(ObjectRepository.login_email_name)
        email_field.send_keys(email)

        print("Entering password")
        password_field = self.wait_for_element(ObjectRepository.login_password_name)
        password_field.send_keys(password)

        print("Clicking login button")
        login_button.click()
