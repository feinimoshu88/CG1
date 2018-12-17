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
import re

class Test_ZhuanRuok (unittest.TestCase):
    jkurl=Config().get ('JKURL')
    token='a686b668-e723-4fa1-98cd-e0bd517575fa'
    # APP登录13010000084
    #http://192.168.1.249:8984/hk-api-services/userController/login
    content = {'access_token': token,
               'deviceId': '7608AB62-D6F4-46F0-B3FF-DC15318CD4B5',
               'deviceName':'iPhone 6s',
               'login':'14010000011',
               'operateSystem':'10.2',
               'passwd':'AZh/laFXskLr634uJym+oTxC7u4x0GZkn6L+CXtzALUerFj95NQIZpb7isAe1cXEDZFENepYECTB5qSR+9N6s5ZJJx5BymeQsLuoAYDBABOJrxb/Kwif/0ML9JZJkxcLfKgIuNly53QCw2ErY1KK8keqSWCcCIs+SlnpF5bVyO0='}

    r = requests.post (jkurl+'/hk-api-services/userController/login',data=content)  # 发送请求
    # print (r.text)  # 获取响应报文
    #{"realName":"","iosVersionView":0,"nickName":"鸿坤金服","isMerchant":0,"sessionId":"509F4AB16F6BD1F7768CD47028A5F4AA","staffType":0
    print (r.status_code)
    print ("登录")
    result=r.text
    session = re.findall (r'"isMerchant":0,"sessionId":"(.+?)","staffType"', result)
    print(session[0])
    ss=session[0]
    # print(resStatus[0])
    #--钱袋子转出
    content1 = {'access_token':token, 'money': '1000', 'sessionId': ss,'source': '11'}
    #http://192.168.1.249:8984/hk-api-services/qdzController/qdzTransferOut  转出
    # r1 = requests.post (jkurl+'/hk-api-services/qdzController/qdzTransferIn',data=content1, cookies=c)  # 发送请求
    r1 = requests.post (jkurl + '/hk-api-services/qdzController/qdzTransferOut', data=content1)  # 发送请求
    # return r.json
    print (r1.text)  # 获取响应报文
    print (r1.status_code)
    print ("转入")

if __name__ == '__main__':
    unittest.main ()
