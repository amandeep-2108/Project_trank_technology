import pytest
from pages.aboutuspage  import Aboutuspage


@pytest.mark.smoke
def test_aboutus_click(page):
  aboutus = Aboutuspage(page)  
  aboutus.click_about_us()


