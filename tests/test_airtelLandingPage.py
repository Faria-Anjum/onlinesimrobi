from models.productionda import HomePage
import pytest

def test_launch(page):
    '''AT webpage can be launched'''
    home = HomePage(page)
    home.navigate()
    home.navigate_to_airtel()
    home.launchairtel()

def test_validate(page):
    '''AT webpage loads successfully'''
    home = HomePage(page)
    home.validateairtel()