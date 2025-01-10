from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage
import config


class LoginPage(BasePage):
    def login(self):
        # Navigate to the login page
        self.driver.get(config.LOGIN_URL)

        # Enter username and password
        self.enter_text((By.ID, "email"), config.USERNAME)
        self.enter_text((By.ID, "passwd"), config.PASSWORD)
        self.driver.find_element(By.ID, "passwd").send_keys(Keys.RETURN)

        # Verify login success
        dashboard_element = self.wait_for_element((By.CLASS_NAME, "page-title"))
        assert "Dashboard" in dashboard_element.text, "Login failed!"
