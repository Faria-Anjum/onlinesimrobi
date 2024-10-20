from models.da_tests import HomePage, ATPrepaidInfoPage, ATPrepaidPage
import pytest

def test_atprepaid_type_number(page):
    '''Valid airtel prepaid msisdn can be typed in textbox'''
    home = HomePage(page)
    home.navigate()
    home.navigate_to_airtel()
    info = ATPrepaidInfoPage(page)
    info.prepaid_visibility()
    info.order_now()
    prepaid = ATPrepaidPage(page)
    prepaid.type_msisdn(prepaid.number)

def test_atprepaid_show_available(page):
    '''Avalilable valid airtel prepaid msisdn shows available message'''
    prepaid = ATPrepaidPage(page)
    prepaid.available_number()

def test_atprepaid_show_unavailable(page):
    '''Unavailable valid airtel prepaid msisdn shows unavailable message'''
    prepaid = ATPrepaidPage(page)
    prepaid.type_msisdn(prepaid.wrongNumber)
    prepaid.unavailable_number()

def test_atprepaid_click_refresh(page):
    '''Clicking refresh button works for airtel prepaid msisdn'''
    prepaid = ATPrepaidPage(page)
    prepaid.click_refresh()

def test_form_fillup(page):
    '''Home Delivery option can be selected for airtel prepaid sim delivery'''
    prepaid = ATPrepaidPage(page)
    prepaid.fill_customer_details()
    prepaid.select_home_delivery()

def test_delivery_time(page):
    '''Delivery time can be selected for airtel prepaid home delivery'''
    prepaid = ATPrepaidPage(page)
    prepaid.select_delivery_time()

def test_collect_from_wic(page):
    '''Nearest WIC option can be selected for airtel prepaid sim delivery'''
    prepaid = ATPrepaidPage(page)
    prepaid.select_nearest_wic()

def test_collect_from_store(page):
    '''Nearest Store option can be selected for airtel prepaid sim delivery'''
    prepaid = ATPrepaidPage(page)
    prepaid.select_nearest_store()

# def test_selectRobiATPrepaidSim(page):
#     airtel = RobiPage(page)
#     prepaid = RobiATPrepaidPage(page)
#     airtel.navigate()
#     prepaid.findATPrepaidSim()
#     prepaid.selectSimKnowMore()
#     prepaid.selectSimOrderNow()

# def test_selectRobiATPrepaidSimNumber(page):
#     form = RobiATPrepaidFormPage(page)
#     form.findSimNumber()
#     form.selectSimNumber()

# def test_fillUpRobiATPrepaidCustomerDetails(page):
#     form = RobiATPrepaidFormPage(page)
#     form.fillUpCustomerDetails()

# def test_selectRobiATPrepaidDeliveryMethod(page):
#     form = RobiATPrepaidFormPage(page)
#     form.selectHomeDelivery()

# def test_confirmRobiATPrepaidThroughOTP(page):
#     form = RobiATPrepaidFormPage(page)
#     form.sendOTP()
