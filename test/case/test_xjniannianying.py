# coding=utf-8
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import unittest, time, re

from utils.config import DATA_PATH
from utils.config1 import Config
from utils.file_reader import ExcelReader


class TestNewyyy(unittest.TestCase):
    excel = DATA_PATH + '/niannianying.xlsx'
    URL=Config().get ('URL')
    def test_newyyy(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest(data=d):
                driver=selenium.webdriver.Chrome()
                driver.get(self.URL)
                driver.find_element_by_id("login").send_keys("18812345678")
                driver.find_element_by_id("password").send_keys("a12345")
                driver.find_element_by_id("submit").click()
                time.sleep (1)
                driver.find_element_by_xpath (".//*[@id='side-menu']/li[2]/a/span[1]").click ()
                driver.find_element_by_xpath (".//*[@id='side-menu']/li[2]/ul[1]/li/a/span").click ()
                time.sleep (1)
                driver.find_element_by_link_text("添加").click()
                time.sleep(1)
                driver.find_element_by_name("bidProductId").click()
                # 选择产品  年年盈
                driver.find_element_by_xpath(".//*[@id='bidForm']/div/div/div[1]/select/option[4]").click()
                # 年年盈到期还本付息.//*[@id='bidForm']/div/div/div[1]/select/option[7]
                # driver.find_element_by_xpath (".//*[@id='bidForm']/div/div/div[1]/select/option[7]").click ()
                driver.find_element_by_name ("loanUse").click ()
                driver.find_element_by_xpath(".//*[@id='bidForm']/div/div/div[2]/select/option[2]").click()
                driver.find_element_by_name("title").send_keys(d['title'])
                driver.find_element_by_name("bidCode").send_keys(d['title'])
                # 金额
                driver.find_element_by_name("totalAmount").send_keys("10000")
                # 几个月
                driver.find_element_by_name("termValue").send_keys("12")
                # 年利率
                driver.find_element_by_name("interestRate").send_keys("10")
                driver.find_element_by_name("raiseRate").send_keys("0")
                driver.find_element_by_name ("commissionRate").send_keys ("0")
                driver.find_element_by_name("serviceRate").send_keys("0")
                driver.find_element_by_link_text("请选择").click()
                time.sleep(1)
                # 选择借款人 14510000500  13301307172  18800000000
                driver.find_element_by_name("login").send_keys("18301306330")
                driver.find_element_by_id("searchForm-searchBtn").click()
                driver.find_element_by_link_text("选择").click()
                time.sleep (1)
                driver.find_element_by_name("type").click()
                # 正常标  爆款标 推荐标
                # driver.find_element_by_xpath (".//*[@id='bidForm']/div/div/div[27]/select/option[2]").click ()

                driver.find_element_by_xpath (".//*[@id='bidForm']/div/div/div[27]/select/option[3]").click ()
                # driver.find_element_by_xpath(".//*[@id='bidForm']/div/div/div[27]/select/option[4]").click()
                driver.find_element_by_id ("startDate").click ()
                # time.sleep(1)
                frame = driver.find_element_by_xpath ("html/body/div[4]/iframe")

                driver.switch_to_frame (frame)
                driver.find_element_by_xpath (".//*[@id='dpTodayInput']").click ()

                # time.sleep(1)
                driver.switch_to_default_content ()
                # time.sleep(1)
                driver.find_element_by_id ("endDate").click ()
                # time.sleep(1)
                driver.switch_to_frame (frame)
                #
                #
                # time.sleep(1)
                driver.find_element_by_xpath (".//*[@id='dpTitle']/div[6]/a").click ()
                driver.find_element_by_xpath (".//*[@id='dpTitle']/div[6]/a").click ()
                driver.find_element_by_xpath ("html/body/div[1]/div[3]/table/tbody/tr[4]/td[3]").click ()
                driver.find_element_by_id ("dpOkInput").click ()

                driver.switch_to_default_content ()
                time.sleep (1)
                driver.find_element_by_xpath (".//*[@id='bidForm']/div/div/div[28]/button[1]").click ()
                time.sleep (1)
                driver.find_element_by_id ("alertOkBtn").click ()
                time.sleep (1)
                # 返回上架
                # driver.find_element_by_xpath (".//*[@id='side-menu']/li[1]/ul[1]/li/a/span").click ()
                # driver.find_element_by_xpath (".//*[@id='side-menu']/li[2]/a/span[1]").click ()
                driver.find_element_by_xpath (".//*[@id='side-menu']/li[2]/ul[1]/li/a/span").click ()
                time.sleep (1)
                driver.find_element_by_name ("title").send_keys (d['title'])
                driver.find_element_by_id ("searchForm-searchBtn").click ()
                time.sleep (1)
                driver.find_element_by_xpath (".//*[@id='mDataTable']/tbody/tr[1]/td[14]/a[2]").click ()
                time.sleep (1)
                driver.find_element_by_id ("confirmOkBtn").click ()

                time.sleep (10)


if __name__ == "__main__":
    unittest.main ()

