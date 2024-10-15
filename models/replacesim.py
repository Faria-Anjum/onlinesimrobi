#8801841254366
#cd /d E:\VSCode\onlinesimrobi\tests
#set PWDEBUG=1
#pytest -s

from models.onlinesimrobi import RobiPage, RobiFormPage
from playwright.sync_api import expect

class ReplacePage(RobiPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/upgrade-sim"
        
    def findReplaceSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("SIM Replacement")).to_be_visible()
        expect(self.page.locator("div:nth-child(5) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(5) > .bg-gray-100 > a").click()

class ReplaceFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/replace-sim"
        self.combo = 1
        
    def selectSimDetails(self):
        expect(self.page.get_by_text("SIM Details")).to_be_visible()
        expect(self.page.get_by_placeholder("Replacement Number")).to_be_visible()
        self.page.get_by_placeholder("Replacement Number").click()
        self.page.get_by_placeholder("Replacement Number").fill("01846888883")
