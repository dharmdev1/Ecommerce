from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
