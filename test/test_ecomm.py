import pytest
from pages.ecommercepage import ecommerce

@pytest.mark.smoke
def test_ecommclick(page):
    ecomm = ecommerce(page)
    ecomm.ecommerce_submenuclick()

from pages.mobileapppage import mobile

@pytest.mark.smoke
def test_mobileclick(page):
    mobi = mobile(page)
    mobi.mobile_submenuclick()

from pages.ABCP import ABCPpage

@pytest.mark.smoke
def test_menuclick(page):
    menu = ABCPpage(page)
    menu.menu_click()

from pages.Footer import footersection

@pytest.mark.smoke
def test_footerclick(page):
    footermenu = footersection(page)
    footermenu.footer_click()
