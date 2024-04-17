from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class HelpPage(Page):
    TOPIC = (By.CSS_SELECTOR, '#shopify-section-template--14511600730184__16552437945f2f16b5 a')
    def verify_topics_number(self, number):
        number = int(number)
        topics = self.driver.find_elements(*self.TOPIC)
        print(topics)
        assert len(topics) == number, f'Expected {number} topics, but got {len(topics)}'

