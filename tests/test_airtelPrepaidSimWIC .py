from models.da_tests import ATPrepaidPage

def test_select_atprepaid_wic(page):
    '''Proceed with nearest wic for at prepaid checkout'''
    prepaid = ATPrepaidPage(page)
    prepaid.navigate()
    prepaid.type_msisdn(prepaid.number)
    prepaid.available_number()
    prepaid.prepaid_select_available_number()
    prepaid.fill_customer_details()
    prepaid.select_nearest_wic()

def test_checkout_atprepaid_wic(page):
    '''Checkout at prepaid with nearest wic inserting all valid data'''
    prepaid = ATPrepaidPage(page)
    prepaid.click_continue()