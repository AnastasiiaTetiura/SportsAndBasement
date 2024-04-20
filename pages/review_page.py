from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ReviewPage(Page):
    POWER_REVIEW = (By.CSS_SELECTOR, '[aria-label="PowerReviews"]')
    def open_review(self):
        self.open_url("https://shop.sportsbasement.com/pages/write-a-review/?pr_page_id=138717888528&pr_merchant_id=965487&pr_merchant_group_id=77450")

    def click_power_reviews(self):
        self.find_element(*self.POWER_REVIEW).click()

    def verify_power_reviews_open(self):
        self.verify_partial_url("https://www.powerreviews.com/")



