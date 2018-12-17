import unittest
import selenium
from telnetlib import EC
import xlrd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver, selenium
import time

from selenium.webdriver.support.wait import WebDriverWait

from utils.config import DATA_PATH
from utils.file_reader import ExcelReader
import pymysql.cursors
from locale import *


class TestLoanRcceiptplan2(unittest.TestCase):
    excel = DATA_PATH + '/investamount.xlsx'
    user = DATA_PATH + '/investuser1.xlsx'
    bidd = DATA_PATH + '/investbidd.xlsx'
    def test_loanreceiptplan2(self):
        connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                                      db='p2p_product_hotcopy',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        fname = DATA_PATH + '/yueyueying.xlsx'
        fname2 = DATA_PATH + '/sanbiao.xlsx'
        bk = xlrd.open_workbook (fname)
        bk2 = xlrd.open_workbook (fname2)
        shxrange = range (bk.nsheets)
        shxrange2 = range (bk2.nsheets)
        try:
            sh = bk.sheet_by_name ("Sheet1")
            sh2 = bk2.sheet_by_name ("Sheet1")
        except:
            print
            "no sheet in %s named Sheet1" % fname
            "no sheet in %s named Sheet1" % fname2
        # 获取第一行第一列数据
        cell_value = sh.cell_value (1, 0)
        cell_value2 = sh.cell_value (2, 0)
        print (cell_value)
        print (cell_value2)
        # 通过cursor创建游标
        cursor = connection.cursor ()
        # sql = "SELECT code FROM bidd_info where title='%s'",(cell_value)   # 加str确认与%s匹配
        #
        # # 创建sql 语句，并执行
        # # sql = "SELECT code FROM bidd_info ORDER BY id LIMIT 1"
        # cursor.execute (sql)
        cursor.execute ("SELECT code FROM bidd_info where title=%s", (cell_value,))
        # 提交SQL
        connection.commit ()
        t = cursor.fetchall ()
        # a=t['tel']
        biddtitle = t
        biddcode = biddtitle[0]['code']
        # [{'tel': '15912345678'}]
        print (biddtitle)
        print (biddcode)
        datas = ExcelReader (self.excel).data
        tzusers = ExcelReader (self.user).data
        tzbidds = ExcelReader (self.bidd).data
        for d in datas:
            with self.subTest (data=d):
                driver=webdriver.Chrome()
                driver.get('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
                WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                for u in tzusers:
                    with self.subTest(tzuser=u):
                        # driver = webdriver.Chrome ()
                        # driver.get ('http://192.168.1.249:9901/hkjf/index.do?method=getIndexPage')
                        # WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
                        driver.find_element_by_id ('login').send_keys (int(u['user']))
                        time.sleep(1)
                        e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
                        action = ActionChains (driver)
                        action.move_to_element (e1).click ().send_keys ("2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc").perform ()

                        driver.find_element_by_xpath(".//*[@id='logindiv']/div/div[2]").submit()
                        for b in tzbidds:
                            with self.subTest (tzbidd=b):
                                # address=("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code=ed791706-92f7-4435-b6f6-aa944ed87f4c")
                                ad1 = "http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code="
                                # ad2 = b['bidd_code']
                                ad2=biddcode
                                add = ad1 + ad2
                                driver.get(add)
                                time.sleep(1)

                                # driver.find_element_by_id("amount").send_keys(int(d['amount']))

                                    # t = driver.find_element_by_xpath (
                                    #     "html/body/div[2]/div[2]/div[2]/div[2]/div[1]/span").text
                                    # # string转换为float类型
                                    # setlocale (LC_NUMERIC, 'English_US')
                                    # # 剩余可投金额
                                    # t1 = int(atof (t))  # 123456.0
                                    # # t2=float ('%.2f' % t1)
                                    # # t2='{:.2f}'.format(t1)
                                    #
                                    # print (t)
                                    # print (t1)

                                # 根据表格配置金额投资
                                driver.find_element_by_id ("amount").send_keys (int (d['amount']))
                                # 剩余可投金额--全投
                                time.sleep(1)
                                # driver.find_element_by_id ("amount").send_keys(t1)
                                driver.find_element_by_link_text ("立即投资").click ()
                                time.sleep (1)
                                driver.find_element_by_class_name ("dialogBtn").click ()
                                time.sleep(1)
                #input class="dialogBtn" type="button" value="确定"
        driver.get ("http://192.168.1.249:9901/hkjf/loginAdmin.do?method=tologin")
        driver.find_element_by_xpath (".//*[@id='login']").send_keys ("yradmin")
        driver.find_element_by_xpath (".//*[@id='password']").send_keys ("a12345")
        time.sleep (5)
        # 手动输入验证码
        # driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
        driver.find_element_by_id ("button").submit ()
        # driver.find_element_by_name('verifyCode').clear()
        # driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
        # driver.find_element_by_xpath (".//*[@id='button']").click()

        driver.find_element_by_xpath (".//*[@id='left']/div/ul/li[5]/div/span[1]").click ()
        time.sleep (1)
        driver.find_element_by_link_text ("待审核的借款标").click ()
        driver.switch_to_frame ("contentIframe")
        # driver.find_element_by_name ("title").send_keys(biddtitle)
        driver.find_element_by_name ("title").send_keys (cell_value)
        time.sleep(3)
        driver.find_element_by_link_text ("查询").click ()
        time.sleep(1)
        driver.find_element_by_link_text ("审核").click ()
        time.sleep (1)
        driver.find_element_by_id ("content").send_keys ("满标审核通过")
        driver.find_element_by_link_text ("通过").click ()
        time.sleep (2)
        driver.switch_to_default_content ()
        time.sleep (2)
        # 财务管理-放款

        driver.find_element_by_xpath (".//*[@id='left']/div/ul/li[7]/div/span[1]").click ()
        time.sleep (1)
        driver.find_element_by_link_text ("待放款的借款标").click ()
        driver.switch_to_frame ("contentIframe")
        driver.find_element_by_name ("title").send_keys (cell_value)
        driver.find_element_by_link_text ("查询").click ()
        driver.find_element_by_link_text ("放款").click ()
        time.sleep (2)
        # a = driver.find_element_by_xpath ("//html/body/div/div/div/div[2]/iframe")
        driver.find_element_by_xpath ("//html/body/div/div/div/div[3]/input[1]").click ()
        time.sleep (3)
        al1 = driver.switch_to_alert ()
        al1.accept ()
        time.sleep (2)
        # 查看回款计划
        # 通过cursor创建游标
        cursor = connection.cursor ()
        # 创建sql 语句，并执行
        # sql = "SELECT TITLE FROM bidd_info ORDER BY id LIMIT 1"
        # cursor.execute ("SELECT code FROM bidd_info where title=%s", (cell_value,))
        cursor.execute("SELECT loan_code,receipt_atm,receipt_capital_atm,RECEIPT_INTEREST_ATM,receipt_plan_time,receipt_user_name from loan_receipt_plan  where loan_code=%s",(biddcode,))

        # 提交SQL
        connection.commit ()
        t = cursor.fetchall ()
        # a=t['tel']
        # b=a[0]['TITLE']
        print (t)  # [{'tel': '15912345678'}]


if __name__ == "__main__":
    unittest.main ()
