#01841254366

from models.postpaidsim import RobiPage, PostpaidFormPage, PostpaidPage

def test_selectRobiPostpaidSim(page):
    robi = RobiPage(page)
    postpaid = PostpaidPage(page)
    robi.navigate()
    postpaid.findPostpaidSim()
    postpaid.selectSimKnowMore()
    postpaid.selectSimOrderNow()

def test_selectRobiPostpaidSimNumber(page):
    form = PostpaidFormPage(page)
    form.findSimNumber()
    form.selectSimNumber()

def test_fillUpRobiPostpaidCustomerDetails(page):
    form = PostpaidFormPage(page)
    form.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectRobiPostpaidDeliveryMethod(page):
    form = PostpaidFormPage(page)
    form.selectHomeDelivery()

def test_confirmRobiPostpaidThroughOTP(page):
    form = PostpaidFormPage(page)
    form.sendOTP()

