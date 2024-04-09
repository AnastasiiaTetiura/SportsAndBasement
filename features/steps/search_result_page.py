from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULT_ITEM = (By.XPATH, '//li[@class="ais-InfiniteHits-item"]')
ADD_BTN = (By.ID, 'add')
ITEM_IN_CART = (By.CSS_SELECTOR, '.item')

@when('Click Add to cart')
def add_to_cart(context):
    context.driver.find_element(*SEARCH_RESULT_ITEM).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(ADD_BTN)
    )
    context.driver.find_element(*ADD_BTN).click()

@then('Verify cart has {number} items')
def verify_cart_item(context, number):
    number = int(number)
    context.driver.wait.until(
        EC.visibility_of_all_elements_located(ITEM_IN_CART)
    )
    items = context.driver.find_elements(*ITEM_IN_CART)
    print(items)
    assert len(items) == number, f'Expected {number} topics, but got {len(items)}'
