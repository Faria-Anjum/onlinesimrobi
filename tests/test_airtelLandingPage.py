from models.productionda import HomePage
import pytest

def test_launch(page):
    home = HomePage(page)
    home.navigate()
    home.navigate_to_airtel()
    home.launchairtel()

def test_validate(page):
    home = HomePage(page)
    home.validateairtel()