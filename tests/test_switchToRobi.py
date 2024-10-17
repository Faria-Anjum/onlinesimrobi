from models.switchprovider import RobiPage, RobiMNPFormPage, RobiMNPPage

def test_selectSwitchToRobi(page):
    '''Switch to Robi option can be selected'''
    robi = RobiPage(page)
    mnp = RobiMNPPage(page)
    robi.navigate()
    mnp.selectSwitchToRobi()

def test_fillUpRobiMNPConnectionDetails(page):
    '''Current SIM details for Robi MNP can be filled'''
    form = RobiMNPFormPage(page)
    form.fillMNPConnectionDetails()

def test_fillUpRobiMNPCustomerDetails(page):
    '''Current customer details for Robi MNP can be filled'''
    form = RobiMNPFormPage(page)
    form.fillUpCustomerDetails()

def test_selectRobiMNPDeliveryMethod(page):
    '''Home delivery method selected for Robi MNP'''
    form = RobiMNPFormPage(page)
    form.selectHomeDelivery()

def test_confirmRobiMNPThroughOTP(page):
    '''Confirm button pressed, OTP received'''
    form = RobiMNPFormPage(page)
    form.sendOTP()