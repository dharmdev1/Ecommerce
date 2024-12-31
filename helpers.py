from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """
        Waits for an element to be present in the DOM and visible.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """
        Clicks an element.
        """
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """
        Enters text into a text field.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
