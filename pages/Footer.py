class footersection:
    def __init__(self, page):
        self.page = page
        self.footer = page.get_by_text("Web Development")
        self.wait = page.wait_for_timeout(2000)
        self.cms = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommweb_footer = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.arrow = page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
        # self.web_dev_footer = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.custom_footer = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        
        self.mobile_footer = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsive_footer = page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brand_footer = page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')

        self.logo = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner = page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packaging = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.card = page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        self.webdevfooter_list = [self.cms,self.ecommweb_footer,self.custom_footer,self.mobile_footer,
                                  self.responsive_footer,self.brand_footer,self.logo,self.banner,
                                  self.packaging,self.card]
    def footer_click(self):
        for i in self.webdevfooter_list:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        
    
