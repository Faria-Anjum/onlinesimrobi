from models.upgradesim import AirtelPage, UpgradeAirtelPage, UpgradeAirtelFormPage

def test_selectUpgradeAirtel(page):
    airtel = AirtelPage(page)
    upgrade = UpgradeAirtelPage(page)
    airtel.navigate()
    upgrade.findUpgradeSim()

def test_selectUpgradeAirtelDetails(page):
    form = UpgradeAirtelFormPage(page)
    form.selectUpgradeSimDetails()

def test_fillUpUpgradeAirtelCustomerDetails(page):
    form = UpgradeAirtelFormPage(page)
    form.fillUpCustomerDetails()

def test_selectUpgradeAirtelDeliveryMethod(page):
    form = UpgradeAirtelFormPage(page)
    form.selectPickupWIC()

def test_confirmUpgradeAirtelThroughOTP(page):
    form = UpgradeAirtelFormPage(page)
    form.sendOTP()