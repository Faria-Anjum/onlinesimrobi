from models.prepaidsim import PrepaidPage, RegistrationPage
from playwright.sync_api import Page, sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
prepaid = PrepaidPage(page)
sim = RegistrationPage(page)

def test_selectPrepaidSim():
    prepaid.navigate()
    prepaid.findPrepaidSim()
    prepaid.selectPrepaidSimKnowMore()
    prepaid.selectPrepaidSimOrderNow()

def test_selectSimNumber():
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpCustomerDetails():
    sim.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectDeliveryMethod():
    sim.selectDeliveryDetails()

def test_sendOTP():
    sim.sendOTP()
