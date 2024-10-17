#01841254366

from models.productionda import HomePage, PostpaidInfoPage, PostpaidPage
import pytest

def test_postpaid_type_number(page):
    '''Valid msisdn can be typed in robi postpaid textbox'''
    home = HomePage(page)
    home.navigate()
    info = PostpaidInfoPage(page)
    info.postpaid_visibility()
    info.order_now()
    postpaid = PostpaidPage(page)
    postpaid.type_msisdn(postpaid.number)

def test_postpaid_show_available(page):
    '''Avalilable valid robi postpaid msisdn shows available message'''
    postpaid = PostpaidPage(page)
    postpaid.available_number()

def test_postpaid_show_unavailable(page):
    '''Unavailable valid robi postpaid msisdn shows unavailable message'''
    postpaid = PostpaidPage(page)
    postpaid.type_msisdn(postpaid.wrongNumber)
    postpaid.unavailable_number()

def test_postpaid_click_refresh(page):
    '''Clicking refresh button works for robi postpaid msisdn'''
    postpaid = PostpaidPage(page)
    postpaid.click_refresh()

def test_form_fillup(page):
    '''Home Delivery option can be selected for robi postpaid sim delivery'''
    postpaid = PostpaidPage(page)
    postpaid.fill_customer_details()
    postpaid.select_home_delivery()

def test_delivery_time(page):
    '''Delivery time can be selected for robi postpaid home delivery'''
    postpaid = PostpaidPage(page)
    postpaid.select_delivery_time()

def test_collect_from_wic(page):
    '''Nearest WIC option can be selected for robi postpaid sim delivery'''
    postpaid = PostpaidPage(page)
    postpaid.select_nearest_wic()

def test_collect_from_store(page):
    '''Nearest Store option can be selected for robi postpaid sim delivery'''
    postpaid = PostpaidPage(page)
    postpaid.select_nearest_store()

# from models.postpaidsim import RobiPage, PostpaidFormPage, PostpaidPage

# def test_selectRobiPostpaidSim(page):
#     robi = RobiPage(page)
#     postpaid = PostpaidPage(page)
#     robi.navigate()
#     postpaid.findPostpaidSim()
#     postpaid.selectSimKnowMore()
#     postpaid.selectSimOrderNow()

# def test_selectRobiPostpaidSimNumber(page):
#     form = PostpaidFormPage(page)
#     form.findSimNumber()
#     form.selectSimNumber()

# def test_fillUpRobiPostpaidCustomerDetails(page):
#     form = PostpaidFormPage(page)
#     form.fillUpCustomerDetails()
#     #storage = context.storage_state(path='reg.json')

# def test_selectRobiPostpaidDeliveryMethod(page):
#     form = PostpaidFormPage(page)
#     form.selectHomeDelivery()

# def test_confirmRobiPostpaidThroughOTP(page):
#     form = PostpaidFormPage(page)
#     form.sendOTP()

