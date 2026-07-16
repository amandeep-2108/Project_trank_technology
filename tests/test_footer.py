import pytest
from pages.footerpage import Footerpage

@pytest.mark.smoke
def test_web_development(page):
    web= Footerpage(page)
    web.footer_web_development_links()
    
    
@pytest.mark.smoke
def test_social_media(page):
    social_m=Footerpage(page)
    social_m.social_media()