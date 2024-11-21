import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

# Specify the path to chromedriver
chrome_driver_path = "C:/Users/aksha/chromedriver-win64/chromedriver.exe"

# Create a Service object with the path to chromedriver
service = Service(chrome_driver_path)

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome(service=service,options=ops)

#Maximize the Window
driver.maximize_window()

#Implicit wait-
driver.implicitly_wait(10)

# Example: Open a website
driver.get("https://whatmylocation.com/")


time.sleep(5)

driver.quit()