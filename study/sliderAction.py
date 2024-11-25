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



driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

minRange=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")

maxRange=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")

print("Location of the Slider Before Moving")
print(minRange.location) #{'x': 59, 'y': 288}
print(maxRange.location) # {'x': 612, 'y': 288}

act = ActionChains(driver)

act.drag_and_drop_by_offset(minRange,100,0).perform()
act.drag_and_drop_by_offset(maxRange,-100,0).perform()

print("Location of the Slider After Moving")
print(minRange.location) #{'x': 159, 'y': 288}
print(maxRange.location) # {'x': 513, 'y': 288}



time.sleep(10)

driver.quit()