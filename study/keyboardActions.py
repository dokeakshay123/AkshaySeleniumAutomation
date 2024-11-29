

import time

import dates
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
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
#driver.implicitly_wait(2)

# open the url
driver.get("https://text-compare.com/")

txtBox1=driver.find_element(By.ID,"inputText1")
txtBox2=driver.find_element(By.ID,"inputText2")

txtBox1.send_keys("Welcome Akshay")

act=ActionChains(driver)

# Select ALl Approach1
#act.key_down(keys.CONTROL)
#act.send_keys("a")
#act.key_up(Keys.CONTROL)


#act.perform()

# Select All Approach2
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()


#Coppy Selected
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press Tab
act.send_keys(Keys.TAB).perform()

# Paste the selected text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()






time.sleep(10)
driver.quit()