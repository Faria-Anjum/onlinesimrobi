from models.productionda import HomePage
import pytest

def test_launch(page):
    home = HomePage(page)
    home.navigate()
    home.launchrobi()

def test_validate(page):
    home = HomePage(page)
    home.validaterobi()