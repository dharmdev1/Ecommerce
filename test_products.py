import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import LOGIN_URL, PRODUCTS_URL, USERNAME, PASSWORD


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)

    def test_add_product(self):
        self.driver.get(LOGIN_URL)
        self.login_page.login(USERNAME, PASSWORD)

        self.products_page.navigate_to_products(PRODUCTS_URL)
        self.products_page.add_product("Test Product", "19.99")

        # Add assertions to verify success message or product presence

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
