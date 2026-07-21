class technologiespage:
   def __init__(self, page):
        self.page = page
       #technolgy
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.e_cd=page.locator('//strong[text()="eCommerce Development"]')
        self.e_cd1=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.e_cd2=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.e_cd3=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.e_cd4=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.e_cd5=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.e_cd6=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.e_cd7=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.e_cd8=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.e_cd9=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.e_cd10=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.e_cd11=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.e_cd12=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.e_cd13=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.e_cd14=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.e_cd15=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.e_cd16=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
  # #  # e_cd17=page.locator('')
        self.tech_list=[self.e_cd1,self.e_cd2,self.e_cd3,self.e_cd4,self.e_cd5,self.e_cd6,self.e_cd7,self.e_cd8,self.e_cd9,self.e_cd10,self.e_cd11,self.e_cd12,self.e_cd13,self.e_cd14,self.e_cd15,self.e_cd16]
    
   
   
   
   #Mobie development
        self.technology=page.locator('(//a[text()="Technologies"])[1]')
        self.mbd=page.locator('//strong[text()="Mobile App Development"]')  
        self.mbd1=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]') 
        self.mbd2=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]') 
        self.mbd3=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]') 
        self.mbd4=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]') 
        self.mbd5=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]') 
        self.mbd6=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]') 
        self.mbd7=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]') 
        self.mbd8=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]') 
        self.mbd_list=[self.mbd1,self.mbd2,self.mbd3,self.mbd4,self.mbd5,self.mbd6,self.mbd7,self.mbd8]
   
   def technology_submenu_clicking(self):
     for i in self.tech_list:
     #try:  
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(1000)
        self.technology.hover()
        self.e_cd.hover()
        i.click()
        self.page.wait_for_load_state("load")
        self.page.go_back()
   
   #mobile app development  
   def mobile_submenu_clicking(self):
      for i in self.mbd_list:
         self.technology.hover()
         self. mbd.hover()
         i.click()
         self.page.wait_for_timeout(2000)
         self.page.go_back()

   
