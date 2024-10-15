# +8801601567422

from playwright.sync_api import expect
import re

class AirtelPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://onlinesim.robi.com.bd/"

#import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://onlinesim.robi.com.bd/")
#     page.goto("https://onlinesim.robi.com.bd/robi")
#     expect(page.get_by_role("link", name="Buy Airtel")).to_be_visible()
#     page.get_by_role("link", name="Buy Airtel").click()
#     expect(page.get_by_role("link", name="Buy Robi")).to_be_visible()
#     expect(page.get_by_text("Get A Prepaid SIM")).to_be_visible()
#     expect(page.get_by_role("link", name="Order Now ").first).to_be_visible()
#     page.get_by_role("link", name="Order Now ").first.click()
#     expect(page.get_by_role("link", name=" Know More")).to_be_visible()
#     page.get_by_role("link", name=" Know More").click()
#     expect(page.get_by_role("button", name="Order Now")).to_be_visible()
#     page.get_by_role("button", name="Order Now").click()
#     page.get_by_placeholder("XXXXXX", exact=True).click()
#     page.get_by_placeholder("XXXXXX", exact=True).fill("567422")
#     page.get_by_role("button", name="Search").click()
#     expect(page.locator("label").filter(has_text="8801601567422")).to_be_visible()
#     page.get_by_placeholder("Enter Full Name").click()
#     page.get_by_placeholder("01XXXXXXXXX").click()
#     page.get_by_placeholder("Enter Date of Birth").click()
#     page.get_by_text("1234567").click()
#     page.get_by_placeholder("Enter NID Number").click()
#     page.locator("div").filter(has_text=re.compile(r"^Select Gender$")).nth(3).click()
#     page.locator(".da-arrow-down").first.click()
#     page.locator("div").filter(has_text=re.compile(r"^Select Gender$")).nth(3).click()
#     page.get_by_placeholder("Enter Email").click()
