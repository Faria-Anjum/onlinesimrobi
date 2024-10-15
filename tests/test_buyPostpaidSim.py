#01841254366

from models.onlinesimrobi import SimPage
from models.postpaidsim import PostpaidFormPage, PostpaidPage

def test_selectPostpaidSim(page):
    sim = SimPage(page)
    postpaid = PostpaidPage(page)
    sim.navigate()
    postpaid.findPostpaidSim()
    postpaid.selectSimKnowMore()
    postpaid.selectSimOrderNow()

def test_selectSimNumber(page):
    sim = PostpaidFormPage(page)
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpCustomerDetails(page):
    sim = PostpaidFormPage(page)
    sim.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectDeliveryMethod(page):
    sim = PostpaidFormPage(page)
    sim.selectDeliveryDetails()

def test_confirmDeliveryThroughOTP(page):
    sim = PostpaidFormPage(page)
    sim.sendOTP()

