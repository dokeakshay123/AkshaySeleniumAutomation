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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")


act = ActionChains(driver)

act.context_click(button).perform() # Right click Action

time.sleep(10)

driver.quit()



