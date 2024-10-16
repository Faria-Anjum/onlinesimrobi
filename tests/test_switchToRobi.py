from models.switchprovider import RobiPage, RobiMNPFormPage, RobiMNPPage

def test_selectSwitchToRobi(page):
    robi = RobiPage(page)
    mnp = RobiMNPPage(page)
    robi.navigate()
    mnp.selectSwitchToRobi()

def test_fillUpRobiMNPConnectionDetails(page):
    form = RobiMNPFormPage(page)
    form.fillMNPConnectionDetails()

def test_fillUpRobiMNPCustomerDetails(page):
    form = RobiMNPFormPage(page)
    form.fillUpCustomerDetails()

def test_selectRobiMNPDeliveryMethod(page):
    form = RobiMNPFormPage(page)
    form.selectHomeDelivery()

def test_confirmRobiMNPThroughOTP(page):
    form = RobiMNPFormPage(page)
    form.sendOTP()