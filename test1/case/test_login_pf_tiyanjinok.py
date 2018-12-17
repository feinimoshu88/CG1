#-*- coding:utf-8 -*-
import unittest
import time
import sys

from test1.common.ftiyanjinpage import PfTiyanjin
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

class Test_FfTiyanjin (unittest.TestCase):
    excel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page=PfTiyanjin()

                # Step3: 输入用户名
                login_page.set_username ("88812345678")
                # # Step4: 输入密码
                login_page.set_password ("a12345")
                # # Step5: 单击登录按钮
                login_page.click_login ()
                time.sleep(1)
                login_page.click_tiyanjingl()
                login_page.click_tiyanjinff()
                time.sleep (1)
                login_page.set_tel(int(d['login'])) #赠送体验金的用户
                login_page.click_sousuo()
                login_page.click_choose()
                login_page.click_fftyj()
                time.sleep(1)
                login_page.click_ruleType()
                login_page.click_touzi()
                login_page.set_money("10000")
                login_page.click_ok()

                login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

