from models.onlinesimrobi import SimPage 
from models.replacesim import ReplacePage, ReplaceFormPage

def test_selectReplaceSim(page):
    sim = SimPage(page)
    replace = ReplacePage(page)
    sim.navigate()
    replace.findReplaceSim()

def test_selectReplaceSimDetails(page):
    replace = ReplaceFormPage(page)
    replace.selectSimDetails()

def test_fillUpReplaceCustomerDetails(page):
    replace = ReplaceFormPage(page)
    replace.fillUpCustomerDetails()

def test_selecReplaceDeliveryMethod(page):
    replace = ReplaceFormPage(page)
    replace.selectPickupWIC()

def test_confirmReplaceThroughOTP(page):
    replace = ReplaceFormPage(page)
    replace.sendOTP()