class Contactpage:
    def __init__(self,page):
        self.page=page
        #locator
        #contact us
        self.page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]').click()
        self.page.locator('(//input[@name="name"])[2]').fill("Amandeep")
        self.page.locator('(//input[@name="email"])[2]').fill("kaurasandhu87@gmail.com")
        self.page.locator('(//input[@name="company"])[2]').fill("ABC pvt.ltd")
        self.service=page.locator('(//select[@name="service"])[2]')
        self.service.select_option("Graphic Design")
        self.page.locator('(//input[@name="phone"])[2]').fill("8544807759")
        self.page.locator('(//textarea[@name="message"])[2]').fill("testing")
        self.page.wait_for_timeout(2000)


    def contact_us_form(self, name="Amandeep", email="kaurasandhu87@gmail.com",
                          company="ABC pvt.ltd", service="Graphic Design",
                          phone="8544807759", message="testing"):
    
      self.page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]').click()
      self.page.locator('(//input[@name="name"])[2]').fill(name)
      self.page.locator('(//input[@name="email"])[2]').fill(email)
      self.page.locator('(//input[@name="company"])[2]').fill(company)

      self.service = self.page.locator('(//select[@name="service"])[2]')
      self.service.select_option(service)

      self.page.locator('(//input[@name="phone"])[2]').fill(phone)
      self.page.locator('(//textarea[@name="message"])[2]').fill(message)
      self.page.wait_for_timeout(2000)