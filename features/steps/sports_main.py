from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

X_BTN = (By.CSS_SELECTOR, '[aria-label="Close dialog 3"]')
ACCNT_BTN = (By.ID, 'desktop-icon-link-account')
PRE_LOVED = (By.ID, 'secondary-nav-link-1')
LOGIN = (By.CSS_SELECTOR, 'h1')

@given('Open main page')
def open_main(context):
    context.driver.get('https://shop.sportsbasement.com/')

@when('Close ad')
def click_close_add(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(X_BTN)
    )
    context.driver.find_element(*X_BTN).click()

@when('Click Pre-loved department')
def click_preloved(context):
    context.driver.find_element(*PRE_LOVED).click()

@when('Click account button')
def click_accnt_btn(context):
    context.driver.find_element(*ACCNT_BTN).click()

@then('Verify Login form is present')
def verify_login_from(context):
    expected = "SHOPPING LOGIN"
    actual = context.driver.find_element(*LOGIN).text
    assert expected == actual, f'Expected {expected}, but actual is {actual}'


