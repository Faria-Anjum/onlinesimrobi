from models.productionda import HomePage, PrepaidInfoPage, PrepaidPage
import pytest

def test_prepaid_type_number(page):
    '''Valid robi prepaid msisdn can be typed in textbox'''
    home = HomePage(page)
    home.navigate()
    info = PrepaidInfoPage(page)
    info.prepaid_visibility()
    info.order_now()
    prepaid = PrepaidPage(page)
    prepaid.type_msisdn(prepaid.number)

def test_prepaid_show_available(page):
    '''Avalilable valid robi prepaid msisdn shows available message'''
    prepaid = PrepaidPage(page)
    prepaid.available_number()

def test_prepaid_show_unavailable(page):
    '''Unavailable valid robi prepaid msisdn shows unavailable message'''
    prepaid = PrepaidPage(page)
    prepaid.type_msisdn(prepaid.wrongNumber)
    prepaid.unavailable_number()

def test_prepaid_click_refresh(page):
    '''Clicking refresh button works for robi prepaid msisdn'''
    prepaid = PrepaidPage(page)
    prepaid.click_refresh()

def test_form_fillup(page):
    '''Home Delivery option can be selected for robi prepaid sim delivery'''
    prepaid = PrepaidPage(page)
    prepaid.fill_customer_details()
    prepaid.select_home_delivery()

def test_delivery_time(page):
    '''Delivery time can be selected for robi prepaid home delivery'''
    prepaid = PrepaidPage(page)
    prepaid.select_delivery_time()

def test_collect_from_wic(page):
    '''Nearest WIC option can be selected for robi prepaid sim delivery'''
    prepaid = PrepaidPage(page)
    prepaid.select_nearest_wic()

def test_collect_from_store(page):
    '''Nearest Store option can be selected for robi prepaid sim delivery'''
    prepaid = PrepaidPage(page)
    prepaid.select_nearest_store()

# def test_selectRobiPrepaidSim(page):
#     robi = RobiPage(page)
#     prepaid = RobiPrepaidPage(page)
#     robi.navigate()
#     prepaid.findPrepaidSim()
#     prepaid.selectSimKnowMore()
#     prepaid.selectSimOrderNow()

# def test_selectRobiPrepaidSimNumber(page):
#     form = RobiPrepaidFormPage(page)
#     form.findSimNumber()
#     form.selectSimNumber()

# def test_fillUpRobiPrepaidCustomerDetails(page):
#     form = RobiPrepaidFormPage(page)
#     form.fillUpCustomerDetails()

# def test_selectRobiPrepaidDeliveryMethod(page):
#     form = RobiPrepaidFormPage(page)
#     form.selectHomeDelivery()

# def test_confirmRobiPrepaidThroughOTP(page):
#     form = RobiPrepaidFormPage(page)
#     form.sendOTP()
