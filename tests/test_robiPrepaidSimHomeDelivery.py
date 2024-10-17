from models.productionda import PrepaidPage

def test_select_prepaid_home_delivery(page):
    '''Proceed with home delivery for robi prepaid checkout'''
    prepaid = PrepaidPage(page)
    prepaid.navigate()
    prepaid.type_msisdn(prepaid.number)
    prepaid.available_number()
    prepaid.prepaid_select_available_number()
    prepaid.fill_customer_details()
    prepaid.select_home_delivery()

def test_checkout_prepaid_home_delivery(page):
    '''Checkout with robi prepaid home delivery inserting all valid data'''
    prepaid = PrepaidPage(page)
    prepaid.select_delivery_time()
    prepaid.click_continue()