from models.onlinesimrobi import RobiPage
from models.switchtorobi import MNPFormPage, MNPPage

def test_selectSwitchToRobi(page):
    sim = RobiPage(page)
    mnp = MNPPage(page)
    sim.navigate()
    mnp.selectSwitchToRobi()

def test_fillUpMNPConnectionDetails(page):
    mnp = MNPFormPage(page)
    mnp.fillConnectionDetails()

def test_fillUpMNPCustomerDetails(page):
    mnp = MNPFormPage(page)
    mnp.fillUpCustomerDetails()

def test_selectMNPDeliveryMethod(page):
    mnp = MNPFormPage(page)
    mnp.selectHomeDelivery()

def test_confirmMNPThroughOTP(page):
    mnp = MNPFormPage(page)
    mnp.sendOTP()