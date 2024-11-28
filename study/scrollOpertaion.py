import time
from os import times_result

import dates
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/aksha/chromedriver-win64/chromedriver.exe"


service= Service(chrome_driver_path)


driver=webdriver.Chrome(service=service)

driver.maximize_window()

driver.implicitly_wait(10)


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

time.sleep(10)


#Scroll down
#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return window.pageYoffset;")
#print("Number of pixel scroll:",value)

#Scroll down page till last
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYoffset;")
print("Number of Pixel Moved Down:",value)
time.sleep(5)

#Scroll up to Startig of the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYoffset;")
print("Number of Pixel Moved up:",value)


time.sleep(5)
driver.quit()