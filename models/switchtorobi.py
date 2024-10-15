from models.onlinesimrobi import SimPage, FormPage
from playwright.sync_api import expect
import re

class MNPPage(SimPage):
    def findUpgradeSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("Switch to Robi")).to_be_visible()
        expect(self.page.locator("div:nth-child(4) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(4) > .bg-gray-100 > a").click()

class MNPFormPage(FormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/switchtorobi"
        self.delivery = "Home Delivery"

    def fillConnectionDetails(self):
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

    

    

