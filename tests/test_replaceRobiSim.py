from models.replacesim import RobiPage, ReplaceRobiPage, ReplaceRobiFormPage

def test_selectReplaceSim(page):
    '''Relace Robi sim option can be selected'''
    robi = RobiPage(page)
    replace = ReplaceRobiPage(page)
    robi.navigate()
    replace.findReplaceSim()

def test_selectReplaceSimDetails(page):
    '''Details to replace Robi sim can be filled'''
    form = ReplaceRobiFormPage(page)
    form.selectSimDetails()

def test_fillUpReplaceCustomerDetails(page):
    '''Current customer details for Robi replace can be filled'''
    form = ReplaceRobiFormPage(page)
    form.fillUpCustomerDetails()

def test_selecReplaceDeliveryMethod(page):
    '''Home delivery method selected for Robi replace'''
    form = ReplaceRobiFormPage(page)
    form.selectPickupWIC()

def test_confirmReplaceThroughOTP(page):
    '''Confirm button pressed, OTP received'''
    form = ReplaceRobiFormPage(page)
    form.sendOTP()