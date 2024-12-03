import time

import dates
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os

# Specify the path to chromedriver
chrome_driver_path = "C:/Users/aksha/chromedriver-win64/chromedriver.exe"

# Create a Service object with the path to chromedriver
service = Service(chrome_driver_path)

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome(service=service)

# Maximize window
driver.maximize_window()

#implicit wait
driver.implicitly_wait(10)

# open the url
driver.get("https://google.com")

#driver.save_screenshot("C:\\Users\\aksha\\OneDrive\\Desktop\\homepage.png")
driver.get_screenshot_as_png()
#driver.get_screenshot_as_file()
#driver.get_screenshot_as_base64()
time.sleep(10)
driver.quit()