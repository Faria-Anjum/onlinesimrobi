from models.replacesim import RobiPage, ReplaceRobiPage, ReplaceRobiFormPage

def test_selectReplaceSim(page):
    robi = RobiPage(page)
    replace = ReplaceRobiPage(page)
    robi.navigate()
    replace.findReplaceSim()

def test_selectReplaceSimDetails(page):
    form = ReplaceRobiFormPage(page)
    form.selectSimDetails()

def test_fillUpReplaceCustomerDetails(page):
    form = ReplaceRobiFormPage(page)
    form.fillUpCustomerDetails()

def test_selecReplaceDeliveryMethod(page):
    form = ReplaceRobiFormPage(page)
    form.selectPickupWIC()

def test_confirmReplaceThroughOTP(page):
    form = ReplaceRobiFormPage(page)
    form.sendOTP()