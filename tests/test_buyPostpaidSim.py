#01841254366

from models.onlinesimrobi import RobiPage
from models.postpaidsim import PostpaidFormPage, PostpaidPage

def test_selectPostpaidSim(page):
    sim = RobiPage(page)
    postpaid = PostpaidPage(page)
    sim.navigate()
    postpaid.findPostpaidSim()
    postpaid.selectSimKnowMore()
    postpaid.selectSimOrderNow()

def test_selectPostpaidSimNumber(page):
    sim = PostpaidFormPage(page)
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpPostpaidCustomerDetails(page):
    sim = PostpaidFormPage(page)
    sim.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectPostpaidDeliveryMethod(page):
    sim = PostpaidFormPage(page)
    sim.selectHomeDelivery()

def test_confirmPostpaidThroughOTP(page):
    sim = PostpaidFormPage(page)
    sim.sendOTP()

