from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results_page import SearchResultPage
from pages.login_page import LoginPage
from pages.help_page import HelpPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.review_page import ReviewPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)

        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultPage(driver)
        self.login_page = LoginPage(driver)
        self.help_page = HelpPage(driver)
        self.cart_page = CartPage(driver)
        self.product_page = ProductPage(driver)
        self.review_page = ReviewPage(driver)
