#coding：utf-8
from selenium import webdriver
import time
mobileEmulation={'deviceName':'Apple iphonee 6'}
options=webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation',mobileEmulation)
driver=webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)
driver.get('https://www.hongkunjinfu.com/hkjftest/mobile/index.do?method=getIndexPage')
time.sleep(3)
