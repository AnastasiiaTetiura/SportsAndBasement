from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search-bar-input')
    SEARCH_BTN = (By.CSS_SELECTOR, '[title="Submit your search"]')
    X_BTN = (By.CSS_SELECTOR, '[aria-label="Close dialog 3"]')
    HEADER = (By.ID, 'secondary-nav')
    HEADER_LINKS = (By.CSS_SELECTOR, '#secondary-nav a')
    PRE_LOVED = (By.ID, 'secondary-nav-link-1')
    ACCNT_BTN = (By.ID, 'desktop-icon-link-account')
    HELP_BTN = (By.ID, 'desktop-icon-link-help')

    def open_main(self):
        self.open_url('https://shop.sportsbasement.com/')

    def close_add(self):
        self.driver.wait.until(
            EC.visibility_of_element_located(self.X_BTN)
        )
        self.driver.find_element(*self.X_BTN).click()

    def open_preloved(self):
        self.driver.find_element(*self.PRE_LOVED).click()
    def open_account(self):
        self.driver.find_element(*self.ACCNT_BTN).click()

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(3)


    def verify_header_nav(self):
        self.driver.find_element(*self.HEADER)

    def verify_header_links(self, number):
        number = int(number)
        links = self.driver.find_elements(*self.HEADER_LINKS)
        print(links)
        assert len(links) == number, f'Expected {number} links, but got {len(links)}'

    def open_help_page(self):
        self.driver.find_element(*self.HELP_BTN).click()