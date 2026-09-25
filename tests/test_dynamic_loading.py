from pages.dynamic_loading_page import DynamicLoadingPage


def test_dynamic_loading_reveals_text(driver):
    dynamic_page = DynamicLoadingPage(driver)
    dynamic_page.load()
    dynamic_page.start_loading()

    finish_text = dynamic_page.get_finish_text()
    assert "Hello World" in finish_text