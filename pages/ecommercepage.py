class ecommerce:
    def __init__(self,page):
        self.page = page
        self.technologies_cat = page.locator('(//a[text()="Technologies"])[1]')
        self.ecomm_devel = page.locator('//strong[text()="eCommerce Development"]')
        self.magneto = page.locator('//a[text()="Magento Development"]')
        self.opencart = page.locator('(//a[text()="Opencart Development"])[1]')
        self.codeigniter = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.wordPress = page.locator('(//a[text()="WordPress Development"])[1]')
        self.BigCommerce = page.locator('(//a[text()="Big Commerce"])[1]')
        self.Shopify = page.locator('(//a[text()="Shopify Development"])[1]')
        self.Cs_Cart = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.Node_JS  = page.locator('(//a[text()="Node JS Development"])[1]')
        self.nopcommerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Woo_Commerce  = page.locator('(//a[text()="Woo Commerce"])[1]')
        self.Laravel  = page.locator('(//a[text()="Laravel Development"])[1]')
        self.Prestashop  = page.locator('(//a[text()="Prestashop Development"])[1]')
        self.Drupal  = page.locator('(//a[text()="Drupal Development"])[1]')
        self.Wix  = page.locator('(//a[text()="Wix Development"])[1]')
        self.Joomla  = page.locator('(//a[text()="Joomla Development"])[1]')
        self.React_JS  = page.locator('(//a[text()="React JS Development"])[1]')
        self.Express_JS  = page.locator('(//a[text()="Express JS Development"])[1]')

        self.Ecomm_develop_list = [self.magneto,self.opencart,self.codeigniter,self.wordPress,self.BigCommerce,self.Shopify,self.Cs_Cart,self.Node_JS,self.nopcommerce,self.Woo_Commerce,self.Laravel,
                            self.Prestashop,self.Drupal,self.Wix,self.Joomla,self.React_JS,self.Express_JS]
        
    def ecommerce_submenuclick(self):
        for i in self.Ecomm_develop_list:
            self.technologies_cat.hover()
            self.ecomm_devel.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()
