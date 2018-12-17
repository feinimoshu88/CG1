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
from utils.config import DATA_PATH, Config
from utils.file_reader import ExcelReader
jkurl = Config ().get ('JKURL')
hturl=Config().get('HTURL')

class Test_smyh(unittest.TestCase):
    tel = DATA_PATH + '/register_sm.xlsx'
    def test_Login(self):
        tels = ExcelReader (self.tel).data
        for d in tels:
            with self.subTest (data=d):
                regtel=int(d['login'])
                print(regtel)
                driver=webdriver.Chrome()
                #登录注册
                # driver.get(jkurl+'/hk-financial-services/register/register.html')
                # driver.find_element_by_id ("nickName").send_keys ("hkjf")
                # driver.find_element_by_id ("loginTmp").send_keys (regtel)
                # # 手动输入问题
                # time.sleep (8)
                # # input('请输入?计算结果！')
                #
                # # driver.find_element_by_id("verify_code")sendSmsBtn
                # driver.find_element_by_id ("smsCodeBtn").click ()
                # time.sleep (0.5)
                # driver.find_element_by_xpath (".//*[@id='dialog']/div/div/div[1]/button").click ()
                # time.sleep (3)
                # con = db.Db ()
                # connection = con.connection
                # cursor = con.cursor
                #
                # # cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
                # #SELECT * from sys_tel_message where tel='15912345678'
                # cursor.execute ("SELECT msg from sms_tel_msg WHERE tel=%s order by id desc limit 1",(regtel,))
                #
                # # 提交SQL
                # connection.commit ()
                # t = cursor.fetchall ()
                # yzm = t[0]['msg']
                # print(yzm)
                # cursor.execute ("SELECT real_name from reg_user_detail WHERE real_name=%s", (d['name'],))
                # # SELECT * FROM personinfo WHERE LOGIN_NAME='牟泓霏'
                # # UPDATE personinfo set login_name='',login_card='' where login_name='牟泓霏'
                # connection.commit()
                # t1=cursor.fetchall()
                # print(t1)
                # print()
                # l = len (t1)
                # print (l)
                #
                #
                # # 输入密码
                # driver.find_element_by_id ("passwdTmp").send_keys ("a12345")
                # # 推荐码
                # driver.find_element_by_id ("commendNo").send_keys ("69321686")
                # # 定位焦点方法
                # elem = driver.find_element_by_id ("smsCode")
                # action_a0 = ActionChains (driver)
                # action_a0.move_to_element (elem).click ().send_keys (yzm).send_keys (Keys.RETURN).perform ()
                # driver.find_element_by_id ("submitBtn").submit ()
                # time.sleep (0.5)
                # #判断身份证，姓名是否已经被使用
                # if l == 0:
                #     print ('hello null')
                #     driver.find_element_by_id ("realName").send_keys (d['name'])  # 姓名
                #     driver.find_element_by_id ("idCard").send_keys (d['idcard'])  # 身份证
                #     driver.find_element_by_id ("email").send_keys ("123@126.com")  # 邮箱
                #     driver.find_element_by_id ("submitBtn").click ()
                # else:
                #     print ('not null')
                #
                #     cursor.execute("SELECT reg_user_id from reg_user_detail  where real_name=%s", (d['name'],))
                #     connection.commit ()
                #     t2 = cursor.fetchall ()
                #     id=t2[0]['reg_user_id']
                #     print (id)
                #     # cursor.execute ("SELECT identify from reg_user where id=%s", (id,))
                #     # connection.commit ()
                #     cursor.execute ("update reg_user set identify=0 where id=%s", (id,))  # 清理实名状态
                #     connection.commit ()
                #     cursor.execute ("UPDATE reg_user_detail set real_name='',id_card='' where real_name=%s",
                #                     (d['name'],))  # 清理实名
                #     connection.commit ()
                #     # t1 = cursor.fetchall ()
                #     # print (t1)
                #     driver.find_element_by_id("realName").send_keys(d['name'])   #姓名
                #     driver.find_element_by_id("idCard").send_keys(d['idcard'])    #身份证
                #     driver.find_element_by_id("email").send_keys("123@126.com")    #邮箱
                #     driver.find_element_by_id("submitBtn").click()
                # time.sleep(2)
                # # driver.find_element_by_link_text("跳过该环节>>").click()
                # # driver.close()
                # 登录后台添加投资白名单
                driver.get(hturl)
                driver.find_element_by_id("login").send_keys("88812345678")
                driver.find_element_by_id("password").send_keys("a12345")
                driver.find_element_by_id("submit").click()
                time.sleep (1)
                #黑白名单管理
                driver.find_element_by_xpath(".//*[@id='side-menu']/li[15]/a/span[1]").click()
                driver.find_element_by_xpath(".//*[@id='side-menu']/li[15]/ul[3]/li/a/span") .click()#用户功能名单
                time.sleep (2)
                driver.find_element_by_link_text("添加").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='rosInfoForm']/div/div/div[1]/input").send_keys(int(d['login'])) #选择用户
                time.sleep (1)
                # 功能类型
                driver.find_element_by_xpath(".//*[@id='rosInfoForm']/div/div/div[2]/select/option[10]").click() #投资
                # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[5]")  # 债权转让
                # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[6]")  # 新手标投资
                # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[13]")  # 提现
                # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[10]")  # 投资ok
                # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[17]")  # 销售ok
                # 名单类型
                driver.find_element_by_xpath(".//*[@id='rosInfoForm']/div/div/div[3]/select/option[2]").click() #白名单
                # driver.find_element_by_xpath(".//*[@id='rosInfoForm']/div/div/div[3]/select/option[1]").click() #黑名单
                driver.find_element_by_xpath(".//*[@id='rosInfoForm']/div/div/div[4]/button[1]").click()  #保存
                time.sleep(1)
                driver.find_element_by_id("alertOkBtn").click()
                driver.close()

if __name__ == "__main__":
    unittest.main ()




