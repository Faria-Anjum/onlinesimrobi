from models.onlinesimrobi import SimPage, FormPage
from playwright.sync_api import expect
import re

class OwnerTransferPage(SimPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/transfer-ownership"
        
    def findTransferOwnership(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("Ownership Transfer")).to_be_visible()
        expect(self.page.locator("div:nth-child(6) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(6) > .bg-gray-100 > a").click()

class OwnerTransferFormPage(FormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/transfer-ownership"
        self.combo = 1

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

# expect(page.get_by_text("Ownership Transfer")).to_be_visible()
# expect(page.locator("div:nth-child(6) > .bg-gray-100 > a")).to_be_visible()
# page.locator("div:nth-child(6) > .bg-gray-100 > a").click()
# expect(page.get_by_text("Current Customer Details")).to_be_visible()
# page.get_by_placeholder("Enter Contact Number").click()
# page.get_by_placeholder("Enter Contact Number").fill("01846888883")
# page.locator("input[name=\"orderDto\\.sourceCustomerDetailsDto\\.nidNumber\"]").click()
# page.locator("input[name=\"orderDto\\.sourceCustomerDetailsDto\\.nidNumber\"]").fill("5436787654")
# page.locator("div").filter(has_text=re.compile(r"^Contact NumberNID NumberDate of Birth$")).get_by_placeholder("Enter Date of Birth").click()
# page.get_by_label("Choose Wednesday, October 4th,").click()
# page.get_by_placeholder("Enter Full Name").click()
# page.get_by_placeholder("Enter Date of Birth").nth(1).click()
# page.get_by_text("891011121314").click()