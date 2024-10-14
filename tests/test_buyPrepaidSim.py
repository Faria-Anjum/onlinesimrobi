from models.prepaidsim import PrepaidPage, PreDeliveryPage

def test_selectPrepaidSim(page):
    prepaid = PrepaidPage(page)
    prepaid.navigate()
    prepaid.findPrepaidSim()
    prepaid.selectPrepaidSimKnowMore()
    prepaid.selectPrepaidSimOrderNow()

def test_selectSimNumber(page):
    sim = PreDeliveryPage(page)
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpCustomerDetails(page):
    sim = PreDeliveryPage(page)
    sim.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectDeliveryMethod(page):
    sim = PreDeliveryPage(page)
    sim.selectDeliveryDetails()

def test_confirmDeliveryThroughOTP(page):
    sim = PreDeliveryPage(page)
    sim.sendOTP()
