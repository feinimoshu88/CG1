#-*- coding:utf-8 -*-
import unittest
import time
import sys

from test1.common.blackwhiteuserpage import BlackWhitepage
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

class Test_Zsjiaxiquan (unittest.TestCase):
    excel = DATA_PATH + '/register.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page=BlackWhitepage()

                # Step3: 输入用户名
                login_page.set_username ("18812345678")
                # # Step4: 输入密码
                login_page.set_password ("a12345")
                # # Step5: 单击登录按钮
                login_page.click_login ()
                time.sleep(1)
                login_page.click_BlackWhitegl()
                login_page.click_yhgnmd()
                time.sleep (1)
                login_page.click_tianjia()
                time.sleep(1)
                login_page.set_tel(int(d['title']))
                login_page.click_gntype()  #点击功能类型
                login_page.click_choosetype()  #点击选择功能类型
                login_page.click_mingdantype()
                login_page.click_black()
                login_page.click_save()
                time.sleep(1)
                login_page.click_alertOkBtn()
                login_page.driver.close()


if __name__ == '__main__':
    unittest.main ()

