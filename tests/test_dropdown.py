import pytest
from pages.dropdown_page import DropdownPage


@pytest.mark.parametrize("option_text", ["Option 1", "Option 2"])
def test_select_dropdown_option(driver, option_text):
    dropdown_page = DropdownPage(driver)
    dropdown_page.load()
    dropdown_page.select_option(option_text)

    selected = dropdown_page.get_selected_option()
    assert selected == option_text