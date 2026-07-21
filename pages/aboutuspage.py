class Aboutuspage:
    def __init__(self,page):
     self.page=page
        #about us
        
    def click_about_us(self):
   
      self.page.locator('(//a[text()="About us"])[1]').click()
      self.page.wait_for_timeout(2000)

      self.page.go_back()
      self.page.wait_for_timeout(2000)
