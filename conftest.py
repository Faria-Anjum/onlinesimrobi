from models.prepaidsim import PrepaidPage, RegistrationPage
from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page