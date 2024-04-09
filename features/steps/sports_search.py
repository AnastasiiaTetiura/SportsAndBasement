from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search-bar-input')
SEARCH_BTN = (By.CSS_SELECTOR, '[title="Submit your search"]')
PRODUCT_NAME = (By.CSS_SELECTOR, '.ais-highlight')
@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(3)

@then('Verify search worked for {product}')
def verify_search(context, product):
    search_product = context.driver.find_element(*PRODUCT_NAME).text
    assert product.upper() in search_product, f'Expected {product} does not match {search_product}'

@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, \
        f'Expected {expected_keyword} in {context.driver.current_url}'
