import unittest

import db
import pymysql
import xlrd

from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode
import requests
from utils.config import DATA_PATH
import json

class TestPCinvest(unittest.TestCase):
    con = db.Db ()
    connection = con.connection
    cursor = con.cursor
    cursor.execute ("SELECT id from bid_info where name='年年盈-按月091201'")
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    # a=t['tel']
    #
    a = t[0]['id']
    # excel = DATA_PATH + '/investamount.xlsx'
    # user = DATA_PATH + '/investuser1.xlsx'
    # bidd = DATA_PATH + '/investbidd.xlsx'
    # con = db.Db ()
    # connection = con.connection
    # fname = DATA_PATH + '/yueyueying.xlsx'
    # bk = xlrd.open_workbook (fname)
    # try:
    #     sh = bk.sheet_by_name ("Sheet1")
    # except:
    #     print
    #     "no sheet in %s named Sheet1" % fname
    #
    # # 获取第一行第一列数据
    # cell_value = sh.cell_value (1, 0)
    # print ("表格", cell_value)
    # # 通过cursor创建游标
    # cursor = con.cursor
    # cursor.execute ("SELECT * from bid_info where name=%s", (cell_value,))
    # # 提交SQL
    # connection.commit ()
    # t = cursor.fetchall ()
    # bidname = t[0]['name']
    # print (bidname)
    # cursor = con.cursor
    # cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
    # # 提交SQL
    # connection.commit ()
    # t = cursor.fetchall ()
    # # a=t['tel']
    # a = t[0]['id']
    def test_login(self):
        content={'login':'13010000045','passwd':'QW8EQ4lM09bcIHZM86COM0462PoQ+1QibJUzLsD0b7JuCUdAPrqTTvGmHSHYj3/4ME6OSTIBrjdBFmtDomdy0OcURcTEljx9LetZpEHz7uHaDje9iguklu/KfguL8QZrWQ8LgIyWe2Hxr+GfNyP0mIihASYFQGGSGtKi/Drcqn4='}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Accept':'application/json, text/javascript, */*; q=0.01',
                   'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                   'Accept-Encoding': 'gzip, deflate',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Referer': 'http://192.168.1.249:8584/hk-financial-services/index.html',
                   'Content-Length': '215',
                   'Cookie': 'container_flag=container_flag; JSESSIONID=4C9658B8B1E2B04BBD1A5121BDA80EB3;',
                   'submitToken': '"SUBMIT_TOKEN:1f5832f3-3e02-4e8a-b264-fa5ce0eaf011";',
                   'ticket_admin': 'lNNabgYFTOyvXgCvOP1X9YB0B7bnzslM; submitToken_admin="SUBMIT_TOKEN:1f810b88-eb9f-4a88-ade9-50f0a5d64827"; ticket=2617gSHVCRVpSoyGybrt7DZQNEoszqPY',
                   'Connection': 'keep-alive'
                   }
        r=requests.post('http://192.168.1.249:8584/hk-financial-services/indexController/fasterLogin.do',data=content,headers=headers)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print("登录")
        c=r.cookies


    # def test_invest(self):   --投标 141  170
        content1={'bidId':TestPCinvest.a,'money':'100','investRedPacketId':'','investRaiseInterestId':''}

        r1=requests.post('http://192.168.1.249:8584/hk-financial-services/bidInfoController/invest.do',data=content1,cookies=c)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print("投资")

if __name__ == "__main__":
    unittest.main ()
