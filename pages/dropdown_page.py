from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"

    DROPDOWN = (By.ID, "dropdown")

    def load(self):
        self.open(self.URL)

    def select_option(self, option_text):
        dropdown_element = self.find(self.DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

    def get_selected_option(self):
        dropdown_element = self.find(self.DROPDOWN)
        select = Select(dropdown_element)
        return select.first_selected_option.text