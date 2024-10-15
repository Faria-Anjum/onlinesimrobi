#8801841254366
#cd /d E:\VSCode\onlinesimrobi\tests
#set PWDEBUG=1
#pytest -s

from models.onlinesimrobi import SimPage, FormPage
from playwright.sync_api import expect
import re

class PostpaidPage(SimPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/2/3477"
        
    def findPostpaidSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("Get A Postpaid SIM")).to_be_visible()
        expect(self.page.locator("div:nth-child(2) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(2) > .bg-gray-100 > a").click()

class PostpaidFormPage(FormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/newconnection/2/3477/registration"
        self.number = "254366"
        self.delivery = "Home Delivery"

    # def selectSimOrderNow(self):
    #     expect(self.page.locator("div").filter(has_text=re.compile(r"^Robi Postpaid$"))).to_be_visible()
    #     expect(self.page.get_by_role("cell", name="Tariff Plan")).to_be_visible()
    #     FormPage.selectSimOrderNow()

    def selectSimNumber(self):
        expect(self.page.locator("label").filter(has_text="8801841254366")).to_be_visible()
        self.page.locator("label").filter(has_text="8801841254366").click()