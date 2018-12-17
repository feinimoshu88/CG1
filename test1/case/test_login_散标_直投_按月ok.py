#-*- coding:utf-8 -*-
import unittest
import time
import sys

from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

class Test_Newsanbiaomonth (unittest.TestCase):
    excel = DATA_PATH + '/sanbiao_month.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page=LoginPage()

                # Step3: 输入用户名
                login_page.set_username ("88812345678")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                # Step5: 单击登录按钮
                login_page.click_login ()
                time.sleep(1)
                # login_page.driver.close()
                login_page.click_jkbgl()
                login_page.click_ckzjkb()
                time.sleep (1)
                login_page.click_new()
                time.sleep (1)
                login_page.click_bidProduct()
                # 选择产品
                login_page.click_sanbiao()
                login_page.click_loanuse()
                login_page.click_loanuseli()
                login_page.set_title(d['title'])
                login_page.set_bidcode(d['title'])
                login_page.set_totalAmount("10000")
                login_page.set_termValue("6")
                login_page.set_interestRate("10")
                login_page.set_raiseRate("1")
                login_page.set_shouxufei("1")
                login_page.set_serviceRate("1")
                login_page.click_tqhb()#提前还本
                login_page.click_ayjx()#按月计息
                login_page.set_returnCapDays("0")
                login_page.click_choose()
                time.sleep(2)
                #13010000040
                login_page.set_loanuser("13010000017")
                login_page.click_search()
                login_page.click_searchok()
                time.sleep(1)
                login_page.click_type()
                # 正常标、爆款标、推荐标
                login_page.click_zcbiao()
                #匹配or直投
                login_page.click_zhitou() #直投类型
                # login_page.click_pipei()#匹配类型
                login_page.click_save()
                time.sleep(1)
                login_page.click_ok()
                # time.sleep (1)
                # login_page.click_ckzjkb ()  #返回上架
                # time.sleep (1)
                # login_page.set_mingcheng(d['title'])
                # login_page.click_sousuo()
                # time.sleep(1)
                # login_page.click_shangjia()
                # time.sleep(1)
                # login_page.click_shangjiaok()
                login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

