from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "passwd")
    LOGIN_BUTTON = (By.NAME, "submitLogin")

    def login(self, username, password):
        """
        Logs into the application.
        """
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
