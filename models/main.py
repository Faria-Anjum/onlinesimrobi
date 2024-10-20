# airtel +8801601567422

from playwright.sync_api import expect
import re

class RobiPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/"

    def navigate(self):
        self.page.goto(self.url, wait_until="load")
        
    def selectSimKnowMore(self):
        expect(self.page.get_by_role("link", name=" Know More")).to_be_visible()
        self.page.get_by_role("link", name=" Know More").click()
        expect(self.page).to_have_url(self.url)

    def selectSimOrderNow(self):
        expect(self.page.get_by_role("button", name="Order Now")).to_be_visible()
        self.page.get_by_role("button", name="Order Now").scroll_into_view_if_needed()
        self.page.get_by_role("button", name="Order Now").click()
        expect(self.page).to_have_url((self.url)+'/registration')

class AirtelPage(RobiPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/"

    def navigate(self):
        self.page.goto(self.url, wait_until="load")
        expect(self.page.get_by_role("link", name="Buy Airtel")).to_be_visible()
        self.page.get_by_role("link", name="Buy Airtel").click()
        expect(self.page).to_have_url((self.url)+'airtel')
        expect(self.page.get_by_role("link", name="Buy Robi")).to_be_visible()

class RobiFormPage:
    def __init__(self):
        self.combo = 1

    def findSimNumber(self):
        expect(self.page).to_have_url(self.url)
        expect(self.page.get_by_text("Choose SIM Number")).to_be_visible()
        self.page.get_by_text("Choose SIM Number").scroll_into_view_if_needed()
        expect(self.page.get_by_placeholder("XXXXXX", exact=True)).to_be_visible()
        self.page.get_by_placeholder("XXXXXX", exact=True).click()
        self.page.get_by_placeholder("XXXXXX", exact=True).fill(self.number)
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.get_by_text("is available!")).to_be_visible()

    def selectUpgradeSimDetails(self):
        expect(self.page.get_by_text("SIM Details")).to_be_visible()
        expect(self.page.get_by_placeholder("Number You Want To Upgrade")).to_be_visible()
        self.page.get_by_placeholder("Number You Want To Upgrade").click()
        self.page.get_by_placeholder("Number You Want To Upgrade").fill("01846888883")

    def fillMNPConnectionDetails(self):
        expect(self.page).to_have_url(self.url)
        expect(self.page.get_by_text("Connection Details")).to_be_visible()
        expect(self.page.get_by_text("Current Operator")).to_be_visible()
        expect(self.page.locator("label").filter(has_text="Banglalink")).to_be_visible()
        self.page.locator("label").filter(has_text="Banglalink").click()

        expect(self.page.locator("div").filter(has_text=re.compile(r"^Select Current Package Type$")).nth(2)).to_be_visible()
        self.page.locator("div").filter(has_text=re.compile(r"^Current Package TypeSelect Current Package Type$")).locator("span").nth(3).click()
        self.page.get_by_role("option", name="Prepaid").click()

        self.page.get_by_placeholder("Mobile Number For MNP").click()
        self.page.get_by_placeholder("Mobile Number For MNP").fill("01846888883")

    def fillupCurrentCustomerDetails(self):
        expect(self.page.get_by_text("Current Customer Details")).to_be_visible()
        self.page.get_by_placeholder("Enter Contact Number").click()
        self.page.get_by_placeholder("Enter Contact Number").fill("01846888883")

        self.page.locator("input[name=\"orderDto\\.sourceCustomerDetailsDto\\.nidNumber\"]").click()
        self.page.locator("input[name=\"orderDto\\.sourceCustomerDetailsDto\\.nidNumber\"]").fill("5436787654")

        self.page.locator("div").filter(has_text=re.compile(r"^Contact NumberNID NumberDate of Birth$")).get_by_placeholder("Enter Date of Birth").click()
        self.page.get_by_label("Choose Wednesday, October 4th,").click()

    def fillUpNewCustomerDetails(self):
        expect(self.page).to_have_url(self.url)
        expect(self.page.get_by_text("New Customer Details")).to_be_visible()
        self.page.get_by_text("New Customer Details").scroll_into_view_if_needed()

        expect(self.page.get_by_placeholder("Enter Full Name")).to_be_visible()
        self.page.get_by_placeholder("Enter Full Name").click()
        self.page.get_by_placeholder("Enter Full Name").fill("Faria Anjum")

        expect(self.page.get_by_placeholder("Enter Date of Birth").nth(1)).to_be_visible()
        self.page.get_by_placeholder("Enter Date of Birth").nth(1).click()

        self.page.get_by_placeholder("Enter Date of Birth").nth(1).click()
        self.page.get_by_role("combobox").nth(self.combo).select_option("1999")
        self.page.locator("div").filter(has_text=re.compile(r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role("combobox").select_option("2")
        self.page.get_by_label("Choose Monday, March 22nd,").click()

        expect(self.page.get_by_text("Select Gender")).to_be_visible()
        #expect(self.page.locator("div").filter(has_text=re.compile(r"^Select Gender$")).nth(3)).to_be_visible()
        self.page.get_by_text("Select Gender").click()
        self.page.get_by_role("option", name="Female").click()

        self.page.locator("input[name=\"orderDto\\.customerDetail\\.nidNumber\"]").click()
        self.page.locator("input[name=\"orderDto\\.customerDetail\\.nidNumber\"]").fill("7898985437")

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
    
    def fillUpCustomerDetails(self):
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
        self.page.get_by_role("combobox").nth(self.combo).select_option("1999")
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

    def selectHomeDelivery(self):
        expect(self.page.get_by_text("Delivery Method")).to_be_visible()
        expect(self.page.locator("label").filter(has_text="Home Delivery")).to_be_visible()

        self.page.locator("label").filter(has_text="Home Delivery").click()

        self.page.get_by_placeholder("Select Date").click()
        self.page.get_by_label("Choose Sunday, October 20th,").click()

        self.page.get_by_placeholder("Time").click()
        self.page.get_by_role("option", name="11:00").click()

    def selectPickupWIC(self):
        expect(self.page.get_by_text("Delivery Method")).to_be_visible()
        expect(self.page.locator("label").filter(has_text="Pickup from Nearest WIC")).to_be_visible()
        self.page.locator("label").filter(has_text="Pickup from Nearest WIC").click()

    def sendOTP(self):
        self.page.get_by_role("button", name="Continue").click()
        expect(self.page.get_by_text("Insert OTP")).to_be_visible()
        