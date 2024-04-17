from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultPage(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, '.ais-highlight')
    LISTINGS = (By.CSS_SELECTOR, '.ais-InfiniteHits-item')
    PRODUCT_IMG = (By.XPATH, '//img[@class="ais-hit--picture"]')

    def verify_search_result(self, product):
        search_product = self.driver.find_element(*self.PRODUCT_NAME).text
        assert product.upper() in search_product, f'Expected {product} does not match {search_product}'
    def verify_search_url(self, expected_keyword):
        assert expected_keyword in self.driver.current_url, \
            f'Expected {expected_keyword} in {self.driver.current_url}'

    def verify_products_name_img(self):
        all_products = self.driver.find_elements(*self.LISTINGS)
        for product in all_products:
            title = product.find_element(*self.PRODUCT_NAME).text
            print(title)
            assert title, 'Product title not shown'
            product.find_element(*self.PRODUCT_IMG)

