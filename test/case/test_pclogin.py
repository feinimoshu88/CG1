import unittest
from selenium import webdriver
import time

class TestLogin(unittest.TestCase):
    def login(self):
        driver=webdriver.Chrome()
        driver.get('http://192.168.1.249:9901/hkjf/')
        time.sleep(3)
        driver.find_element_by_id('login').send_keys('13301307172')

    # driver.find_element_by_xpath(".//*[@id='txt2']").send_keys('2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc')
    # time.sleep(1)
    # driver.find_element_by_xpath(".//*[@id='logindiv']/div/div[2]").submit()
    # driver.get('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
    # time.sleep(1)
    # driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[1]/div/a/button").click()
    # time.sleep(2)
    # driver.find_element_by_xpath(".//*[@id='selone']/li[3]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath(".//*[@id='yxxm0']/a").click()
    # time.sleep(2)
#
# driver.find_element_by_id("amount").send_keys("100")
# driver.find_element_by_xpath(".//*[@id='clientInvestForm']/div[4]/a").click()
# time.sleep(3)
# #sreach_window=driver.current_window_handle
# #driver.find_element_by_xpath(".//*[@id='PDF9hFVQpC']/div[1]/div[3]/input[1]").click()
# driver.find_element_by_class_name("dialogBtn").click()
# #input class="dialogBtn" type="button" value="确定"
if __name__ == '__main__':
    unittest.main()


