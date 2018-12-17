#-*- coding:utf-8 -*-
import datetime
import unittest
import time
import sys

from test1.common.fredpackgepage import PfRedpackage
from utils.config import DATA_PATH, REPORT_PATH
from utils.config1 import Config
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
qturl = Config().get ('QTURL')

class Test_Pf_pclqredpackage (unittest.TestCase):
    excel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page=PfRedpackage()
                driver=login_page.driver

                # Step3: 输入用户名
                login_page.set_username ("88812345678")
                # # Step4: 输入密码
                login_page.set_password ("a12345")
                # # Step5: 单击登录按钮
                login_page.click_login ()
                time.sleep(1)
                login_page.click_zzfu()
                login_page.click_hbgl()
                time.sleep(2)
                login_page.click_pfhb()
                time.sleep(1)
                login_page.set_tel(int(d['login']))
                login_page.click_sousuo()
                login_page.click_choose()
                login_page.set_value("1000000")
                a = datetime.datetime.now ()
                b = str(a + datetime.timedelta(days=365))
                login_page.set_enddate(b)    #2018-07-28 14:52:04
                login_page.set_packetSendReason("测试")
                login_page.click_paifa()
                time.sleep(1)
                login_page.click_confirmOkBtn()
                login_page.click_ok()
                time.sleep(1)
                a=driver.find_element_by_xpath (".//*[@id='mDataTable']/tbody/tr[1]/td[2]").text  #红包编码
                print(a)
                #红包审核
                login_page.click_cwgl()
                time.sleep(1)
                login_page.click_hbsh()
                time.sleep(1)
                login_page.set_dhuser(int(d['login']))
                login_page.click_sousuo2()
                login_page.click_quanxuan()
                time.sleep(1)
                login_page.click_plsh()
                time.sleep(1)
                login_page.set_shreason("派发红包审核通过")
                login_page.click_shok()
                time.sleep(2)
                # # driver.close()
                #登录前台领取红包
                driver.get(qturl)
                print(qturl)
                WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'loginTmp')))

                # driver = webdriver.Chrome ()
                # driver.get ('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
                # WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                driver.find_element_by_id ('loginTmp').send_keys (int (d['login']))
                time.sleep (1)
                e1 = driver.find_element_by_id ("passwdTmp")
                action = ActionChains (driver)
                # action.move_to_element (e1).click ().send_keys (
                #     'QW8EQ4lM09bcIHZM86COM0462PoQ+1QibJUzLsD0b7JuCUdAPrqTTvGmHSHYj3/4ME6OSTIBrjdBFmtDomdy0OcURcTEljx9LetZpEHz7uHaDje9iguklu/KfguL8QZrWQ8LgIyWe2Hxr+GfNyP0mIihASYFQGGSGtKi/Drcqn4=').perform ()
                action.move_to_element (e1).click ().send_keys('a12345').perform ()
                driver.find_element_by_id("loginBtn").click()
                time.sleep(1)
                driver.find_element_by_id("myAccount").click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[@id='menu-one']/li[6]/div/span").click() #有债权转让菜单？
                # driver.find_element_by_xpath(".//*[@id='menu-one']/li[5]/div/span").click()  #无债权转让菜单
                driver.find_element_by_link_text("红包兑换").click()
                time.sleep(0.5)
                driver.find_element_by_id("redpageKey").send_keys(a)
                driver.find_element_by_id("exchange").click()  #兑换
                time.sleep(0.5)
                driver.close()
if __name__ == '__main__':
    unittest.main ()

