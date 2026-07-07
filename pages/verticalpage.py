class veriticalpage:
    def __init__(self,page):
        self.page =page
    #locators
        self.vertical =page.locator('(//a[text()="Verticals"])[1]')
        self.trad=page.locator('(//strong[text()="Trading"])')
        self.t1=page.locator('(//a[text()="Stock Trading"])[1]')
        self.t2=page.locator('(//a[text()="Paper Trading"])[1]')
        self.t3=page.locator('(//a[text()="CFD Trading"])[1]')
        self.t4=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
    #t6=page.locator('//a[text()="Trading App Development in Massachusetts"]')[1]
        self.t5=page.locator('//a[text()="Algo Trading"]')
        self.t6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.t7=page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.trad_list =[self.t1,self.t2,self.t3,self.t4,self.t5,self.t6,self.t7]
        
         #Retail
        self.ret=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.r1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.r2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.ret_list =[self.r1,self.r2,]
        #helathcare
        self.health=page.locator('//strong[text()="Healthcare"]')
        self.h1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.h2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.health_list =[self.h1,self.h2]

        #fintech
        self.fintech=page.locator('//strong[text()="Fintech"]')
        self.f1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.f2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
    
    #custom app
        self.custom_app=page.locator('//strong[text()="Custom App"]')
        self.c1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.c2=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.c3=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.c4=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.c5=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.c6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.c7=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.c8=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.c9=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
    #f2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
     
        self.custom_list =[self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9]
      
        self.fintech_list =[self.f1,self.f2] 
        
    
    def trading_submenu_clicking(self):    
        for i in self.trad_list:
          self.vertical.hover()
          self.trad.hover()
          i.click()
          self.page.wait_for_timeout(2000)
          self.page.go_back()
          
         
    def retail_submenu_clicking(self):
        for i in self.ret_list:
         self.vertical.hover()
         self.ret.hover()
         i.click()
         self.page.wait_for_load_state("load")
         self.page.go_back()

    def healt_submenu_clicking(self): 
        for i in self.health_list:
         self.vertical.hover()
         self.health.hover()
         i.click()
         self.page.wait_for_timeout(2000)
         self.page.go_back()

    def fintech_submenu_clicking(self):
        for i in self.fintech_list:
         self.vertical.hover()
         self.fintech.hover()
         i.click()
         self.page.wait_for_timeout(2000)
         self.page.go_back()


    def custom_submenu_clicking(self):
        for i in self.custom_list:
         self.vertical.hover()
         self.custom_app.hover()
         i.click()
      #i.click(force=True)
      #page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        self.page.go_back()
    
    