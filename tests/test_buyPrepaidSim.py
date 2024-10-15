from models.onlinesimrobi import RobiPage 
from models.prepaidsim import PrepaidPage, PrepaidFormPage

def test_selectPrepaidSim(page):
    sim = RobiPage(page)
    prepaid = PrepaidPage(page)
    sim.navigate()
    prepaid.findPrepaidSim()
    prepaid.selectSimKnowMore()
    prepaid.selectSimOrderNow()

def test_selectPrepaidSimNumber(page):
    sim = PrepaidFormPage(page)
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpPrepaidCustomerDetails(page):
    sim = PrepaidFormPage(page)
    sim.fillUpCustomerDetails()

def test_selectPrepaidDeliveryMethod(page):
    sim = PrepaidFormPage(page)
    sim.selectHomeDelivery()

def test_confirmPrepaidThroughOTP(page):
    sim = PrepaidFormPage(page)
    sim.sendOTP()
