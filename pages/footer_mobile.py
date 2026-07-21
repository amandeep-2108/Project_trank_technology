class mobileapp:
    def __init__(self,page):
        self.page = page
        self.ios_footer = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.android_footer = page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.androidapp_footer = page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.app_footer = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.hybrid_footer = page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross_footer = page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressive_footer = page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')

        self.app_development_footer = [self.ios_footer,self.android_footer,self.hybrid_footer,self.cross_footer,
                                       self.progressive_footer]

    def mobilefooter_click(self):
        for i in self.app_development_footer:
            if i == self.android_footer:
                i.click()
                self.page.go_back()
                self.page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]').click()
                self.footer_android_list = [self.androidapp_footer,self.app_footer]
                for i in self.footer_android_list:
                    with self.page.expect_popup() as popup_info:
                        self.footer = self.page.get_by_text("Web Development")
                        i.click()
                        self.new_tab = popup_info.value
                        self.new_tab.wait_for_load_state()
                        self.new_tab.close()
                        continue
            else:
                i.click()
                self.page.wait_for_timeout(1000)
                self.page.go_back()