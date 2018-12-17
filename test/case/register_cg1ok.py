import unittest
from telnetlib import EC

import pymysql
import xlrd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH
from utils.file_reader import ExcelReader


class TestTouziyyy1(unittest.TestCase):
    tel = DATA_PATH + '/register.xlsx'

    def test_register(self):
        registers = ExcelReader (self.tel).data
        # tzusers = ExcelReader (self.user).data
        # for u in tzusers:
        #     with self.subTest (tzuser=u):

        driver=webdriver.Chrome()
        driver.get('http://192.168.1.249:8602/financial/register/register.html')
        driver.find_element_by_id("nickName").send_keys("hkjf")

        driver.find_element_by_id("loginTmp").send_keys("15510000013")
        # 手动输入问题
        time.sleep (6)

        # driver.find_element_by_id("verify_code")
        driver.find_element_by_id("smsCodeBtn").click()
        time.sleep(3)
        connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                                      db='finance_qa',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


        cursor = connection.cursor ()
        # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
        cursor.execute ("SELECT msg from sms_tel_msg WHERE tel='15510000013'order by id desc limit 1")
        # 提交SQL
        connection.commit ()
        t = cursor.fetchall ()
        # a=t['tel']

        yzm = t[0]['msg']
        # [{'tel': '15912345678'}]
        print(yzm)

        # 定位焦点方法
        elem = driver.find_element_by_id("smsCode")
        action_a0 = ActionChains (driver)

        action_a0.move_to_element (elem).click ().send_keys(yzm).send_keys (Keys.RETURN).perform ()

        # driver.find_element_by_id("smsCode").send_keys(yzm)
        # driver.find_element_by_xpath(".//*[@id='smsCode']").send_keys(yzm)


        # 输入密码
        txt2=driver.find_element_by_id("passwdTmp")
        action_a = ActionChains (driver)
        action_a.move_to_element(txt2).click ().send_keys ('a12345').send_keys (Keys.RETURN).perform ()
        driver.find_element_by_id("agreeOn").click()

        # 推荐码
        # driver.find_element_by_id("commendPhone").send_keys("01307172")
        driver.find_element_by_id("commendNo").send_keys("01307172")
        driver.find_element_by_id("submitBtn").submit()
        time.sleep(2)
        driver.find_element_by_link_text("跳过该环节>>").click()



if __name__ == "__main__":
    unittest.main ()




