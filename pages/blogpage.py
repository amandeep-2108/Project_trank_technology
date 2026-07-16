class Blogpage:
    def __init__(self,page):
        self.page= page
# blog
    def blog_click(self):
        self.page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]').click()
        self.page.wait_for_timeout(2000)

        self.page.go_back()
        self.page.wait_for_timeout(2000)