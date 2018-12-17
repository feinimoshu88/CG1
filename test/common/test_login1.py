import unittest
import selenium
import time
from appium.webdriver import webdriver
from test.common.basepage import BasePage
from test.common.loginpage import LoginPage

class Test_Login (unittest.TestCase):
    def test_Login(self):
        # # Step1: 打开登录页
        # BasePage()

        # Step2: 初始化登录Page
        login_page=LoginPage()

        # Step3: 输入用户名
        login_page.set_username ("18812345678")

        # Step4: 输入密码
        login_page.set_password ("a12345")

        # Step5: 单击登录按钮
        login_page.click_login ()
        time.sleep(3)
        login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

