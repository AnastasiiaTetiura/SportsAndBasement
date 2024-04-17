from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Open Help page')
def click_help(context):
    context.app.main_page.open_help_page()

@then('Verify there are {number} topics')
def verify_topics_number(context, number):
    context.app.help_page.verify_topics_number(number)
