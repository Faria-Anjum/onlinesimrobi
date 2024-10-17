from models.ownertransfer import AirtelPage, AirtelOwnerTransferPage, AirtelOwnerTransferFormPage

def test_selectAirtelTransferOwnership(page):
    '''Transfer AT ownership option can be selected'''
    sim = AirtelPage(page)
    transfer = AirtelOwnerTransferPage(page)
    sim.navigate()
    transfer.findTransferOwnership()

def test_fillupAirtelCurrentCustomerDetails(page):
    '''Current customer details for AT ownership transfer filled'''
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.fillupCurrentCustomerDetails()

def test_fillUpAirtelNewCustomerDetails(page):
    '''New customer details for AT ownership transfer filled'''
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.fillUpNewCustomerDetails()

def test_selectAirtelTransferOwnershipMethod(page):
    '''Delivery method WIC selected for AT ownership transfer'''
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.selectPickupWIC()

def test_confirmAirtelTransferThroughOTP(page):
    '''Confirm button pressed, OTP received'''
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.sendOTP()