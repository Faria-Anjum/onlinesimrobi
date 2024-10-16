from models.switchprovider import AirtelPage, AirtelMNPPage, AirtelMNPFormPage

def test_selectSwitchToAirtel(page):
    airtel = AirtelPage(page)
    mnp = AirtelMNPPage(page)
    airtel.navigate()
    mnp.selectSwitchToRobi()

def test_fillUpAirtelMNPConnectionDetails(page):
    form = AirtelMNPFormPage(page)
    form.fillMNPConnectionDetails()

def test_fillUpAirtelMNPCustomerDetails(page):
    form = AirtelMNPFormPage(page)
    form.fillUpCustomerDetails()

def test_selectAirtelMNPDeliveryMethod(page):
    form = AirtelMNPFormPage(page)
    form.selectHomeDelivery()

def test_confirmAirtelMNPThroughOTP(page):
    form = AirtelMNPFormPage(page)
    form.sendOTP()