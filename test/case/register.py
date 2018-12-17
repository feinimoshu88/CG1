import unittest
from telnetlib import EC

import pymysql
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




    tel = DATA_PATH + '/tel.xlsx'

    def test_register(self):


        driver=webdriver.Chrome()
        driver.get('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
        driver.find_element_by_link_text("注册").click()
        driver.find_element_by_id("nickName").send_keys("2024")
        driver.find_element_by_id("login").send_keys("13301302026")
        time.sleep(6)
        # 手动输入问题
        # driver.find_element_by_id("verify_code")
        driver.find_element_by_id("sendSmsBtn").click()
        time.sleep(3)
        connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                                      db='p2p_product_hotcopy',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor ()
        cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
        # 提交SQL
        connection.commit ()
        t = cursor.fetchall ()
        # a=t['tel']

        yzm = t[0]['message_note']
        # [{'tel': '15912345678'}]
        print (yzm)
        driver.find_element_by_id("randCode").send_keys(yzm)
        time.sleep (1)
        # 输入密码
        txt2=driver.find_element_by_id("txt2")
        action_a = ActionChains (driver)
        action_a.move_to_element(txt2).click ().send_keys ('a12345').send_keys (Keys.RETURN).perform ()

        time.sleep(5)
        # 推荐码
        # driver.find_element_by_id("commendPhone").send_keys("01307172")
        driver.find_element_by_id("btn_sub").click()
        time.sleep(3)
        driver.find_element_by_link_text("跳过该环节>>").click()

        time.sleep(10)

if __name__ == "__main__":
    unittest.main ()




