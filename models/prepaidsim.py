#8801886325284
#cd /d E:\VSCode\onlinesimrobi\tests

from playwright.sync_api import expect
import re

class PrepaidPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://onlinesim.robi.com.bd/", wait_until="load")
        
    def findPrepaidSim(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi")
        assert self.page.get_by_text("Get A Prepaid SIMOrder Now").is_visible()
        expect(self.page.locator(".bg-gray-100 > a").first).to_be_visible()
        self.page.locator(".bg-gray-100 > a").first.scroll_into_view_if_needed()
        self.page.locator(".bg-gray-100 > a").first.hover()
        self.page.locator(".bg-gray-100 > a").first.click()
        
    def selectPrepaidSimKnowMore(self):
        expect(self.page.get_by_role("link", name=" Know More")).to_be_visible()
        self.page.get_by_role("link", name=" Know More").click()
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/1/2227")

    def selectPrepaidSimOrderNow(self):
        expect(self.page.get_by_role("button", name="Order Now")).to_be_visible()
        self.page.get_by_role("button", name="Order Now").scroll_into_view_if_needed()
        self.page.get_by_role("button", name="Order Now").click()
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/1/2227/registration")

class RegistrationPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://onlinesim.robi.com.bd/robi/newconnection/1/2227/registration", wait_until="load")

    def findSimNumber(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/1/2227/registration")
        expect(self.page.get_by_text("Choose SIM Number")).to_be_visible()
        self.page.get_by_text("Choose SIM Number").scroll_into_view_if_needed()
        expect(self.page.get_by_placeholder("XXXXXX", exact=True)).to_be_visible()
        self.page.get_by_placeholder("XXXXXX", exact=True).click()
        self.page.get_by_placeholder("XXXXXX", exact=True).fill("329279")
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.get_by_text("is available!")).to_be_visible()
        
    def selectSimNumber(self):
        expect(self.page.get_by_text("8801886329279", exact=True)).to_be_visible()
        self.page.locator("label").filter(has_text="8801886329279").click()

    def fillUpCustomerDetails(self):
        expect(self.page).to_have_url("https://onlinesim.robi.com.bd/robi/newconnection/1/2227/registration")
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