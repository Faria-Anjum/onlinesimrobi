from models.onlinesimrobi import RobiPage 
from models.upgradesim import UpgradePage, UpgradeFormPage

def test_selectUpgradeSim(page):
    sim = RobiPage(page)
    upgrade = UpgradePage(page)
    sim.navigate()
    upgrade.findUpgradeSim()

def test_selectUpgradeSimDetails(page):
    sim = UpgradeFormPage(page)
    sim.selectSimDetails()

def test_fillUpUpgradeCustomerDetails(page):
    sim = UpgradeFormPage(page)
    sim.fillUpCustomerDetails()

def test_selectUpgradeDeliveryMethod(page):
    sim = UpgradeFormPage(page)
    sim.selectPickupWIC()

def test_confirmUpgradeThroughOTP(page):
    sim = UpgradeFormPage(page)
    sim.sendOTP()