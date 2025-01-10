from selenium.webdriver.common.by import By
from base_page import BasePage
import config


class ProductsPage(BasePage):
    def navigate_to_products(self):
        # Navigate to the products page
        self.driver.get(config.PRODUCTS_URL)

    def add_new_product(self, product_name):
        # Click the "Add new product" button
        add_button = self.wait_for_element((By.CSS_SELECTOR, "i.process-icon-new"))
        self.scroll_to_element(add_button)
        add_button.click()

        # Enter product name
        name_field = self.wait_for_element((By.ID, "name_1"))
        self.scroll_to_element(name_field)
        self.enter_text((By.ID, "name_1"), product_name)

        # Save the product
        save_button = self.wait_for_element((By.CSS_SELECTOR, "i.process-icon-save"))
        self.scroll_to_element(save_button)
        save_button.click()

        # Verify product addition
        success_message = self.wait_for_element((By.CLASS_NAME, "alert-success"))
        assert "successful creation" in success_message.text.lower(), "Product addition failed!"

    def edit_product_price(self, product_name, price):
        # Locate the product and click "Edit"
        edit_button_xpath = f"//tr[contains(., '{product_name}')]//a[@class='edit btn btn-default']"
        edit_button = self.wait_for_element((By.XPATH, edit_button_xpath))
        self.scroll_to_element(edit_button)
        edit_button.click()

        # Navigate to the "Prices" tab
        prices_tab = self.wait_for_element((By.CSS_SELECTOR, "a#link-Prices"))
        self.scroll_to_element(prices_tab)
        prices_tab.click()

        # Update wholesale price
        wholesale_price_field = self.wait_for_element((By.ID, "wholesale_price"))
        self.scroll_to_element(wholesale_price_field)
        self.enter_text((By.ID, "wholesale_price"), str(price))

        # Save the changes
        save_button = self.wait_for_element((By.CSS_SELECTOR, "button[name='submitAddproduct']"))
        self.scroll_to_element(save_button)
        save_button.click()

        # Verify price update success
        success_message = self.wait_for_element((By.CLASS_NAME, "alert-success"))
        assert "successful update" in success_message.text.lower(), "Price update failed!"

    def delete_product(self, product_name):
        # Locate the product and click "Delete"
        delete_button_xpath = f"//tr[contains(., '{product_name}')]//a[@class='delete']"
        delete_button = self.wait_for_element((By.XPATH, delete_button_xpath))
        self.scroll_to_element(delete_button)
        delete_button.click()

        # Confirm the deletion
        alert = self.driver.switch_to.alert
        alert.accept()

        # Verify product deletion
        success_message = self.wait_for_element((By.CLASS_NAME, "alert-success"))
        assert "successful deletion" in success_message.text.lower(), "Product deletion failed!"
