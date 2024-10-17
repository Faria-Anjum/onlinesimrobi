from models.productionda import HomePage
import pytest

def test_launch(page):
    '''Robi webpage can be launched'''
    home = HomePage(page)
    home.navigate()
    home.launchrobi()

def test_validate(page):
    '''Robi webpage loads successfully'''
    home = HomePage(page)
    home.validaterobi()