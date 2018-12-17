#-*- coding:utf-8 -*-
import unittest
import time
import sys
import db
import requests
import xlrd
from test1.common.basepage import BasePage
from utils.config import DATA_PATH, REPORT_PATH, Config
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from test1.common.loginpage import LoginPage

class Test_Newyyy22 (unittest.TestCase):
    jkurl=Config().get ('JKURL')
    #需要投资的标的
    bid='mhf活期601'
    con = db.Db ()
    connection = con.connection
    # 通过cursor创建游标
    cursor = con.cursor
    # cursor.execute ("SELECT * from bid_info where name=%s", (d['title'],))
    cursor.execute ("SELECT * from bid_info where name=%s", (bid,))
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    print(t)
    bidname = t[0]['name']
    print (bidname)
    cursor = con.cursor
    cursor.execute ("SELECT id from bid_info where  name=%s", (bidname,))
    # 提交SQL
    connection.commit ()
    t = cursor.fetchall ()
    # a=t['tel']
    a = t[0]['id']
    cursor.close()
    connection.close()
    # # #登录前台
    # content = {'login': '13010000084', 'passwd': 'QW8EQ4lM09bcIHZM86COM0462PoQ+1QibJUzLsD0b7JuCUdAPrqTTvGmHSHYj3/4ME6OSTIBrjdBFmtDomdy0OcURcTEljx9LetZpEHz7uHaDje9iguklu/KfguL8QZrWQ8LgIyWe2Hxr+GfNyP0mIihASYFQGGSGtKi/Drcqn4='}
    #
    # r = requests.post (jkurl+'/hk-financial-services/indexController/fasterLogin.do',data=content)  # 发送请求
    # # r = requests.post (jkurl + '/hk-financial-services/indexController/fasterLogin.do', data=content)  # 发送请求
    # print (r.text)  # 获取响应报文
    # print (r.status_code)
    # print ("登录")
    # c = r.cookies
    # #--投标 141  170    投资金额
    # content1 = {'bidId': a, 'money': '10000', 'investRedPacketId': '','investRaiseInterestId': ''}
    # r1 = requests.post (jkurl+'/hk-financial-services/bidInfoController/invest.do',data=content1, cookies=c)  # 发送请求
    # # return r.json
    # print (r1.text)  # 获取响应报文
    # print (r1.status_code)
    # print ("投资")
    # 后台登录
    conten2 = {'randomCode': '123', 'rememberMe': '0', 'login': '88812345678', 'passwd': 'H/SOSDPHotw0L2qVobGWQkipJ7HWEkabs5Q63qU8PW8NvPy5HYNwMZuu2bG03VxixQczvSQRaWlEDror33LOflH7DJUPRiwD/1iYB1w1qsBN0z/1KwargVhtGw/SMDUd9yTotjfG4NbiGH9yiiba8t1hHVVVCCJbv6PvEn1bBYs='}
    r2 = requests.post (jkurl+'/hk-management-services/managementLoginController/login',data=conten2)  # 发送请求
    print (r2.text)  # 获取响应报文
    print (r2.status_code)
    print ("123")
    c2 = r2.cookies
    # 满标审核
    content3 = {'id': a, 'reason': '满标审核通过', 'state': '4'}
    r3 = requests.post (jkurl+'/hk-management-services/bidInfoController/auditBid',data=content3,cookies=c2)  # 发送请求
    print (r3.text)  # 获取响应报文
    print (r3.status_code)
    print ("审核")
    #放款  http://192.168.1.249:8984/hk-management-services/loanController/makeLoans?bidInfoId=442
    a1 = jkurl+'/hk-management-services/loanController/makeLoans?bidInfoId='
    a2 = str (a)
    add = a1 + a2
    r4 = requests.post (add, cookies=c2)
    # return r.json
    print (r4.text)  # 获取响应报文
    print (r4.status_code)
    print ("放款")
if __name__ == '__main__':
    unittest.main ()
