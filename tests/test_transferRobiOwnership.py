from models.ownertransfer import RobiPage, RobiOwnerTransferPage, RobiOwnerTransferFormPage

def test_selectRobiTransferOwnership(page):
    sim = RobiPage(page)
    transfer = RobiOwnerTransferPage(page)
    sim.navigate()
    transfer.findTransferOwnership()

def test_fillupRobiCurrentCustomerDetails(page):
    transferform = RobiOwnerTransferFormPage(page)
    transferform.fillupCurrentCustomerDetails()

def test_fillUpRobiNewCustomerDetails(page):
    transferform = RobiOwnerTransferFormPage(page)
    transferform.fillUpNewCustomerDetails()

def test_selectRobiTransferOwnershipMethod(page):
    transferform = RobiOwnerTransferFormPage(page)
    transferform.selectPickupWIC()

def test_confirmRobiTransferThroughOTP(page):
    transferform = RobiOwnerTransferFormPage(page)
    transferform.sendOTP()