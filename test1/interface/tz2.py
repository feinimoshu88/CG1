import unittest
import selenium
from telnetlib import EC
import xlrd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import time

from selenium.webdriver.support.wait import WebDriverWait

from test1.common import db
from utils.config import DATA_PATH
from utils.file_reader import ExcelReader
import pymysql.cursors
from locale import *



class TestPPy1s1(unittest.TestCase):

    excel = DATA_PATH + '/investamount.xlsx'
    user = DATA_PATH + '/investuser1.xlsx'
    bidd = DATA_PATH + '/investbidd.xlsx'

    def test_ppy1s1(self):
        con = db.Db ()
        connection = con.connection
        fname = DATA_PATH + '/yueyueying.xlsx'
        bk = xlrd.open_workbook (fname)
        try:
            sh = bk.sheet_by_name ("Sheet1")
        except:
            print
            "no sheet in %s named Sheet1" % fname

        # 获取第一行第一列数据
        cell_value = sh.cell_value(1, 0)
        print ("表格",cell_value)
        # 通过cursor创建游标
        cursor = con.cursor
        cursor.execute ("SELECT * from bid_info where name=%s", (cell_value,))
        # 提交SQL
        connection.commit ()
        t = cursor.fetchall ()
        bidname = t[0]['name']
        print (bidname)

if __name__ == "__main__":
    unittest.main ()




