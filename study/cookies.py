import time

import dates
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
#driver.get("https://google.com")


#gmailBtn=Keys.CONTROL+Keys.RETURN
#driver.find_element(By.LINK_TEXT,"Gmail").send_keys(gmailBtn)

#New Tab - Open New tab and switch to new tab

driver.get("https://google.com")
driver.switch_to.new_window('tab')
driver.get("https://facebook.com")

# Capture cookies

storecookes=driver.get_cookies()
#print(storecookes)
print("Size of cookies:",len(storecookes))

# print details of cookies
#
# for c in storecookes:
# #print(c)
#     print(c.get('name'),":",c.get('value'))

# # Capture cookies
# storecookies = driver.get_cookies()
# print("Size of cookies:", len(storecookies), storecookies)

# Add new cookies

driver.add_cookie({"name":"Akki","value":"12345"})
storecookes=driver.get_cookies()
print("Size of afer adding new one cookies:",len(storecookes))

# Delete Specific cookies
driver.delete_cookie('Akki')
storecookes=driver.get_cookies()
print("Size of afer adding delete new one cookies:",len(storecookes))

#Delete all cookies
driver.delete_all_cookies()
storecookes=driver.get_cookies()
print("Size of afer adding delete all cookies:",len(storecookes))

driver.delete_all_cookies()


time.sleep(5)
driver.quit()