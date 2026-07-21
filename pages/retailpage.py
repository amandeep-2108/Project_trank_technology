class retailpage:
    def __init__(self,page):
        self.page = page
        self.vertical_cat = page.locator('(//a[text()="Verticals"])[1]')
        self.retail_cat = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.ecomm_web = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecomm_app = page.locator('//a[text()="eCommerce App Development"]')

        self.retail_list = [self.ecomm_app,self.ecomm_web]

    def retail_submenuclick(self):
        for i in self.retail_list:
            self.vertical_cat.hover()
            self.retail_cat.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    