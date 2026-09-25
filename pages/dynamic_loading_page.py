from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    FINISH_TEXT = (By.ID, "finish")

    def load(self):
        self.open(self.URL)

    def start_loading(self):
        self.click(self.START_BUTTON)

    def get_finish_text(self):
        return self.get_text(self.FINISH_TEXT, timeout=15)