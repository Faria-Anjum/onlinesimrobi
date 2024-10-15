from models.onlinesimrobi import SimPage 
from models.prepaidsim import PrepaidPage, PrepaidFormPage

def test_selectPrepaidSim(page):
    sim = SimPage(page)
    prepaid = PrepaidPage(page)
    sim.navigate()
    prepaid.findPrepaidSim()
    prepaid.selectSimKnowMore()
    prepaid.selectSimOrderNow()

def test_selectSimNumber(page):
    sim = PrepaidFormPage(page)
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpCustomerDetails(page):
    sim = PrepaidFormPage(page)
    sim.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectDeliveryMethod(page):
    sim = PrepaidFormPage(page)
    sim.selectDeliveryDetails()

def test_confirmDeliveryThroughOTP(page):
    sim = PrepaidFormPage(page)
    sim.sendOTP()
