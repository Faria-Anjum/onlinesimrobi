#8801841254366
#cd /d E:\VSCode\onlinesimrobi\tests

from playwright.sync_api import expect
import re

class PostpaidPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://onlinesim.robi.com.bd/", wait_until="load")
        
    def findPostpaidSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        expect(self.page.get_by_text("Get A Postpaid SIM")).to_be_visible()
        expect(self.page.locator("div:nth-child(2) > .bg-gray-100 > a")).to_be_visible()
        self.page.locator("div:nth-child(2) > .bg-gray-100 > a").click()
        
    def selectPostpaidSimKnowMore(self):
        expect(self.page.get_by_role("link", name=" Know More")).to_be_visible()
        self.page.get_by_role("link", name=" Know More").click()
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/2/3477")

    def selectPostpaidSimOrderNow(self):
        expect(self.page.locator("div").filter(has_text=re.compile(r"^Robi Postpaid$"))).to_be_visible()
        expect(self.page.get_by_role("cell", name="Tariff Plan")).to_be_visible()
        expect(self.page.get_by_role("button", name="Order Now")).to_be_visible()
        self.page.get_by_role("button", name="Order Now").scroll_into_view_if_needed()
        self.page.get_by_role("button", name="Order Now").click()
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/2/3477/registration")

class PostDeliveryPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://onlinesim.robi.com.bd/robi/newconnection/2/3477", wait_until="load")

    def findSimNumber(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/2/3477/registration")
        expect(self.page.get_by_text("Choose SIM Number")).to_be_visible()
        self.page.get_by_text("Choose SIM Number").scroll_into_view_if_needed()
        expect(self.page.get_by_placeholder("XXXXXX", exact=True)).to_be_visible()
        self.page.get_by_placeholder("XXXXXX", exact=True).click()
        self.page.get_by_placeholder("XXXXXX", exact=True).fill("254366")
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.get_by_text("is available!")).to_be_visible()
        
    def selectSimNumber(self):
        expect(self.page.locator("label").filter(has_text="8801841254366")).to_be_visible()
        self.page.locator("label").filter(has_text="8801841254366").click()

    def fillUpCustomerDetails(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/2/3477/registration")
        expect(self.page.get_by_text("Customer Details")).to_be_visible()
        self.page.get_by_text("Customer Details").scroll_into_view_if_needed()

        expect(self.page.get_by_placeholder("Enter Full Name")).to_be_visible()
        self.page.get_by_placeholder("Enter Full Name").click()
        self.page.get_by_placeholder("Enter Full Name").fill("Faria Anjum")

        expect(self.page.get_by_placeholder("01XXXXXXXXX")).to_be_visible()
        self.page.get_by_placeholder("01XXXXXXXXX").click()
        self.page.get_by_placeholder("01XXXXXXXXX").fill("01846888883")

        expect(self.page.get_by_placeholder("Enter Date of Birth")).to_be_visible()
        self.page.get_by_placeholder("Enter Date of Birth").click()

        expect(self.page.get_by_role("combobox").nth(1)).to_be_visible()
        self.page.get_by_role("combobox").nth(1).select_option("1988")
        self.page.get_by_label("Choose Thursday, October 13th,").click()

        expect(self.page.locator("div").filter(has_text=re.compile(r"^Select Gender$")).nth(3)).to_be_visible()
        self.page.locator("div").filter(has_text=re.compile(r"^Select Gender$")).nth(3).click()
        self.page.get_by_role("option", name="Female").click()

        expect(self.page.get_by_placeholder("Enter NID Number")).to_be_visible()
        self.page.get_by_placeholder("Enter NID Number").click()
        self.page.get_by_placeholder("Enter NID Number").fill("7898985437")

        expect(self.page.locator("div").filter(has_text=re.compile(r"^Select District$")).nth(2)).to_be_visible()
        self.page.locator("div").filter(has_text=re.compile(r"^Select District$")).nth(2).click()
        self.page.locator("#react-select-3-input").fill("D")
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

    def selectDeliveryDetails(self):
        expect(self.page.get_by_text("Delivery Method")).to_be_visible()
        expect(self.page.locator("label").filter(has_text=re.compile(r"^Home Delivery"))).to_be_visible()

        self.page.locator("label").filter(has_text=re.compile(r"^Home Delivery")).click()

        self.page.get_by_placeholder("Select Date").click()
        self.page.get_by_label("Choose Tuesday, October 15th,").click()

        self.page.get_by_placeholder("Time").click()
        self.page.get_by_role("option", name="11:00").click()

    def sendOTP(self):
        self.page.get_by_role("button", name="Continue").click()
        expect(self.page.get_by_text("Insert OTP")).to_be_visible()