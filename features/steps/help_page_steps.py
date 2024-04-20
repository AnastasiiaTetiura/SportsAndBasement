from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open review page for the SB gift card')
def open_review_page(context):
    context.app.review_page.open_review()

@when('Open Help page')
def click_help(context):
    context.app.main_page.open_help_page()

@when('Store original window')
def store_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.original_window = context.app.page.get_current_window()
    # print('All windows', context.windows)
    # print('Current window', context.original_window)


@when('Click Power Reviews')
def click_power_reviews(context):
    context.app.review_page.click_power_reviews()

@when('Switch to new window')
def switch_window(context):
    context.app.page.switch_to_new_window()

@when('Close current page')
def close(context):
    context.app.page.close_page()
    sleep(2)

@when('Return to original window')
def switch_to_original(context):
    context.app.page.switch_to_window(context.original_window)
    sleep(2)

@then('Verify Power Reviews page is open')
def verify_power_reviews_open(context):
    context.app.review_page.verify_power_reviews_open()

@then('Verify there are {number} topics')
def verify_topics_number(context, number):
    context.app.help_page.verify_topics_number(number)



