#8801886325284
#cd /d E:\VSCode\onlinesimrobi\tests

from models.onlinesimrobi import SimPage, FormPage
from playwright.sync_api import expect

class PrepaidPage(SimPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/1/2227"
        
    def findPrepaidSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        assert self.page.get_by_text("Get A Prepaid SIM").is_visible()
        expect(self.page.locator(".bg-gray-100 > a").first).to_be_visible()
        self.page.locator(".bg-gray-100 > a").first.scroll_into_view_if_needed()
        self.page.locator(".bg-gray-100 > a").first.hover()
        self.page.locator(".bg-gray-100 > a").first.click()

class PrepaidFormPage(FormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/1/2227/registration"
        self.number = "329279"
        self.delivery = "Home Delivery"
        
    def selectSimNumber(self):
        expect(self.page.get_by_text("8801886329279", exact=True)).to_be_visible()
        self.page.locator("label").filter(has_text="8801886329279").click()

    # self.page.get_by_label("Please enter verification").click()
    # self.page.get_by_label("Please enter verification").fill("9")
    # self.page.get_by_label("Digit 2").fill("6")
    # self.page.get_by_label("Digit 3").fill("2")
    # self.page.get_by_label("Digit 4").fill("5")
    # self.page.get_by_label("Digit 5").fill("3")
    # self.page.get_by_label("Digit 6").fill("1")
    # self.page.get_by_role("button", name="Validate").click()
    # self.page.get_by_label("I have read & agreed with the").check()
    # self.page.get_by_role("button", name="Confirm Order").click()