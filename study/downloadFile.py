

import time

import dates
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
location=os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    chrome_driver_path = "C:/Users/aksha/chromedriver-win64/chromedriver.exe"
    service = Service(chrome_driver_path)

#download files in desired location
   # preferences={"download.default_directory":location}
  #  ops=webdriver.ChromeOptions()
 #   ops.add_experimental_option("prefs",preferences)

#driver = webdriver.Chrome(service=service,options=ops)
    driver= webdriver.Chrome(service=service)
    return driver

driver=chrome_setup()
# Maximize window
driver.maximize_window()

#implicit wait
driver.implicitly_wait(10)

# open the url
#driver.get("https://file-examples.com/index.php/sample-documents-download/")

driver.get("https://filesamples.com/formats/csv")

driver.find_element(By.XPATH,"//div[@class='output']//div[1]//a[1]").click()

time.sleep(5)
driver.quit()