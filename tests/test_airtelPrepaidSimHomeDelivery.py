from models.productionda import ATPrepaidPage

def test_select_atprepaid_home_delivery(page):
    '''Proceed with home delivery for at prepaid checkout'''
    prepaid = ATPrepaidPage(page)
    prepaid.navigate()
    prepaid.type_msisdn(prepaid.number)
    prepaid.available_number()
    prepaid.prepaid_select_available_number()
    prepaid.fill_customer_details()
    prepaid.select_home_delivery()

def test_checkout_atprepaid_home_delivery(page):
    '''Checkout with at prepaid home delivery inserting all valid data'''
    prepaid = ATPrepaidPage(page)
    prepaid.select_delivery_time()
    prepaid.click_continue()