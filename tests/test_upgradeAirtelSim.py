from models.upgradesim import AirtelPage, UpgradeAirtelPage, UpgradeAirtelFormPage

def test_selectUpgradeAirtel(page):
    '''Upgrade AT sim option can be selected'''
    airtel = AirtelPage(page)
    upgrade = UpgradeAirtelPage(page)
    airtel.navigate()
    upgrade.findUpgradeSim()

def test_selectUpgradeAirtelDetails(page):
    '''Textbox accepts valid AT msisdn to be upgraded'''
    form = UpgradeAirtelFormPage(page)
    form.selectUpgradeSimDetails()

def test_fillUpUpgradeAirtelCustomerDetails(page):
    '''Customer details for AT sim upgrade filled'''
    form = UpgradeAirtelFormPage(page)
    form.fillUpCustomerDetails()

def test_selectUpgradeAirtelDeliveryMethod(page):
    '''Delivery method WIC selected for AT upgrade'''
    form = UpgradeAirtelFormPage(page)
    form.selectPickupWIC()

def test_confirmUpgradeAirtelThroughOTP(page):
    '''Confirm button pressed, OTP received'''
    form = UpgradeAirtelFormPage(page)
    form.sendOTP()