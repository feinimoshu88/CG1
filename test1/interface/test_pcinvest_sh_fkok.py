import unittest

import pymysql
import xlrd

from test1.common import db
from utils.config import DATA_PATH
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode
import requests
import json

class TestPCinvest_sh_fk(unittest.TestCase):
    # con = db.Db ()
    # connection = con.connection
    # cursor = con.cursor
    # cursor.execute ("SELECT id from bid_info where name='m重构月月8203'")
    # # 提交SQL
    # connection.commit ()
    # t = cursor.fetchall ()
    # # a=t['tel']
    #
    # a = t[0]['id']
    con = db.Db ()
    connection = con.connection
    fname = DATA_PATH + '/sanbiao_month.xlsx'
    bk = xlrd.open_workbook (fname)
    try:
        sh = bk.sheet_by_name ("Sheet1")
    except:
        print
        "no sheet in %s named Sheet1" % fname

    # 获取第一行第一列数据
    cell_value = sh.cell_value (1, 0)
    print ("表格", cell_value)
    # 通过cursor创建游标
    cursor = con.cursor
    cursor.execute ("SELECT * from bid_info where name=%s", (cell_value,))
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    bidname = t[0]['name']
    print (bidname)
    cursor = con.cursor
    cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    # a=t['tel']
    a = t[0]['id']
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
        r=requests.post('http://192.168.1.249:8984/hk-financial-services/indexController/fasterLogin.do',data=content,headers=headers)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print("登录")
        c=r.cookies


    # def test_invest(self):   --投标 141  170
        content1={'bidId':TestPCinvest_sh_fk.a,'money':'10000','investRedPacketId':'','investRaiseInterestId':''}

        r1=requests.post('http://192.168.1.249:8984/hk-financial-services/bidInfoController/invest.do',data=content1,cookies=c)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)
        print("投资")

    # 后台登录
    def test_loginht(self):
        conten2 = {'randomCode': '123', 'rememberMe': '0', 'login': '88812345678',
                   'passwd': 'H/SOSDPHotw0L2qVobGWQkipJ7HWEkabs5Q63qU8PW8NvPy5HYNwMZuu2bG03VxixQczvSQRaWlEDror33LOflH7DJUPRiwD/1iYB1w1qsBN0z/1KwargVhtGw/SMDUd9yTotjfG4NbiGH9yiiba8t1hHVVVCCJbv6PvEn1bBYs='}

        r2 = requests.post ('http://192.168.1.249:8984/hk-management-services/managementLoginController/login',
                           data=conten2)  # 发送请求

        print (r2.text)  # 获取响应报文
        print (r2.status_code)
        print ("123")
        c2 = r2.cookies

        # def test_invest(self):   --投标 141  170
        content3 = {'id': TestPCinvest_sh_fk.a, 'reason': '满标审核通过', 'state': '4'}
                            #http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid
        r3 = requests.post ('http://192.168.1.249:8984/hk-management-services/bidInfoController/auditBid',
                            data=content3,
                            cookies=c2)  # 发送请求

        # return r.json
        print (r3.text)  # 获取响应报文
        print (r3.status_code)
        print ("审核")

        # http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=302
        # http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid
        a1 = 'http://192.168.1.249:8984/hk-management-services/loanController/makeLoans?bidInfoId='
        a2 = str (TestPCinvest_sh_fk.a)
        add = a1 + a2
        r4 = requests.post (add, cookies=c2)
        # return r.json
        print (r4.text)  # 获取响应报文
        print (r4.status_code)
        print ("放款")


if __name__ == "__main__":
    unittest.main ()
