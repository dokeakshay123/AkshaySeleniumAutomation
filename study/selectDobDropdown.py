import time

import dates
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//input[@id='dob']").click()
#driver.find_element(By.ID,'dob').click()

datePicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datePicker_month.select_by_visible_text("Dec") # Select Month

datePicker_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
datePicker_year.select_by_visible_text("1996") # Select Year

alldates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in alldates:
    if date.text=="25":
        date.click()
        break

time.sleep(10)

driver.quit()