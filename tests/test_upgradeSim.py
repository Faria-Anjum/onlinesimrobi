from models.onlinesimrobi import SimPage 
from models.upgradesim import UpgradePage, UpgradeFormPage

def test_selectUpgradeSim(page):
    sim = SimPage(page)
    upgrade = UpgradePage(page)
    sim.navigate()
    upgrade.findUpgradeSim()

def test_selectSimDetails(page):
    sim = UpgradeFormPage(page)
    sim.selectSimDetails()

def test_fillUpCustomerDetails(page):
    sim = UpgradeFormPage(page)
    sim.fillUpCustomerDetails()

def test_selectDeliveryMethod(page):
    sim = UpgradeFormPage(page)
    sim.selectDeliveryDetails()

def test_confirmDeliveryThroughOTP(page):
    sim = UpgradeFormPage(page)
    sim.sendOTP()