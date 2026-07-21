class healthcare:
    def __init__(self,page):
        self.page = page
        self.vertical_cat = page.locator('(//a[text()="Verticals"])[1]')
        self.healthcare_cat = page.locator('//strong[text()="Healthcare"]')
        self.diet = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.trackapp = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.heathcare_list = [self.diet,self.trackapp]
    
    def healthcare_submenuclick(self):
        for i in self.heathcare_list:
            self.vertical_cat.hover()
            self.healthcare_cat.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    