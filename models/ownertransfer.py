from models.onlinesimrobi import RobiPage, AirtelPage, RobiFormPage
from playwright.sync_api import expect
import re

class RobiOwnerTransferPage(RobiPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/transfer-ownership"
        
    def findTransferOwnership(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("Ownership Transfer")).to_be_visible()
        expect(self.page.locator("div:nth-child(6) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(6) > .bg-gray-100 > a").click()

class RobiOwnerTransferFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/transfer-ownership"
        self.combo = 1

class AirtelOwnerTransferPage(AirtelPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/transfer-ownership"
        
    def findTransferOwnership(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/airtel")
        expect(self.page.get_by_text("Ownership Transfer")).to_be_visible()
        expect(self.page.get_by_role("link", name="Order Now ").nth(4)).to_be_visible()
        self.page.get_by_role("link", name="Order Now ").nth(4).click()

class AirtelOwnerTransferFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/transfer-ownership"
        self.combo = 1