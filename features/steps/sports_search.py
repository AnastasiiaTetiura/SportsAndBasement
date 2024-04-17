from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)


@then('Verify search worked for {product}')
def verify_search(context, product):
    context.app.search_results_page.verify_search_result(product)

@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    context.app.search_results_page.verify_search_url(expected_keyword)


@then('Verify that every product has name and image')
def verify_products_name_img(context):
    context.app.search_results_page.verify_products_name_img()


