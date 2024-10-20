from models.da_tests import HomePage, PrepaidInfoPage
import pytest

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    return page

def test_prepaid_visibility(page):
    '''Robi prepaid sim option is visible'''
    home = HomePage(page)
    home.navigate()
    prepaid = PrepaidInfoPage(page)
    prepaid.prepaid_visibility()

def test_prepaid_check_know_details(page):
    '''Robi prepaid sim>>know details option is accessible and visible'''
    home = HomePage(page)
    home.navigate()
    prepaid = PrepaidInfoPage(page)
    prepaid.prepaid_visibility()
    prepaid.know_details

def test_prepaid_click_order_now(page):
    '''Robi prepaid sim>> order now option is accessible and visible'''
    home = HomePage(page)
    home.navigate()
    prepaid = PrepaidInfoPage(page)
    prepaid.prepaid_visibility()
    prepaid.order_now()