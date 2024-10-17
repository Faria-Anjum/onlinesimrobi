from models.productionda import PostpaidPage

def test_select_postpaid_home_delivery(page):
    postpaid = PostpaidPage(page)
    postpaid.navigate()
    postpaid.type_msisdn(postpaid.number)
    postpaid.available_number()
    postpaid.postpaid_select_available_number()
    postpaid.fill_customer_details()
    postpaid.select_home_delivery()

def test_checkout_postpaid_home_delivery(page):
    postpaid = PostpaidPage(page)
    postpaid.select_delivery_time()
    postpaid.click_continue()

