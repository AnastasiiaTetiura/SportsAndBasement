from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click Add to cart')
def add_to_cart(context):
    context.app.product_page.add_to_cart()

@then('Verify cart has {number} items')
def verify_cart_item(context, number):
    context.app.cart_page.verify_cart_item(number)
