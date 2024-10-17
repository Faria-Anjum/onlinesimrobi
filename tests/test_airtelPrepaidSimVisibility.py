
from models.productionda import HomePage, ATPrepaidInfoPage
import pytest

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    return page

def test_atprepaid_visibility(page):
    '''AT prepaid sim option is visible'''
    home = HomePage(page)
    home.navigate()
    home.navigate_to_airtel()
    atprepaid = ATPrepaidInfoPage(page)
    atprepaid.prepaid_visibility()

def test_atprepaid_check_know_details(page):
    '''AT prepaid sim>>know details option is accessible and visible'''
    home = HomePage(page)
    home.navigate()
    home.navigate_to_airtel()
    atprepaid = ATPrepaidInfoPage(page)
    atprepaid.prepaid_visibility()
    atprepaid.know_details

def test_atprepaid_click_order_now(page):
    '''AT prepaid sim>> order now option is accessible and visible'''
    home = HomePage(page)
    home.navigate()
    home.navigate_to_airtel()
    atprepaid = ATPrepaidInfoPage(page)
    atprepaid.prepaid_visibility()
    atprepaid.order_now()

# from models.prepaidsim import AirtelPage, AirtelPrepaidPage, AirtelPrepaidFormPage

# def test_selectAirtelPrepaidSim(page):
#     airtel = AirtelPage(page)
#     prepaid = AirtelPrepaidPage(page)
#     airtel.navigate()
#     prepaid.findPrepaidSim()
#     prepaid.selectSimKnowMore()
#     prepaid.selectSimOrderNow()

# def test_selectAirtelPrepaidSimNumber(page):
#     form = AirtelPrepaidFormPage(page)
#     form.findSimNumber()
#     form.selectSimNumber()

# def test_fillUpAirtelPrepaidCustomerDetails(page):
#     form = AirtelPrepaidFormPage(page)
#     form.fillUpCustomerDetails()

# def test_selectAirtelPrepaidDeliveryMethod(page):
#     form = AirtelPrepaidFormPage(page)
#     form.selectHomeDelivery()

# def test_confirmAirtelPrepaidThroughOTP(page):
#     form = AirtelPrepaidFormPage(page)
#     form.sendOTP()
