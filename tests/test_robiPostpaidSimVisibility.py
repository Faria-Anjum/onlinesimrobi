from models.productionda import HomePage, PostpaidInfoPage
import pytest

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    return page

def test_postpaid_visibility(page):
    '''Robi postpaid sim option is visible'''
    home = HomePage(page)
    home.navigate()
    postpaid = PostpaidInfoPage(page)
    postpaid.postpaid_visibility()

def test_postpaid_check_know_details(page):
    '''Robi postpaid sim>>know details option is accessible and visible'''
    home = HomePage(page)
    home.navigate()
    postpaid = PostpaidInfoPage(page)
    postpaid.postpaid_visibility()
    postpaid.know_details

def test_postpaid_click_order_now(page):
    '''Robi postpaid sim>> order now option is accessible and visible'''
    home = HomePage(page)
    home.navigate()
    postpaid = PostpaidInfoPage(page)
    postpaid.postpaid_visibility()
    postpaid.order_now()