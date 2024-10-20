from models.main import RobiPage, AirtelPage, RobiFormPage
from playwright.sync_api import expect
import re

class RobiMNPPage(RobiPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/switchtorobi"

    def selectSwitchToRobi(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("Switch to Robi")).to_be_visible()
        expect(self.page.locator("div:nth-child(4) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(4) > .bg-gray-100 > a").click()

class RobiMNPFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/switchtorobi"
        self.combo = 2

class AirtelMNPPage(AirtelPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/switchtoairtel"

    def selectSwitchToRobi(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/airtel")
        expect(self.page.get_by_text("Switch to Airtel")).to_be_visible()
        expect(self.page.get_by_role("link", name="Order Now ").nth(2)).to_be_visible()
        self.page.get_by_role("link", name="Order Now ").nth(2).click()


class AirtelMNPFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/switchtoairtel"
        self.combo = 2

    

