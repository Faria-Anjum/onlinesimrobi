from models.replacesim import AirtelPage, ReplaceAirtelPage, ReplaceAirtelFormPage

def test_selectReplaceSim(page):
    airtel = AirtelPage(page)
    replace = ReplaceAirtelPage(page)
    airtel.navigate()
    replace.findReplaceSim()

def test_selectReplaceSimDetails(page):
    form = ReplaceAirtelFormPage(page)
    form.selectSimDetails()

def test_fillUpReplaceCustomerDetails(page):
    form = ReplaceAirtelFormPage(page)
    form.fillUpCustomerDetails()

def test_selecReplaceDeliveryMethod(page):
    form = ReplaceAirtelFormPage(page)
    form.selectPickupWIC()

def test_confirmReplaceThroughOTP(page):
    form = ReplaceAirtelFormPage(page)
    form.sendOTP()