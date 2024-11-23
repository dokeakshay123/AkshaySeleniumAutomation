import time

import dates
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
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0) #Switch to frame

#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/18/1996")

year="2022"
month="March"
date="10"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click() # Open the calender

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text

    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;

    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()



# Select date
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")  # Find all date elements
for ele in dates:
    if ele.text == date:
        ele.click()  # Click the matching date
        break

time.sleep(10)

driver.quit()