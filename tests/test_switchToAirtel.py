from models.switchprovider import AirtelPage, AirtelMNPPage, AirtelMNPFormPage

def test_selectSwitchToAirtel(page):
    '''Switch to AT option can be selected'''
    airtel = AirtelPage(page)
    mnp = AirtelMNPPage(page)
    airtel.navigate()
    mnp.selectSwitchToRobi()

def test_fillUpAirtelMNPConnectionDetails(page):
    '''Current SIM details for AT MNP can be filled'''
    form = AirtelMNPFormPage(page)
    form.fillMNPConnectionDetails()

def test_fillUpAirtelMNPCustomerDetails(page):
    '''Current customer details for AT MNP can be filled'''
    form = AirtelMNPFormPage(page)
    form.fillUpCustomerDetails()

def test_selectAirtelMNPDeliveryMethod(page):
    '''Home delivery method selected for AT MNP'''
    form = AirtelMNPFormPage(page)
    form.selectHomeDelivery()

def test_confirmAirtelMNPThroughOTP(page):
    '''Confirm button pressed, OTP received'''
    form = AirtelMNPFormPage(page)
    form.sendOTP()