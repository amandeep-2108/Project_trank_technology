class custom:
    def __init__(self,page):
        self.page = page
        self.vertical_cat = page.locator('(//a[text()="Verticals"])[1]')
        self.custom_cat = page.locator('//strong[text()="Custom App"]')
        self.desktop = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.elearning = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.real_estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.crm_usa = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        self.custom_list = [self.desktop,self.crm,self.hrm,self.erp,self.travel,self.elearning,self.dating,self.real_estate,self.crm_usa]
        
    def custom_submenuclick(self):
        for i in self.custom_list:
            self.vertical_cat.hover()
            self.custom_cat.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()