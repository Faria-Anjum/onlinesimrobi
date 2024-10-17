from models.ownertransfer import RobiPage, RobiOwnerTransferPage, RobiOwnerTransferFormPage

def test_selectRobiTransferOwnership(page):
    '''Transfer Robi ownership option can be selected'''
    sim = RobiPage(page)
    transfer = RobiOwnerTransferPage(page)
    sim.navigate()
    transfer.findTransferOwnership()

def test_fillupRobiCurrentCustomerDetails(page):
    '''Current customer details for Robi ownership transfer filled'''
    transferform = RobiOwnerTransferFormPage(page)
    transferform.fillupCurrentCustomerDetails()

def test_fillUpRobiNewCustomerDetails(page):
    '''New customer details for Robi ownership transfer filled'''
    transferform = RobiOwnerTransferFormPage(page)
    transferform.fillUpNewCustomerDetails()

def test_selectRobiTransferOwnershipMethod(page):
    '''Delivery method WIC selected for Robi ownership transfer'''
    transferform = RobiOwnerTransferFormPage(page)
    transferform.selectPickupWIC()

def test_confirmRobiTransferThroughOTP(page):
    '''Confirm button pressed, OTP received'''
    transferform = RobiOwnerTransferFormPage(page)
    transferform.sendOTP()