from models.upgradesim import RobiPage, UpgradeRobiPage, UpgradeRobiFormPage

def test_selectUpgradeRobi(page):
    '''Upgrade Robi sim option can be selected'''
    robi = RobiPage(page)
    upgrade = UpgradeRobiPage(page)
    robi.navigate()
    upgrade.findUpgradeSim()

def test_selectUpgradeRobiDetails(page):
    '''Textbox accepts valid Robi msisdn to be upgraded'''
    form = UpgradeRobiFormPage(page)
    form.selectUpgradeSimDetails()

def test_fillUpUpgradeRobiCustomerDetails(page):
    '''Customer details for Robi sim upgrade filled'''
    form = UpgradeRobiFormPage(page)
    form.fillUpCustomerDetails()

def test_selectUpgradeRobiDeliveryMethod(page):
    '''Delivery method WIC selected for AT upgrade'''
    form = UpgradeRobiFormPage(page)
    form.selectPickupWIC()

def test_confirmUpgradeRobiThroughOTP(page):
    '''Confirm button pressed'''
    form = UpgradeRobiFormPage(page)
    form.sendOTP()