#-*- coding:utf-8 -*-
import unittest
import time
import sys

import requests
import xlrd

from test1.common import db
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

excel = DATA_PATH + '/yueyueying.xlsx'
def test_Login():
    datas = ExcelReader (excel).data
    for d in datas:
       print(d)

test_Login()