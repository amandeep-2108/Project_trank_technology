import pytest
from  pages.blogpage import Blogpage

@pytest.mark.smoke()
def test_blog_click(page):
 blog= Blogpage(page)
 blog.blog_click()