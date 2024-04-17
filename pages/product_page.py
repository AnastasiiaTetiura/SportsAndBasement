from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ProductPage(Page):
    SEARCH_RESULT_ITEM = (By.XPATH, '//li[@class="ais-InfiniteHits-item"]')
    ADD_BTN = (By.ID, 'add')
    def add_to_cart(self):
        self.driver.find_element(*self.SEARCH_RESULT_ITEM).click()
        self.driver.wait.until(
            EC.visibility_of_element_located(self.ADD_BTN)
        )
        self.driver.find_element(*self.ADD_BTN).click()