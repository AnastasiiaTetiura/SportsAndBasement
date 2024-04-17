from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage(Page):
    LOGIN = (By.CSS_SELECTOR, 'h1')
    EMAIL = (By.ID, 'CustomerEmail')
    PASSWORD = (By.ID, 'CustomerPassword')
    SIGNIN_BTN = (By.CSS_SELECTOR, '[value="Sign In"]')
    ACNT_DTL = (By.XPATH, '//h4[text()="Account Details"]')
    def verify_login_form(self):
        expected = "SHOPPING LOGIN"
        actual = self.driver.find_element(*self.LOGIN).text
        assert expected == actual, f'Expected {expected}, but actual is {actual}'

    def sign_in(self):
        self.find_element(*self.EMAIL).send_keys("sweetdd40@suksesboss.com")
        self.find_element(*self.PASSWORD).send_keys("sweet@123")
        #NOTE - SAVE PASSWORD ONLY WITH **** to the GIT IN REAL PROJECT

    def click_sign_in_btn(self):
        self.find_element(*self.SIGNIN_BTN).click()


    def verify_logged_in(self):
        expected = "ACCOUNT DETAILS"
        actual = self.find_element(*self.ACNT_DTL).text
        assert expected == actual, f'Expected {expected}, but actual is {actual}'








