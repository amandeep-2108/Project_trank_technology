from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False) #to show the web page 

    # open new tab
    page =browser.new_page()
    page.goto("https://www.amazon.in/")
    page.locator('//img[@alt="VAYA Tydbyt Stainless Steel Lunch Box for Kids & Boys, 650ml, 3 Steel Containers & Lids, No Mix-Up Tiffin Box, School..."]').click()
    page.wait_for_timeout(2000)
   