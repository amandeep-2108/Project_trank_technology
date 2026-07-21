import pytest

from pages.followuslink import followlinks

@pytest.mark.smoke
def test_followus_click(page):
    follow = followlinks(page)
    follow.followlink_click()