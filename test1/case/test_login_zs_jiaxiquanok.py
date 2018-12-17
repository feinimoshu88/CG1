#-*- coding:utf-8 -*-
import unittest
import time
import sys

from test1.common.zsjiaxiquanpage import ZsJiaxiquan
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

class Test_Zsjiaxiquan (unittest.TestCase):
    excel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page=ZsJiaxiquan()

                # Step3: 输入用户名
                login_page.set_username ("88812345678")
                # # Step4: 输入密码
                login_page.set_password ("a12345")
                # # Step5: 单击登录按钮
                login_page.click_login ()
                time.sleep(1)
                login_page.click_kqgl()
                login_page.click_zskq()
                time.sleep (2)
                login_page.click_kqtype()
                # login_page.click_choosejxq()#选择加息券
                login_page.click_choosehb() #红包
                # login_page.click_choosetxq()#提现券
                # login_page.click_choosehyq()  #好友券
                login_page.click_sousuo()
                login_page.click_all()
                login_page.click_xzuser()
                time.sleep(1)
                login_page.set_tel(int(d['login'])) #赠送加息券/投资红包的用户
                login_page.click_search()
                # time.sleep(1)
                login_page.click_xztel()
                login_page.set_reason("卡券赠送原因123")
                login_page.click_zengsong()
                time.sleep (1)
                login_page.click_confirmOkBtn()
                time.sleep(1)
                login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

