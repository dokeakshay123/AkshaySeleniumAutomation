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

#Maximize the Window
driver.maximize_window()

#Implicit wait-
driver.implicitly_wait(10)



driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Login

username=driver.find_element(By.XPATH,"//input[@placeholder='Username']")
username.click()
username.send_keys("Admin")

password=driver.find_element(By.XPATH,"//input[@placeholder='Password']")
password.click()
password.send_keys("admin123")

submitbtn=driver.find_element(By.XPATH,"//button[@type='submit']")
submitbtn.click()

# Admin--> user management --> users
admin=driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']")


#usermanagement=driver.find_element(By.XPATH,"//span[@class='oxd-topbar-body-nav-tab-item'][1]")

#usermanagement.click()
#time.sleep(5)

#user=driver.find_element(By.XPATH,"//ul[@role='menu']//li")

#user.click()


# Mouser Hover

act=ActionChains(driver)
#act.move_to_element(admin).move_to_element(usermanagement).move_to_element(user).click().perform()
act.move_to_element(admin).click().perform()



time.sleep(10)

driver.quit()


