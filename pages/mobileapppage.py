class mobile:
    def __init__(self,page):
        self.page = page
        self.technologies_cat = page.locator('(//a[text()="Technologies"])[1]')
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

    def mobile_submenuclick(self):
        for i in self.mobile_app_list:
            self.technologies_cat.hover()
            self.mobile_app.hover()
            i.click()
            self.page.wait_for_timeout(1000)
            self.page.go_back()

        