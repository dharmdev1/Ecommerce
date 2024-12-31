import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        """
        This method is called before every test. It initializes the WebDriver.
        """
        self.driver = webdriver.Chrome()  # No path needed for modern versions if ChromeDriver is in PATH
        self.driver.maximize_window()

    def test_valid_login(self):
        """
        This test case checks if the login works with valid credentials.
        """
        driver = self.driver
        driver.get(
            "https://es.bishalkarki.com/admin12/index.php?controller=AdminLogin&token=243394023a948e1b81dd83bb2d8067d7"
        )

        # Perform login actions
        username_field = driver.find_element(By.ID, "email")  # Replace with actual ID
        password_field = driver.find_element(By.ID, "passwd")  # Replace with actual ID

        username_field.send_keys("admin@es.bishalkarki.com")  # Replace with your username
        password_field.send_keys("Password123!@#")  # Replace with your password
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for the page to load

        # Verify login success
        try:
            dashboard_element = driver.find_element(By.CLASS_NAME, "page-title")  # Replace with actual element
            self.assertIn("Dashboard", dashboard_element.text, "Login failed!")
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_invalid_login(self):
        """
        This test case checks login behavior with invalid credentials.
        """
        driver = self.driver
        driver.get(
            "https://es.bishalkarki.com/admin12/index.php?controller=AdminLogin&token=243394023a948e1b81dd83bb2d8067d7"
        )

        # Perform login actions with invalid credentials
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "passwd")

        username_field.send_keys("invalid_username")
        password_field.send_keys("invalid_password")
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)

        # Verify login failure message
        try:
            error_message = driver.find_element(By.CLASS_NAME, "alert-danger")  # Replace with actual element
            self.assertIn("Invalid credentials", error_message.text, "Error message not displayed!")
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        """
        This method is called after every test. It cleans up the WebDriver.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
