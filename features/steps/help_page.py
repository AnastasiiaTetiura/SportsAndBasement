from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

HELP_BTN =(By.ID, 'desktop-icon-link-help')
TOPIC = (By.CSS_SELECTOR, '#shopify-section-template--14511600730184__16552437945f2f16b5 a')

@when('Open Help page')
def click_help(context):
    context.driver.find_element(*HELP_BTN).click()

@then('Verify there are {number} topics')
def verify_topics_number(context, number):
    number = int(number)
    topics = context.driver.find_elements(*TOPIC)
    print(topics)
    assert len(topics) == number, f'Expected {number} topics, but got {len(topics)}'
