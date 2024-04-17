from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CartPage(Page):
    ITEM_IN_CART = (By.CSS_SELECTOR, '.item')

    def verify_cart_item(self, number):
        number = int(number)
        self.driver.wait.until(
            EC.visibility_of_all_elements_located(self.ITEM_IN_CART)
        )
        items = self.driver.find_elements(*self.ITEM_IN_CART)
        print(items)
        assert len(items) == number, f'Expected {number} topics, but got {len(items)}'
