from models.replacesim import AirtelPage, ReplaceAirtelPage, ReplaceAirtelFormPage

def test_selectReplaceSim(page):
    '''Relace AT sim option can be selected'''
    airtel = AirtelPage(page)
    replace = ReplaceAirtelPage(page)
    airtel.navigate()
    replace.findReplaceSim()

def test_selectReplaceSimDetails(page):
    '''Details to replace AT sim can be filled'''
    form = ReplaceAirtelFormPage(page)
    form.selectSimDetails()

def test_fillUpReplaceCustomerDetails(page):
    '''Current customer details for AT replace can be filled'''
    form = ReplaceAirtelFormPage(page)
    form.fillUpCustomerDetails()

def test_selecReplaceDeliveryMethod(page):
    '''Home delivery method selected for AT replace'''
    form = ReplaceAirtelFormPage(page)
    form.selectPickupWIC()

def test_confirmReplaceThroughOTP(page):
    '''Confirm button pressed, OTP received'''
    form = ReplaceAirtelFormPage(page)
    form.sendOTP()