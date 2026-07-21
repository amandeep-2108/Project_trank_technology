import pytest

from pages.customapppage import custom

@pytest.mark.trading
def test_customclick(page):
    cust = custom(page)
    cust.custom_submenuclick()


from pages.fintechpage import fintech

@pytest.mark.trading
def test_fintechclick(page):
    fin = fintech(page)
    fin.fintechpage_submenuclick()

from pages.healthcare import healthcare

@pytest.mark.trading
def test_healthcareclick(page):
    health = healthcare(page)
    health.healthcare_submenuclick()

from pages.retailpage import retailpage

@pytest.mark.smoke
def test_retailclick(page):
    retail = retailpage(page)
    retail.retail_submenuclick()

from pages.verticalpage import verticalpage

@pytest.mark.smoke
def test_tradingclick(page):
    trading = verticalpage(page)
    trading.trading_submenuclick()

