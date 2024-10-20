#8801841254366
#cd /d E:\VSCode\onlinesimrobi\tests
#set PWDEBUG=1
#pytest -s

from models.main import RobiPage, AirtelPage, RobiFormPage
from playwright.sync_api import expect

class ReplaceRobiPage(RobiPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/upgrade-sim"
        
    def findReplaceSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("SIM Replacement")).to_be_visible()
        expect(self.page.locator("div:nth-child(5) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(5) > .bg-gray-100 > a").click()

class ReplaceRobiFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/replace-sim"
        self.combo = 1
        
    def selectSimDetails(self):
        expect(self.page.get_by_text("SIM Details")).to_be_visible()
        expect(self.page.get_by_placeholder("Replacement Number")).to_be_visible()
        self.page.get_by_placeholder("Replacement Number").click()
        self.page.get_by_placeholder("Replacement Number").fill("01846888883")

class ReplaceAirtelPage(AirtelPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/upgrade-sim"
        
    def findReplaceSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/airtel")
        expect(self.page.get_by_text("SIM Replacement")).to_be_visible()
        expect(self.page.get_by_role("link", name="Order Now ").nth(3)).to_be_visible()
        self.page.get_by_role("link", name="Order Now ").nth(3).click()

class ReplaceAirtelFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/replace-sim"
        self.combo = 1
        
    def selectSimDetails(self):
        expect(self.page.get_by_text("SIM Details")).to_be_visible()
        expect(self.page.get_by_placeholder("Replacement Number")).to_be_visible()
        self.page.get_by_placeholder("Replacement Number").click()
        self.page.get_by_placeholder("Replacement Number").fill("01846888883")
