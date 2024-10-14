from models.prepaidsim import PrepaidPage, RegistrationPage
from playwright.sync_api import Page, sync_playwright
import pytest

def test_selectPrepaidSim(page):
    prepaid = PrepaidPage(page)
    prepaid.navigate()
    prepaid.findPrepaidSim()
    prepaid.selectPrepaidSimKnowMore()
    prepaid.selectPrepaidSimOrderNow()

def test_selectSimNumber(page):
    sim = RegistrationPage(page)
    sim.findSimNumber()
    sim.selectSimNumber()

def test_fillUpCustomerDetails(page):
    sim = RegistrationPage(page)
    sim.fillUpCustomerDetails()
    #storage = context.storage_state(path='reg.json')

def test_selectDeliveryMethod(page):
    sim = RegistrationPage(page)
    sim.selectDeliveryDetails()

def test_confirmDeliveryThroughOTP(page):
    sim = RegistrationPage(page)
    sim.sendOTP()
