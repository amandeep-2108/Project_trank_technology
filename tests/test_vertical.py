import pytest
from pages.verticalpage import veriticalpage


@pytest.mark.smoke
def test_vertical_click(page):
    vertical1 = veriticalpage(page)
    vertical1.trading_submenu_clicking()
    
@pytest.mark.smoke
def test_retail_click(page):
    retail1 = veriticalpage(page)
    retail1.retail_submenu_clicking()
    
@pytest.mark.smoke
def test_heath_click(page):
    health1 = veriticalpage(page)
    health1.healt_submenu_clicking()
    

@pytest.mark.smoke
def test_fintech_click(page):
    fintech = veriticalpage(page)
    fintech.fintech_submenu_clicking()
    
    
    
@pytest.mark.smoke
def test_custom_click(page):
    custom = veriticalpage(page)
    custom.custom_submenu_clicking()
    
    
   
          