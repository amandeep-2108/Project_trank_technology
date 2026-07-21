class ABCPpage:
    def __init__(self,page):
        self.page = page
        self.About_us = page.locator('(//a[text()="About us"])[1]')
        self.Blog = page.locator('(//a[text()="Blog"])[1]')
        self.Contact = page.locator('(//a[text()="Contact us"])[1]')
        self.Portfolio = page.locator('//a[text()="Portfolio"]')

        self.menu_list = [self.About_us,self.Blog,self.Contact,self.Portfolio]

    def menu_click(self):
        for i in self.menu_list:
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
