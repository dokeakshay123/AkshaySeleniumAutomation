import time

import dates
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.switch_to.frame("iframeResult")

filed1=driver.find_element(By.XPATH,"//input[@id='field1']")
filed1.clear()
filed1.send_keys("Akshay")

time.sleep(5)

btn=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")

act=ActionChains(driver)

act.double_click(btn).perform() # doble click action

time.sleep(5)

driver.quit()

