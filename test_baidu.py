import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://www.baidu.com"
print(os.path.abspath(__file__))
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
print(base_path)
driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
print(driver_path)

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "jkresult")]/h3/a')
#
driver = webdriver.chrome(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium 灰蓝')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
time.sleep(3)
driver.quit()
