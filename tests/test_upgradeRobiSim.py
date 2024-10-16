from models.upgradesim import RobiPage, UpgradeRobiPage, UpgradeRobiFormPage

def test_selectUpgradeRobi(page):
    robi = RobiPage(page)
    upgrade = UpgradeRobiPage(page)
    robi.navigate()
    upgrade.findUpgradeSim()

def test_selectUpgradeRobiDetails(page):
    form = UpgradeRobiFormPage(page)
    form.selectUpgradeSimDetails()

def test_fillUpUpgradeRobiCustomerDetails(page):
    form = UpgradeRobiFormPage(page)
    form.fillUpCustomerDetails()

def test_selectUpgradeRobiDeliveryMethod(page):
    form = UpgradeRobiFormPage(page)
    form.selectPickupWIC()

def test_confirmUpgradeRobiThroughOTP(page):
    form = UpgradeRobiFormPage(page)
    form.sendOTP()