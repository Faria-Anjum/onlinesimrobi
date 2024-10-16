from models.ownertransfer import AirtelPage, AirtelOwnerTransferPage, AirtelOwnerTransferFormPage

def test_selectAirtelTransferOwnership(page):
    sim = AirtelPage(page)
    transfer = AirtelOwnerTransferPage(page)
    sim.navigate()
    transfer.findTransferOwnership()

def test_fillupAirtelCurrentCustomerDetails(page):
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.fillupCurrentCustomerDetails()

def test_fillUpAirtelNewCustomerDetails(page):
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.fillUpNewCustomerDetails()

def test_selectAirtelTransferOwnershipMethod(page):
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.selectPickupWIC()

def test_confirmAirtelTransferThroughOTP(page):
    transferform = AirtelOwnerTransferFormPage(page)
    transferform.sendOTP()