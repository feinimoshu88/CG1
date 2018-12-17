#-*- coding:utf-8 -*-
import unittest
import time
import sys

from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

class Test_Newyyy (unittest.TestCase):
    excel = DATA_PATH + '/yueyueying.xlsx'
    #excel = DATA_PATH + '/xinshoubiao.xlsx'
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
                login_page.click_yyyay()  #月月赢按月

                login_page.click_yyydq()  #月月赢到期
                # login_page.click_xinshoubiao ()  # 新手标
                login_page.click_loanuse()
                login_page.click_loanuseli()
                login_page.set_title(d['title'])
                login_page.set_bidcode(d['title'])
                login_page.set_totalAmount("10000") #标的金额
                login_page.set_termValue("6") #投资几个月
                login_page.set_interestRate("10")#年化收益率
                login_page.set_raiseRate("0")
                login_page.set_shouxufei("0")
                login_page.click_choose()
                time.sleep(2)
                login_page.set_loanuser("13010000017")
                login_page.click_search()
                login_page.click_searchok()
                time.sleep(1)
                login_page.click_type()
                # 正常标、爆款标、推荐标
                login_page.click_zcbiao() #正常
                # login_page.click_bkbiao()  #爆款
                # login_page.click_tuijianbiao() #推荐
                login_page.click_save()
                time.sleep(1)
                login_page.click_ok()
                time.sleep (1)
                login_page.driver.quit()
                #返回上架
                # login_page.click_ckzjkb ()
                # time.sleep (1)
                # login_page.set_mingcheng(d['title'])
                # login_page.click_sousuo()
                # time.sleep(1)
                # login_page.click_shangjia()
                # time.sleep(1)
                # login_page.click_shangjiaok()
                # login_page.driver.close()

if __name__ == '__main__':
    unittest.main ()

