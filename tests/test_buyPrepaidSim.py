from models.onlinesimrobi import SimPage 
from models.prepaidsim import PrepaidPage, PrepaidFormPage

def test_selectPrepaidSim(page):
    sim = SimPage(page)
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
    #storage = context.storage_state(path='reg.json')

def test_selectPrepaidDeliveryMethod(page):
    sim = PrepaidFormPage(page)
    sim.selectHomeDelivery()

def test_confirmPrepaidThroughOTP(page):
    sim = PrepaidFormPage(page)
    sim.sendOTP()
