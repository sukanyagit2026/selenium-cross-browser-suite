import csv
import os
import pytest
from pages.login_page import LoginPage


def load_login_test_data():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "login_data.csv")
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


LOGIN_TEST_DATA = load_login_test_data()
@pytest.mark.parametrize(
    "case",
    LOGIN_TEST_DATA,
    ids=[f"{row['username'] or 'blank'}_{row['expected_result']}" for row in LOGIN_TEST_DATA],
)
def test_login(driver, case):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(case["username"], case["password"])

    flash_message = login_page.get_flash_message()
    assert case["expected_message_contains"] in flash_message

    if case["expected_result"] == "success":
        assert login_page.is_logged_in() is True
    else:
        assert login_page.is_logged_in() is False
        