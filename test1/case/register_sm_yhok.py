import unittest
from telnetlib import EC
import db
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
from utils.config import DATA_PATH, Config
from utils.file_reader import ExcelReader
jkurl = Config ().get ('JKURL')

class Test_smyh(unittest.TestCase):
    tel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        tels = ExcelReader (self.tel).data
        for d in tels:
            with self.subTest (data=d):
                regtel=int(d['login'])
                print(regtel)
                driver=webdriver.Chrome()
                driver.get(jkurl+'/hk-financial-services/register/register.html')
                driver.find_element_by_id ("nickName").send_keys ("hkjf")
                driver.find_element_by_id ("loginTmp").send_keys (regtel)
                # 手动输入问题
                time.sleep (8)
                # input('请输入?计算结果！')

                # driver.find_element_by_id("verify_code")sendSmsBtn
                driver.find_element_by_id ("smsCodeBtn").click ()
                time.sleep (0.5)
                driver.find_element_by_xpath (".//*[@id='dialog']/div/div/div[1]/button").click ()
                time.sleep (3)
                con = db.Db ()
                connection = con.connection
                cursor = con.cursor

                # cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
                #SELECT * from sys_tel_message where tel='15912345678'
                cursor.execute ("SELECT msg from sms_tel_msg WHERE tel=%s order by id desc limit 1",(regtel,))

                # 提交SQL
                connection.commit ()
                t = cursor.fetchall ()
                yzm = t[0]['msg']
                print(yzm)
                cursor.execute ("SELECT real_name from reg_user_detail WHERE real_name=%s", (d['name'],))
                # SELECT * FROM personinfo WHERE LOGIN_NAME='牟泓霏'
                # UPDATE personinfo set login_name='',login_card='' where login_name='牟泓霏'
                connection.commit()
                t1=cursor.fetchall()
                print(t1)
                print()
                l = len (t1)
                print (l)

               # 输入密码
                driver.find_element_by_id ("passwdTmp").send_keys ("a12345")
                # 推荐码
                driver.find_element_by_id ("commendNo").send_keys ("69321686")
                # 定位焦点方法
                elem = driver.find_element_by_id ("smsCode")
                action_a0 = ActionChains (driver)
                action_a0.move_to_element (elem).click ().send_keys (yzm).send_keys (Keys.RETURN).perform ()
                driver.find_element_by_id ("submitBtn").submit ()
                time.sleep (0.5)
                #判断身份证，姓名是否已经被使用
                if l == 0:
                    print ('hello null')
                    driver.find_element_by_id ("realName").send_keys (d['name'])  # 姓名
                    driver.find_element_by_id ("idCard").send_keys (d['idcard'])  # 身份证
                    driver.find_element_by_id ("email").send_keys ("123@126.com")  # 邮箱
                    driver.find_element_by_id ("submitBtn").click ()
                else:
                    print ('not null')

                    cursor.execute("SELECT reg_user_id from reg_user_detail  where real_name=%s", (d['name'],))
                    connection.commit ()
                    t2 = cursor.fetchall ()
                    id=t2[0]['reg_user_id']
                    print (id)
                    # cursor.execute ("SELECT identify from reg_user where id=%s", (id,))
                    # connection.commit ()
                    cursor.execute ("update reg_user set identify=0 where id=%s", (id,))  # 清理实名状态
                    connection.commit ()
                    cursor.execute ("UPDATE reg_user_detail set real_name='',id_card='' where real_name=%s",
                                    (d['name'],))  # 清理实名
                    connection.commit ()
                    # t1 = cursor.fetchall ()
                    # print (t1)
                    driver.find_element_by_id("realName").send_keys(d['name'])   #姓名
                    driver.find_element_by_id("idCard").send_keys(d['idcard'])    #身份证
                    driver.find_element_by_id("email").send_keys("123@126.com")    #邮箱
                    driver.find_element_by_id("submitBtn").click()
                time.sleep(2)
                # driver.find_element_by_link_text("跳过该环节>>").click()
                driver.close()
if __name__ == "__main__":
    unittest.main ()




