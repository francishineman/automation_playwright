import pytest
from playwright.sync_api import sync_playwright

# This fixture automatically manages the Playwright browser context
# and page object for all tests that request the 'page' argument.
# It runs once per test function (scope='function').

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Override browser context arguments to disable video/screenshot saving 
    by default for cleaner runs, unless explicitly enabled in tests.
    """
    return {
        **browser_context_args,
        "record_video_dir": None,
        "viewport": {"width": 1920, "height": 1080}, # Set a fixed desktop viewport
    }

@pytest.fixture(scope="function")
def page(browser, browser_context_args):
    """
    A pytest fixture that creates a new page object for each test function.
    It yields the page and ensures the context/page is closed afterward.
    
    This replaces the default Playwright page fixture provided by pytest-playwright.
    """
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    page.close()
    context.close()

# Note: The 'browser' fixture is implicitly provided by pytest-playwright.
# You can configure the browser type (e.g., --browser=chromium) when running pytest.
