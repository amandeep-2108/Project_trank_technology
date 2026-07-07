import pytest
from pages.technologiespage import technologiespage

@pytest.mark.smoke
def test_technolgy_clicking(page):
    technology = technologiespage(page)
    technology.technology_submenu_clicking()
    
    
@pytest.mark.smoke                          # ✅ Added missing @
def test_mobile_clicking(page):
    mobile = technologiespage(page)
    mobile.mobile_submenu_clicking()