from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when("Input email and password on SignIn page")
def sign_in(context):
    context.app.login_page.sign_in()

@when("Click Sign In")
def click_sign_in_btn(context):
    context.app.login_page.click_sign_in_btn()

@then("Verify user is logged in")
def verify_user_logged(context):
    context.app.login_page.verify_logged_in()