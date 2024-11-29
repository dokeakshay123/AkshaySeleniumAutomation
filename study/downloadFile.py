

import time

import dates
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    chrome_driver_path = "C:/Users/aksha/chromedriver-win64/chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

driver=chrome_setup()
# Maximize window
driver.maximize_window()

#implicit wait
driver.implicitly_wait(2)

# open the url
driver.get("https://file-examples.com/index.php/sample-documents-download/")

time.sleep(5)
driver.quit()