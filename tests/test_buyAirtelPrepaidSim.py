from models.prepaidsim import AirtelPage, AirtelPrepaidPage, AirtelPrepaidFormPage

def test_selectAirtelPrepaidSim(page):
    airtel = AirtelPage(page)
    prepaid = AirtelPrepaidPage(page)
    airtel.navigate()
    prepaid.findPrepaidSim()
    prepaid.selectSimKnowMore()
    prepaid.selectSimOrderNow()

def test_selectAirtelPrepaidSimNumber(page):
    form = AirtelPrepaidFormPage(page)
    form.findSimNumber()
    form.selectSimNumber()

def test_fillUpAirtelPrepaidCustomerDetails(page):
    form = AirtelPrepaidFormPage(page)
    form.fillUpCustomerDetails()

def test_selectAirtelPrepaidDeliveryMethod(page):
    form = AirtelPrepaidFormPage(page)
    form.selectHomeDelivery()

def test_confirmAirtelPrepaidThroughOTP(page):
    form = AirtelPrepaidFormPage(page)
    form.sendOTP()
