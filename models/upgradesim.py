#8801841254366
#cd /d E:\VSCode\onlinesimrobi\tests
#set PWDEBUG=1
#pytest -s

from models.main import RobiPage, AirtelPage, RobiFormPage
from playwright.sync_api import expect
import re

class UpgradeRobiPage(RobiPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/upgrade-sim"
        
    def findUpgradeSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("Upgrade to 4.5G")).to_be_visible()
        expect(self.page.locator("div:nth-child(3) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(3) > .bg-gray-100 > a").click()

class UpgradeRobiFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/robi/upgrade-sim"
        self.combo = 1

class UpgradeAirtelPage(AirtelPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/upgrade-sim"
        
    def findUpgradeSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/airtel")
        expect(self.page.get_by_text("Upgrade to 4.5G")).to_be_visible()
        expect(self.page.get_by_role("link", name="Order Now ").nth(1)).to_be_visible()
        self.page.get_by_role("link", name="Order Now ").nth(1).click()

class UpgradeAirtelFormPage(RobiFormPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/airtel/upgrade-sim"
        self.combo = 1


#     expect(page.get_by_text("Customer Details")).to_be_visible()
#     page.get_by_placeholder("Enter Full Name").click()
#     page.get_by_placeholder("Enter Full Name").fill("Faria")
#     expect(page.get_by_text("Pickup from Nearest WIC")).to_be_visible()
#     expect(page.locator("label").filter(has_text="Pickup from Nearest WICPlease")).to_be_visible()
#     expect(page.get_by_text("Click here to find your")).to_be_visible()
#     with page.expect_popup() as page1_info:
#         page.get_by_text("Click here").click()
#     page1 = page1_info.value
#     page1.locator("div:nth-child(3) > div:nth-child(68)").click()
#     page1.close()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
