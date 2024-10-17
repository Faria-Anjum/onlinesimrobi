from models.productionda import PostpaidPage

def test_select_postpaid_store(page):
    '''Checkout with nearest store inserting all valid data'''
    postpaid = PostpaidPage(page)
    postpaid.navigate()
    postpaid.type_msisdn(postpaid.number)
    postpaid.available_number()
    postpaid.postpaid_select_available_number()
    postpaid.fill_customer_details()
    postpaid.select_nearest_store()

def test_checkout_postpaid_store(page):
    '''Checkout robi prepaid with nearest store inserting all valid data'''
    postpaid = PostpaidPage(page)
    postpaid.click_continue()