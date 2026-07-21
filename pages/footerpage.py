class Footerpage:
    def __init__(self,page):
        self.page=page
        #locator
        self.website_dev=self.page.locator('//a[text()="Web Development"]')
        self.cms_website_dev=self.page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommerce_dev=self.page.locator('//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"]').last
        self.custome_web_portal_dev=self.page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.footer_web_developement_links = [self.cms_website_dev,self.ecommerce_dev,self.custome_web_portal_dev]
        #follow us  on home page 
        self.facebook =self.page.locator('//img[@alt="Facebook"]')
        self.ln = self.page.locator('//img[@alt="LinkedIn"]')
        self.insta = self.page.locator('//img[contains(@src,"Insta")]')
        self.pin  = self.page.locator('//img[contains(@src,"pinterest")]')
        self.twiter = self.page.locator('//img[contains(@src,"twitter")]')
        self.ytube = self.page.locator('//img[contains(@src,"youtube")]')
        self.quora = self.page.locator('//img[contains(@src,"quora")]')
        self.social_list = [self.facebook,self.ln,self.insta, self.pin, self.twiter, self.ytube, self.quora]   
    
    def footer_web_development_links(self):

         self.website_dev=self.page.locator('//a[text()="Web Development"]')
         self.cms_website_dev=self.page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
         self.ecommerce_dev=self.page.locator('//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"]').last
         self.custome_web_portal_dev=self.page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
         self.footer_web_developement_links = [self.cms_website_dev,self.ecommerce_dev,self.custome_web_portal_dev]
    
         for k in self.footer_web_developement_links:
            k.scroll_into_view_if_needed(timeout=10000)
            k.wait_for(state="visible", timeout=10000) 
            if k == self.ecommerce_dev:
              k.click()
              self.page.go_back()
              self.page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
              self.website_dev = self.page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]').first
              with self.page.expect_popup() as popup_info:
                self.website_dev.click()
                new_tab = popup_info.value
                new_tab.wait_for_load_state()
                print(new_tab.title())
                new_tab.close()
                self.page.bring_to_front()
                self.page.wait_for_load_state('networkidle')
                
              continue
            else:
             k.click()
             self.page.wait_for_timeout(2000)
             self.page.go_back()
     
    #  #
    def social_media(self):
        for i in self.social_list:
       #try
            i.scroll_into_view_if_needed(timeout=10000)
            i.wait_for(state="visible",timeout=10000)
            with self.page.expect_popup() as social_popup:
             i.click()
            self.page.wait_for_timeout(2000)
            social_tab = social_popup.value
            social_tab.wait_for_load_state()
            print(f"✅ Social tab: {social_tab.title()}")
            social_tab.close()
            self.page.bring_to_front()
            self.page.wait_for_timeout(1500)

    
       # page.go_back()
    
#technolgy