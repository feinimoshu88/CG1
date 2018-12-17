#-*- coding:utf-8 -*-
import unittest
import selenium
import time
from appium.webdriver import webdriver
import sys
sys.path.append('D:\\jftest1_CG\\test1')
# sys.path.append('C:\\Users\\mhf\\PycharmProjects\\jftest1_CG72301\\test1')
from test1.common.loginpage import LoginPage

class Test_Login (unittest.TestCase):

    def test_Login(self):
        login_page=LoginPage()

        # Step3: 输入用户名
        login_page.set_username ("88812345678")
        # Step4: 输入密码
        login_page.set_password ("a12345")
        # Step5: 单击登录按钮
        login_page.click_login ()
        login_page.driver.maximize_window ()
        time.sleep(500000)
        # login_page.driver.close()
if __name__ == '__main__':
    unittest.main ()

