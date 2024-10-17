from models.productionda import ATPrepaidPage

def test_select_atprepaid_store(page):
    '''Proceed with nearest store for at prepaid checkout'''
    prepaid = ATPrepaidPage(page)
    prepaid.navigate()
    prepaid.type_msisdn(prepaid.number)
    prepaid.available_number()
    prepaid.prepaid_select_available_number()
    prepaid.fill_customer_details()
    prepaid.select_nearest_store()

def test_checkout_atprepaid_store(page):
    '''Checkout at prepaid with nearest store inserting all valid data'''
    prepaid = ATPrepaidPage(page)
    prepaid.click_continue()