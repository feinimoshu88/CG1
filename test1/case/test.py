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

con = db.Db ()
connection = con.connection
cursor=con.cursor
#查询名下的可使用的加息券
user='13010000049'
cursor.execute ("SELECT id from reg_user where login=%s", (user,))   #用户id
# 提交SQL
connection.commit ()
uid  = cursor.fetchall ()
user_id= uid[0]['id']
print(user_id)
cursor.execute ("SELECT id from vas_coupon_product where type='0'") #卡券类型产品id
# 提交SQL
connection.commit ()
pid = cursor.fetchall ()
# pro_id = pid[0]['id']
print(pid)
# print(pro_id)
num=len(pid)
# print(len(pid))
lis = []
for p in pid:
    pro_id=pid[num-1]['id']
    num=num-1
    # print(pro_id)
    #某某的加息券，适用于月月赢的id cur.execute("select * from user where userid = '%s' and password = '%s'" %(userid,password))
    # cursor.execute("SELECT * from vas_coupon_detail where acceptor_user_id='%s' and coupon_product_id in('%s') and state=1 and bid_product_type_range like'%2%'"
    #            %(user_id, pro_id))
    cursor.execute (
        "SELECT id from vas_coupon_detail where acceptor_user_id='%s' and coupon_product_id in('%s') and state=1 and find_in_set('2', bid_product_type_range)"
        % (user_id, pro_id))
    # userid='15510000011'
    # password='af8f9dffa5d420fbc249141645b962ee'
    # cursor.execute("SELECT * from reg_user where login= '%s' and passwd = '%s'" %(userid,password))
    connection.commit()
    jxqid = cursor.fetchall()
    if type(jxqid) is tuple:
        pass
    else:
        lis.append(jxqid)
print("lis 是：",lis)
n=len(lis)
# for a in lis:
#     a=lis[n-1][0]
#     n=n-1
#     print(a['id'])
jxq_id=lis[n-1][0]['id']
print(jxq_id)



