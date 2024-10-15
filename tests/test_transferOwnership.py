from models.onlinesimrobi import RobiPage 
from models.ownertransfer import OwnerTransferPage, OwnerTransferFormPage

def test_selectTransferOwnership(page):
    sim = RobiPage(page)
    transfer = OwnerTransferPage(page)
    sim.navigate()
    transfer.findTransferOwnership()

def test_fillupCurrentCustomerDetails(page):
    transferform = OwnerTransferFormPage(page)
    transferform.fillupCurrentCustomerDetails()

def test_fillUpNewCustomerDetails(page):
    transferform = OwnerTransferFormPage(page)
    transferform.fillUpNewCustomerDetails()

def test_selectTransferOwnershipMethod(page):
    transferform = OwnerTransferFormPage(page)
    transferform.selectPickupWIC()

def test_confirmTransferThroughOTP(page):
    transferform = OwnerTransferFormPage(page)
    transferform.sendOTP()