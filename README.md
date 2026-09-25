# Selenium Cross-Browser Test Suite

Automated UI test suite for [the-internet.herokuapp.com](https://the-internet.herokuapp.com), built with Python, Selenium WebDriver, and pytest, using the Page Object Model design pattern. Tests run cross-browser (Chrome + Firefox) both locally and in CI via GitHub Actions.

![CI](https://github.com/sukanyagit2026/selenium-cross-browser-suite/actions/workflows/selenium-tests.yml/badge.svg)

## Key Skills Demonstrated

- Page Object Model (POM) architecture for maintainable, reusable test code
- Data-driven testing with `pytest.mark.parametrize`, including CSV-driven test data
- Explicit waits (`WebDriverWait` + `expected_conditions`) for reliable handling of dynamic content
- Cross-browser testing (Chrome and Firefox) via a configurable pytest fixture
- Automatic screenshot capture on test failure for debugging
- Self-contained HTML test reports with `pytest-html`
- Continuous Integration with GitHub Actions, running the full suite on every push across a browser matrix

## Tech Stack

- Python 3.11
- Selenium WebDriver
- pytest
- webdriver-manager (automatic ChromeDriver/GeckoDriver management)
- pytest-html
- GitHub Actions

## Test Coverage

| Area | Description |
|---|---|
| Login | 5 data-driven scenarios (valid login, wrong password, wrong username, blank fields) sourced from a CSV file |
| Dropdown | Selecting options and verifying selection state |
| Dynamic Loading | Handling content that appears asynchronously after a delay |
| File Upload | Uploading a file and verifying the upload confirmation |

## Project Structure