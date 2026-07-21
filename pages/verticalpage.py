from datetime import datetime
import re

class verticalpage:
    def __init__(self,page):
        self.page = page
        self.vertical_cat = page.locator('(//a[text()="Verticals"])[1]')
        self.trading_cat = page.locator('//strong[text()="Trading"]')
        self.stocktrading = page.locator('(//a[text()="Stock Trading"])[1]')
        self.algotrading = page.locator('//a[text()="Algo Trading"]')
        self.papertrading = page.locator('//a[text()="Paper Trading"]')
        self.customtrading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfdtrading = page.locator('(//a[text()="CFD Trading"])[1]')
        self.webportaltrading = page.locator('(//a[text()="Web Portal Trading"])[1]')
        self.developtrading = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

        self.trading_list = [self.stocktrading,self.algotrading,self.papertrading,self.customtrading,self.cfdtrading,self.webportaltrading,self.developtrading]

    
        self.retail_cat = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.ecomm_web = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecomm_app = page.locator('//a[text()="eCommerce App Development"]')

        self.retail_list = [self.ecomm_app,self.ecomm_web]
    
        self.healthcare_cat = page.locator('//strong[text()="Healthcare"]')
        self.diet = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.trackapp = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.heathcare_list = [self.diet,self.trackapp]
    
        self.fintech_cat = page.locator('//strong[text()="Fintech"]')
        self.pos = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.fintech_list = [self.pos,self.crypto]
    
        self.custom_cat = page.locator('//strong[text()="Custom App"]')
        self.desktop = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.elearning = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.real_estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.crm_usa = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        self.custom_list = [self.desktop,self.crm,self.hrm,self.erp,self.travel,self.elearning,self.dating,self.real_estate,self.crm_usa]
        
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
        
    
        self.mobile_app = page.locator('//strong[text()="Mobile App Development"]')
        self.react_mobile = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamrian = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.iconic = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.swift = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.appoint_book = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.ai = page.locator('//strong[text()="Artificial Intelligence"]')

        self.mobile_app_list = [self.react_mobile,self.enterprise,self.xamrian,self.kotlin,self.flutter,self.iconic,self.swift,self.appoint_book,self.ai]
            
        self.About_us = page.locator('(//a[text()="About us"])[1]')
        self.Blog = page.locator('(//a[text()="Blog"])[1]')
        self.Contact = page.locator('(//a[text()="Contact us"])[1]')
        self.Portfolio = page.locator('//a[text()="Portfolio"]')

        self.menu_list = [self.About_us,self.Blog,self.Contact,self.Portfolio]

    # for i in menu_list:
    #     i.click()
    #     if i == "Contact":
    #         page.get_by_text("Want to know more? Let's connect right away!")
    #         page.wait_for_timeout(2000)
    #         page.locator('(//input[@placeholder="Your Name"])[2]').fill("Khushi")
    #         page.locator('(//input[@placeholder="Your Mail"])[2]').fill("test@gmail.com")
    #         page.locator('(//button[text()="Send OTP"])[2]').click()
    #         page.locator('(//input[@placeholder="Your Company"])[2]').fill("Uncodemy")
    #         service = page.locator('//select[@name="service"]')
    #         service.select_option("Web Development")
    #         page.locator('(//input[@placeholder="Your Phone"])[2]').fill("1234567890")
    #         page.locator('(//textarea[@placeholder="Message"])[2]').fill("this is test message")
    #         page.locator('(//div[@role="presentation"])[6]').click
    #         page.wait_for_timeout(2000)
    #     page.wait_for_timeout(1000)
    #     page.go_back()
    #Footer
        self.footer = page.get_by_text("Web Development")
        self.wait = page.wait_for_timeout(2000)
        self.cms = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.ecommweb_footer = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.arrow = page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
        # self.web_dev_footer = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.custom_footer = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        self.webdevfooter_list = [self.cms,self.ecommweb_footer,self.custom_footer]

    # for i in webdevfooter_list:
    #     if i == ecommweb_footer:
    #         i.click()
    #         page.go_back()
    #         page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
    #         web_dev_footer = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
    #         page.wait_for_timeout(5000)
    #         with page.expect_popup() as popup:
    #             web_dev_footer.click()
    #             new_tab = popup.value
    #             new_tab.wait_for_load_state()
    #             new_tab.close()
    #             continue
    #     else:
    #         i.click()
    #         page.wait_for_load_state("load")
    #         page.go_back()
    
        self.footer = page.get_by_text("Web Development")
        self.mobile_footer = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsive_footer = page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brand_footer = page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')

        self.uiuxfooterlist = [self.mobile_footer,self.responsive_footer,self.brand_footer]
    
        self.ios_footer = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.android_footer = page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.androidapp_footer = page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.app_footer = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.hybrid_footer = page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross_footer = page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressive_footer = page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')

        self.app_development_footer = [self.ios_footer,self.android_footer,self.hybrid_footer,self.cross_footer,self.progressive_footer]
    
        self.logo = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner = page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packaging = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.card = page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        self.graphic = [self.logo,self.banner,self.packaging,self.card]

    # def vertical_mousehover(self):
    #     self.vertical_cat.hover()
    
    # def trading_mousehover(self):
    #     self.trading_cat.hover()
    
    def trading_submenuclick(self):
        for i in self.trading_list:
            self.vertical_cat.hover()
            self.trading_cat.hover()
            if i.is_visible():
                i.click()
                self.page.wait_for_timeout(1000)
                self.page.go_back()
            else:
                self.page.wait_for_timeout(1000)
                self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                self.filename = f"{self.clean_title}_{self.timestamp}.png"
                self.page.screenshot(path=self.filename)
    
                self.page.go_back()
    
    