from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductsPage(BasePage):
    # Locators
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a#page-header-desc-configuration-add")
    PRODUCT_NAME_FIELD = (By.ID, "form_step1_name_1")
    PRODUCT_PRICE_FIELD = (By.ID, "form_step1_price_ttc")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button#submit")

    def navigate_to_products(self, url):
        """
        Navigates to the Products page.
        """
        self.driver.get(url)

    def add_product(self, name, price):
        """
        Adds a new product.
        """
        self.click(self.ADD_PRODUCT_BUTTON)
        self.enter_text(self.PRODUCT_NAME_FIELD, name)
        self.enter_text(self.PRODUCT_PRICE_FIELD, price)
        self.click(self.SAVE_BUTTON)
