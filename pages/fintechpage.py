class fintech:
    def __init__(self,page):
        self.page = page
        self.vertical_cat = page.locator('(//a[text()="Verticals"])[1]')
        self.fintech_cat = page.locator('//strong[text()="Fintech"]')
        self.pos = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.fintech_list = [self.pos,self.crypto]
    
    def fintechpage_submenuclick(self):
        for i in self.fintech_list:
            self.vertical_cat.hover()
            self.fintech_cat.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()


    