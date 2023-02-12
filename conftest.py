import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def open_browser():
    browser.config.window_width = 300
    browser.config.window_height = 700

    yield

    browser.quit()
