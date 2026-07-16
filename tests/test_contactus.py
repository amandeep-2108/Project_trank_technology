import pytest
from pages.contactpage import Contactpage

@pytest.mark.smoke
def test_contact_click(page):
    cont = Contactpage(page)
    cont.contact_us_form()