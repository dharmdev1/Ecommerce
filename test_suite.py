import unittest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from login_page import LoginPage
from products_page import ProductsPage


class TestSuite(unittest.TestCase):
    def setUp(self):
        """
        Initialize the WebDriver.
        """
        try:
            self.driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
            self.driver.maximize_window()
            self.login_page = LoginPage(self.driver)
            self.products_page = ProductsPage(self.driver)
        except WebDriverException as e:
            self.fail(f"WebDriver initialization failed: {e}")

    def tearDown(self):
        """
        Clean up the WebDriver.
        """
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Error during WebDriver teardown: {e}")

    def test_login(self):
        """
        Test for login functionality.
        """
        self.login_page.login()

    def test_add_new_product(self):
        """
        Test for adding a new product.
        """
        self.login_page.login()
        self.products_page.navigate_to_products()
        self.products_page.add_new_product("Test Product")

    def test_edit_product_price(self):
        """
        Test for editing the product price.
        """
        self.login_page.login()
        self.products_page.navigate_to_products()
        self.products_page.edit_product_price("Test Product", 12.00)

    def test_delete_product(self):
        """
        Test for deleting the product.
        """
        self.login_page.login()
        self.products_page.navigate_to_products()
        self.products_page.delete_product("Test Product")


if __name__ == "__main__":
    unittest.main()
