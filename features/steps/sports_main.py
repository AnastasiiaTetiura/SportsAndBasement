from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_main(context):
    context.app.main_page.open_main()

@when('Close ad')
def click_close_add(context):
    context.app.main_page.close_add()

@when('Click Pre-loved department')
def open_preloved(context):
    context.app.main_page.open_preloved()

@when('Click account button')
def open_account(context):
    context.app.main_page.open_account()

@then('Verify Login form is present')
def verify_login_from(context):
    context.app.login_page.verify_login_form()


@when('Verify header is present')
def verify_header_nav(context):
    context.app.main_page.verify_header_nav()


@then('Verify header has {number} links')
def verify_header_links(context, number):
    context.app.main_page.verify_header_links(number)


