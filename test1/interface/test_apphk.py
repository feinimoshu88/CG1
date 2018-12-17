import unittest

import pymysql

from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode
import requests

import json

class TestInvest(unittest.TestCase):
    # connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
    #                               db='finance_qa',
    #                               charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    #
    # cursor = connection.cursor()
    # # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
    # cursor.execute ("SELECT id from bid_info where name='m年年一次71303'")
    # # 提交SQL
    # connection.commit ()
    # t = cursor.fetchall ()
    # # a=t['tel']
    #
    # a= t[0]['id']

    def test_login(self):
        content = {'access_token': 'ed39725a-5f6f-4504-adb2-07f78b9adf04','login': '18301306330',
                   'passwd': 'FezfhWyda5Pe5T/cYvnTNq4sph88sotP1O02LmQBv+NhyMWLFjqgJngDJ9K+EIOJxmU1KfO2vp50yCK33WbERd7qBFn/6n1Ao/2GUHmJZeJutaEWTFRTyoZ59mh33RT7nYoe1+LI1yUSydYOITeEKPUwZ+xaUBBwOfH4MB2EQxA='}
        headers = {'Accept': '*/*',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-Hans-CN;q=1',
                   'User-Agent': 'caixiangPlus/1.0.1 (iPhone; iOS 10.0.1; Scale/2.00)',
                   'Content-Length': '364',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Connection': 'keep-alive',
                   'Host': '192.168.1.249:8484'}
        # headers=headers
        r = requests.post('http://192.168.1.249:8484/hk-api-services/userController/login', data=content)  # 发送请求

        print (r.text)  # 获取响应报文
        print (r.status_code)
        print ("登录")
        c = r.cookies
        for key, value in c.items ():
            print (key, '==', value)
        s=c.values()
        print(c.values())
        d= r.cookies['JSESSIONID']
        print('==========')
        print(d)
        # session = requests.session()
        # ss=session.get('http://192.168.1.249:9080/api/userController/login')
        # print(ss)

        # def test_invest(self):   --投标 141  170
        # content1 = {'access_token': 'ed39725a-5f6f-4504-adb2-07f78b9adf04','bidId': TestInvest.a ,'investWay': '1101', 'money': '10000',
        #             'sessionId': s, 'sign': '42952b6522bbed5e51aac4e481c588c0', 'sign_type': 'MD5', 'source': '11'}
        content1 = {'access_token': 'ed39725a-5f6f-4504-adb2-07f78b9adf04', 'repayId':166, 'sessionId':d,'source':'11'}
        # 还款接口
        r1 = requests.post('http://192.168.1.249:8484/hk-api-services/loanController/repaySample',data=content1)  # 发送请求

        # return r.json
        print (r1.text)  # 获取响应报文
        print (r1.status_code)

    # # 后台登录
    # def test_loginht(self):
    #     content = {'randomCode': '123', 'rememberMe': '0', 'login': '18812345678',
    #                'passwd': 'Xb4dT7muWJyqt0+TpHahsWrdxIe/BDKa9yxeFoD108q1yaCONHJdFgW7gr3fHmfuWZre8K8aDb4A5qtZWefu+M2QBEGZSRndZhSSOMeqGzkFsxspStSsf1Wv6P9Ppsb/MOKQYSpm2iiFdVTd4UV6CnmV+BCmPGw3URmtalNDvzs='}
    #
    #     r = requests.post ('http://192.168.1.249:8484/hk-management-services/managementLoginController/login',
    #                        data=content)  # 发送请求
    #
    #     print (r.text)  # 获取响应报文
    #     print (r.status_code)
    #     print ("123")
    #     c = r.cookies
    #
    #     # def test_invest(self):   --投标 141  170
    #     content1 = {'id': TestInvest.a, 'reason': '满标审核通过', 'state': '4'}
    #
    #     r1 = requests.post ('http://192.168.1.249:8484/hk-management-services/bidInfoController/auditBid', data=content1,
    #                         cookies=c)  # 发送请求
    #
    #     # return r.json
    #     print (r1.text)  # 获取响应报文
    #     print (r1.status_code)
    #     print ("审核")
    #
    #     # http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=302
    #     # http://192.168.1.249:8484/hk-management-services/loanController/makeLoans?bidInfoId=713
    #     a1 = 'http://192.168.1.249:8484/hk-management-services/loanController/makeLoans?bidInfoId='
    #     a2 = str (TestInvest.a)
    #     add = a1 + a2
    #     r2 = requests.post (add, cookies=c)
    #     # return r.json
    #     print (r1.text)  # 获取响应报文
    #     print (r1.status_code)
    #     print ("放款")
    #

if __name__ == "__main__":
    unittest.main ()
