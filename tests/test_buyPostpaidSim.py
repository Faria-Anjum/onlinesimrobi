#01841254366

from models.postpaidsim import PostpaidPage, PostDeliveryPage

def test_selectPostpaidSim(page):
    postpaid = PostpaidPage(page)
    postpaid.navigate()
    postpaid.findPostpaidSim()
    postpaid.selectPostpaidSimKnowMore()
    postpaid.selectPostpaidSimOrderNow()

def test_selectSimNumber(page):
    sim = PostDeliveryPage(page)
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpCustomerDetails(page):
    sim = PostDeliveryPage(page)
    sim.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectDeliveryMethod(page):
    sim = PostDeliveryPage(page)
    sim.selectDeliveryDetails()

def test_confirmDeliveryThroughOTP(page):
    sim = PostDeliveryPage(page)
    sim.sendOTP()

