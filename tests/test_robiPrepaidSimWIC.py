from models.productionda import PrepaidPage

def test_select_prepaid_wic(page):
    prepaid = PrepaidPage(page)
    prepaid.navigate()
    prepaid.type_msisdn(prepaid.number)
    prepaid.available_number()
    prepaid.prepaid_select_available_number()
    prepaid.fill_customer_details()
    prepaid.select_nearest_wic()

def test_checkout_prepaid_wic(page):
    prepaid = PrepaidPage(page)
    prepaid.click_continue()