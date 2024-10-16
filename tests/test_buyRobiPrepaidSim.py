from models.prepaidsim import RobiPage, RobiPrepaidPage, RobiPrepaidFormPage

def test_selectRobiPrepaidSim(page):
    robi = RobiPage(page)
    prepaid = RobiPrepaidPage(page)
    robi.navigate()
    prepaid.findPrepaidSim()
    prepaid.selectSimKnowMore()
    prepaid.selectSimOrderNow()

def test_selectRobiPrepaidSimNumber(page):
    form = RobiPrepaidFormPage(page)
    form.findSimNumber()
    form.selectSimNumber()

def test_fillUpRobiPrepaidCustomerDetails(page):
    form = RobiPrepaidFormPage(page)
    form.fillUpCustomerDetails()

def test_selectRobiPrepaidDeliveryMethod(page):
    form = RobiPrepaidFormPage(page)
    form.selectHomeDelivery()

def test_confirmRobiPrepaidThroughOTP(page):
    form = RobiPrepaidFormPage(page)
    form.sendOTP()
