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
import db
from utils.config import DATA_PATH, Config
from utils.file_reader import ExcelReader
jkurl = Config ().get ('JKURL')

class Test_notuijian(unittest.TestCase):
    tel = DATA_PATH + '/register.xlsx'
    print (tel)
    print ("tel的类型是：", type (tel))

    def test_Login(self):
        datas = ExcelReader (self.tel).data
        for d in datas:
            with self.subTest (data=d):
                regtel=int(d['title'])
                driver=webdriver.Chrome()
                driver.get(jkurl+'/hk-financial-services/register/register.html')
                driver.find_element_by_id("nickName").send_keys("hkjf")
                driver.find_element_by_id("loginTmp").send_keys(regtel)
                # 手动输入问题
                time.sleep (6)

                # driver.find_element_by_id("verify_code")
                driver.find_element_by_id("smsCodeBtn").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='dialog']/div/div/div[1]/button").click()
                time.sleep(3)
                con = db.Db ()
                connection = con.connection
                cursor = con.cursor

                # cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
                cursor.execute ("SELECT msg from sms_tel_msg WHERE tel=%s order by id desc limit 1",(regtel,))
                # 提交SQL
                connection.commit ()
                t = cursor.fetchall ()
                yzm = t[0]['msg']
                print(yzm)
                # 输入密码
                driver.find_element_by_id ("passwdTmp").send_keys("a12345")
                # 推荐码
                driver.find_element_by_id("commendNo").send_keys("69321686")

                # 定位焦点方法
                elem = driver.find_element_by_id ("smsCode")
                action_a0 = ActionChains (driver)
                action_a0.move_to_element (elem).click ().send_keys (yzm).send_keys (Keys.RETURN).perform ()

                driver.find_element_by_id("submitBtn").submit()
                time.sleep(0.5)
                driver.find_element_by_link_text("跳过该环节>>").click()
                driver.close()

if __name__ == "__main__":
    unittest.main ()




