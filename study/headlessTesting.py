from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    chrome_driver_path = Service("C:/Users/aksha/chromedriver-win64/chromedriver.exe")

    ops=webdriver.ChromeOptions()
    ops.headless=True


    driver = webdriver.Chrome(service=chrome_driver_path,options=ops)
    return driver

driver=headless_chrome()

driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.close()