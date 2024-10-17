from playwright.sync_api import expect
import re

class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/"

    def navigate(self):
        self.page.goto(self.url, wait_until="load")

    def navigate_to_airtel(self):
        self.page.get_by_text("Buy Airtel").click()

    def launchrobi(self):
        expect(self.page).to_have_url((self.url)+'robi')

    def launchairtel(self):
        expect(self.page).to_have_url((self.url)+'airtel')

    def validaterobi(self):
        assert self.page.get_by_text("Buy Airtel").is_visible()

    def validateairtel(self):
        assert self.page.get_by_text("Buy Robi").is_visible()

    def order_visibility(self):
        assert self.page.get_by_text("Track Order").is_visible()

    def order_functionality(self):
        self.page.get_by_text("Track Order").click()
        assert self.page.get_by_text("Track Your Order").is_visible()

class PrepaidInfoPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/1"
        self.link = '/2227'

    def prepaid_visibility(self):
        assert self.page.get_by_text("Get A Prepaid SIM").is_visible()
        assert self.page.locator(".bg-gray-100 > a").first.is_visible()
        self.page.locator(".bg-gray-100 > a").first.click()
        expect(self.page).to_have_url(self.url)

    def know_details(self):
        expect(self.page).to_have_url(self.url)
        assert self.page.get_by_role("link", name=" Know More").is_visible()
        self.page.get_by_role("link", name=" Know More").click()
        expect(self.page).to_have_url(self.url+self.link)

    def order_now(self):
        expect(self.page).to_have_url(self.url)
        expect(self.page.get_by_role("button", name="Order Now")).to_be_visible()
        self.page.get_by_role("button", name="Order Now").click()
        expect(self.page).to_have_url(self.url+self.link+'/registration')

class ATPrepaidInfoPage(PrepaidInfoPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/newconnection/1"
        self.link = '/2852'

    def prepaid_visibility(self):
        assert self.page.get_by_text("Get A Prepaid SIM").is_visible()
        assert self.page.locator(".bg-gray-100 > a").first.is_visible()
        self.page.locator(".bg-gray-100 > a").first.click()
        expect(self.page).to_have_url(self.url)

class PostpaidInfoPage(PrepaidInfoPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/2"
        self.link = '/3477'

    def postpaid_visibility(self):
        expect(self.page.get_by_text("Get A Postpaid SIM")).to_be_visible()
        expect(self.page.locator("div:nth-child(2) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(2) > .bg-gray-100 > a").click()
        expect(self.page).to_have_url(self.url)

class PrepaidPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/1/2227/registration"
        self.number = "329279"
        self.wrongNumber = "329277"

    def navigate(self):
        self.page.goto(self.url, wait_until='load')

    def type_msisdn(self, number):
        expect(self.page).to_have_url(self.url)
        expect(self.page.get_by_text("Choose SIM Number")).to_be_visible()
        assert self.page.get_by_placeholder("XXXXXX", exact=True).is_visible()
        self.page.get_by_placeholder("XXXXXX", exact=True).click()
        self.page.get_by_placeholder("XXXXXX", exact=True).fill(number)
        expect(self.page.get_by_placeholder("XXXXXX", exact=True)).to_have_value(number)

    def available_number(self):
        expect(self.page.get_by_placeholder("XXXXXX", exact=True)).to_have_value(self.number)
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.get_by_text("is available!")).to_be_visible()

    def prepaid_select_available_number(self):
        expect(self.page.get_by_text("8801886329279", exact=True)).to_be_visible()
        self.page.locator("label").filter(has_text="8801886329279").click()

    def unavailable_number(self):
        expect(self.page.get_by_placeholder("XXXXXX", exact=True)).to_have_value(self.wrongNumber)
        self.page.get_by_role("button", name="Search").click()
        
        expect(self.page.get_by_text("Sorry! Your desired mobile")).to_be_visible()

    def click_refresh(self):
        self.page.locator(".da-loading-arrow").click()
        #expect(self.page.get_by_text("No numbers found")).to_be_visible()
        assert self.page.get_by_text("Suggested Numbers").is_visible()

    def fill_customer_details(self):
        expect(self.page).to_have_url(self.url)
        expect(self.page.get_by_text("Customer Details")).to_be_visible()
        self.page.get_by_text("Customer Details").scroll_into_view_if_needed()

        expect(self.page.get_by_placeholder("Enter Full Name")).to_be_visible()
        self.page.get_by_placeholder("Enter Full Name").click()
        self.page.get_by_placeholder("Enter Full Name").fill("Faria Anjum")

        expect(self.page.get_by_placeholder("01XXXXXXXXX")).to_be_visible()
        self.page.get_by_placeholder("01XXXXXXXXX").click()
        self.page.get_by_placeholder("01XXXXXXXXX").fill("01846888883")

        expect(self.page.get_by_placeholder("Enter Date of Birth")).to_be_visible()
        self.page.get_by_placeholder("Enter Date of Birth").click()

        self.page.get_by_placeholder("Enter Date of Birth").click()
        self.page.get_by_role("combobox").nth(1).select_option("1999")
        self.page.locator("div").filter(has_text=re.compile(r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role("combobox").select_option("2")
        self.page.get_by_label("Choose Monday, March 22nd,").click()

        expect(self.page.get_by_text("Select Gender")).to_be_visible()
        #expect(self.page.locator("div").filter(has_text=re.compile(r"^Select Gender$")).nth(3)).to_be_visible()
        self.page.get_by_text("Select Gender").click()
        self.page.get_by_role("option", name="Female").click()

        expect(self.page.get_by_placeholder("Enter NID Number")).to_be_visible()
        self.page.get_by_placeholder("Enter NID Number").click()
        self.page.get_by_placeholder("Enter NID Number").fill("7898985437")

        expect(self.page.locator("div").filter(has_text=re.compile(r"^Select District$")).nth(2)).to_be_visible()
        self.page.locator("div").filter(has_text=re.compile(r"^Select District$")).nth(2).click()
        #self.page.locator("#react-select-3-input").fill("D")
        expect(self.page.get_by_role("option", name="Dhaka")).to_be_visible()
        self.page.get_by_role("option", name="Dhaka").click()

        self.page.get_by_text("Select Thana").click()
        self.page.get_by_role("option", name="Mirpur").click()

        self.page.get_by_placeholder("Enter House No").click()
        self.page.get_by_placeholder("Enter House No").fill("4")

        self.page.get_by_placeholder("Enter Road").click()
        self.page.get_by_placeholder("Enter Road").fill("6")

        self.page.get_by_placeholder("Enter Area").click()
        self.page.get_by_placeholder("Enter Area").fill("Mirpur")

        self.page.locator("div").filter(has_text=re.compile(r"^Select Post Code$")).nth(1).click()
        self.page.get_by_role("option", name="1216").click()

    def select_home_delivery(self):
        expect(self.page.get_by_text("Delivery Method")).to_be_visible()
        expect(self.page.locator("label").filter(has_text="Home Delivery")).to_be_visible()
        self.page.locator("label").filter(has_text="Home Delivery").click()

    def select_delivery_time(self):
        expect(self.page.get_by_placeholder("Select Date")).to_be_visible()
        self.page.get_by_placeholder("Select Date").click()
        self.page.get_by_label("Choose Sunday, October 20th,").click()

        expect(self.page.get_by_placeholder("Time")).to_be_visible()
        self.page.get_by_placeholder("Time").click()
        self.page.get_by_role("option", name="11:00").click()

    def select_nearest_wic(self):
        expect(self.page.get_by_text("Delivery Method")).to_be_visible()
        expect(self.page.locator("label").filter(has_text="Pickup from Nearest WIC")).to_be_visible()
        self.page.locator("label").filter(has_text="Pickup from Nearest WIC").click()

    def select_nearest_store(self):
        expect(self.page.get_by_text("Delivery Method")).to_be_visible()
        expect(self.page.locator("label").filter(has_text="Pickup from Nearest Store")).to_be_visible()
        self.page.locator("label").filter(has_text="Pickup from Nearest Store").click()

    def click_continue(self):
        self.page.get_by_role("button", name="Continue").click()
        expect(self.page.get_by_text("Insert OTP")).to_be_visible()

class ATPrepaidPage(PrepaidPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/newconnection/1/2852/registration"
        self.number = "567422"
        self.wrongNumber = "254444"

    def prepaid_select_available_number(self):
        expect(self.page.locator("label").filter(has_text="8801601567422")).to_be_visible()
        self.page.locator("label").filter(has_text="8801601567422").click()

class PostpaidPage(PrepaidPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/2/3477/registration"
        self.number = "254366"
        self.wrongNumber = "254444"

    def postpaid_select_available_number(self):
        expect(self.page.locator("label").filter(has_text="8801841254366")).to_be_visible()
        self.page.locator("label").filter(has_text="8801841254366").click()