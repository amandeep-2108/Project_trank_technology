class followlinks:
    def __init__(self,page):
        self.page = page
        self.facebook = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/facebook.png"]')
        self.linkedin = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/linkedin.png"]')
        self.instagram = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')
        self.pinterest = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/pinterest.png"]')
        self.twitter = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/twitter.png"]')
        self.youtube = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/youtube.png"]')
        self.quora = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/quora.png"]')

        self.follow_list = [self.facebook,self.linkedin,self.instagram,self.pinterest,self.twitter,
                        self.youtube,self.quora]

    def followlink_click(self):
        for i in self.follow_list:
            with self.page.expect_popup() as self.popup_info:
                i.click()
                self.new_tab1 = self.popup_info.value
                self.new_tab1.wait_for_load_state("load")
                self.new_tab1.close()
            self.page.wait_for_timeout(2000)