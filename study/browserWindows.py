import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to chromedriver
chrome_driver_path = "C:/Users/aksha/chromedriver-win64/chromedriver.exe"

# Create a Service object with the path to chromedriver
service = Service(chrome_driver_path)

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome(service=service)

#Maximize the Window
driver.maximize_window()

#Implicit wait-
driver.implicitly_wait(10)

# Example: Open a website
driver.get("https://opensource-demo.orangehrmlive.com/")

#windowid=driver.current_window_handle # this code use for single window id
#print(windowid)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

windowids=driver.window_handles # this is used for multiple window ids


#Approach 1
#parrentWindowId=windowids[0]
#childWindowId=windowids[1]
#print(parrentWindowId,childWindowId)

#driver.switch_to.window(childWindowId)
#print("title of child window:",driver.title)

#driver.switch_to.window(parrentWindowId)
#print("title of parrent window:",driver.title)

#Approach 2
#for winId in windowids:
 #   driver.switch_to.window(winId)
  #  print(driver.title)

# close parent window
#for winId in windowids:
 ##  if driver.title=="OrangeHRM":
   #     driver.close()

# close Child window
for winId in windowids:
    driver.switch_to.window(winId)
    time.sleep(2)
    print(winId,driver.title)
    if driver.title == "Human Resources Management Software | OrangeHRM":
        driver.close()


time.sleep(5)

driver.quit()

