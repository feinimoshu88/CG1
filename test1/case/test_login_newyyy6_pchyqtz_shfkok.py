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

class Test_Newyyy_pchyq_tz_shfk (unittest.TestCase):
    excel = DATA_PATH + '/yueyueying.xlsx'
    def test_Login(self):
        datas = ExcelReader (self.excel).data
        for d in datas:
            with self.subTest (data=d):
                login_page=LoginPage()

                # Step3: 输入用户名
                login_page.set_username ("88812345678")
                # Step4: 输入密码
                login_page.set_password ("a12345")
                # Step5: 单击登录按钮
                login_page.click_login ()
                time.sleep(1)
                # login_page.driver.close()
                login_page.click_jkbgl()
                login_page.click_ckzjkb()
                time.sleep (1)
                login_page.click_new()
                time.sleep (1)
                login_page.click_bidProduct()
                # 选择产品
                login_page.click_yyyay()  #月月赢按月
                # login_page.click_yyydq()  #月月赢到期
                login_page.click_loanuse()
                login_page.click_loanuseli()
                login_page.set_title(d['title'])
                login_page.set_bidcode(d['title'])
                login_page.set_totalAmount("10000")
                login_page.set_termValue("12")
                login_page.set_interestRate("10")
                login_page.set_raiseRate("0")
                login_page.set_shouxufei("0")
                login_page.click_choose()
                time.sleep(2)
                login_page.set_loanuser("18888888888")
                login_page.click_search()
                login_page.click_searchok()
                time.sleep(1)
                login_page.click_type()
                # 正常标、爆款标、推荐标
                login_page.click_zcbiao()
                login_page.click_save()
                time.sleep(1)
                login_page.click_ok()
                time.sleep (1)
                login_page.click_ckzjkb ()
                time.sleep (1)
                login_page.set_mingcheng(d['title'])
                login_page.click_sousuo()
                time.sleep(1)
                login_page.click_shangjia()
                time.sleep(1)
                login_page.click_shangjiaok()
                login_page.driver.close()
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
                cell_value = sh.cell_value (1, 0)
                print ("表格", cell_value)
                # 通过cursor创建游标
                cursor = con.cursor
                cursor.execute ("SELECT * from bid_info where name=%s", (d['title'],))
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
                #前台用户登录
                user='15510000013'
                content = {'login': user,
                           'passwd': 'QW8EQ4lM09bcIHZM86COM0462PoQ+1QibJUzLsD0b7JuCUdAPrqTTvGmHSHYj3/4ME6OSTIBrjdBFmtDomdy0OcURcTEljx9LetZpEHz7uHaDje9iguklu/KfguL8QZrWQ8LgIyWe2Hxr+GfNyP0mIihASYFQGGSGtKi/Drcqn4='}
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                           'Accept': 'application/json, text/javascript, */*; q=0.01',
                           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
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
                r = requests.post ('http://192.168.1.249:8584/hk-financial-services/indexController/fasterLogin.do',
                                   data=content, headers=headers)  # 发送请求

                print (r.text)  # 获取响应报文
                print (r.status_code)
                print ("登录")
                c = r.cookies

                # 查询名下的可使用的投资红包
                user = '15510000013'
                cursor.execute ("SELECT id from reg_user where login=%s", (user,))  # 用户id
                # 提交SQL
                connection.commit ()
                uid = cursor.fetchall ()
                user_id = uid[0]['id']
                print (user_id)
                #'type产品类型:0-加息券，1-投资红包，2-免费提现券，3-好友券',
                cursor.execute ("SELECT id from vas_coupon_product where type='3'")  # 卡券类型产品id
                # 提交SQL
                connection.commit ()
                pid = cursor.fetchall ()
                # pro_id = pid[0]['id']
                print (pid)
                # print(pro_id)
                num = len (pid)
                # print(len(pid))
                lis = []
                for p in pid:
                    pro_id = pid[num - 1]['id']
                    num = num - 1
                    # print(pro_id)
                    # 某某的加息券，适用于月月赢的id cur.execute("select * from user where userid = '%s' and password = '%s'" %(userid,password))
                    # cursor.execute("SELECT * from vas_coupon_detail where acceptor_user_id='%s' and coupon_product_id in('%s') and state=1 and bid_product_type_range like'%2%'"
                    #            %(user_id, pro_id))
                    cursor.execute (
                        "SELECT id from vas_coupon_detail where acceptor_user_id='%s' and coupon_product_id in('%s') and state=1 and find_in_set('2', bid_product_type_range)"
                        % (user_id, pro_id))
                    # userid='15510000011'
                    # password='af8f9dffa5d420fbc249141645b962ee'
                    # cursor.execute("SELECT * from reg_user where login= '%s' and passwd = '%s'" %(userid,password))
                    connection.commit ()
                    jxqid = cursor.fetchall ()
                    if type (jxqid) is tuple:
                        pass
                    else:
                        lis.append (jxqid)
                print ("lis 是：", lis)
                n = len (lis)
                # for a in lis:
                #     a=lis[n-1][0]
                #     n=n-1
                #     print(a['id'])
                hyq_id = lis[n - 1][0]['id']
                print (hyq_id)


                # def test_invest(self):   --投标 141  170
                content1 = {'bidId': a, 'money': '10000', 'investRedPacketId':'', 'investRaiseInterestId':hyq_id}

                r1 = requests.post ('http://192.168.1.249:8584/hk-financial-services/bidInfoController/invest.do',
                                    data=content1, cookies=c)  # 发送请求

                # return r.json
                print (r1.text)  # 获取响应报文
                print (r1.status_code)
                print ("投资")

                # 后台登录


                conten2 = {'randomCode': '123', 'rememberMe': '0', 'login': '88812345678',
                           'passwd': 'H/SOSDPHotw0L2qVobGWQkipJ7HWEkabs5Q63qU8PW8NvPy5HYNwMZuu2bG03VxixQczvSQRaWlEDror33LOflH7DJUPRiwD/1iYB1w1qsBN0z/1KwargVhtGw/SMDUd9yTotjfG4NbiGH9yiiba8t1hHVVVCCJbv6PvEn1bBYs='}

                r2 = requests.post ('http://192.168.1.249:8584/hk-management-services/managementLoginController/login',
                                    data=conten2)  # 发送请求

                print (r2.text)  # 获取响应报文
                print (r2.status_code)
                print ("123")
                c2 = r2.cookies

                # def test_invest(self):   --投标 141  170
                content3 = {'id': a, 'reason': '满标审核通过', 'state': '4'}
                # http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid
                r3 = requests.post ('http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid',
                                    data=content3,
                                    cookies=c2)  # 发送请求

                # return r.json
                print (r3.text)  # 获取响应报文
                print (r3.status_code)
                print ("审核")

                # http://192.168.1.249:8501/management/loanController/makeLoans?bidInfoId=302
                # http://192.168.1.249:8584/hk-management-services/bidInfoController/auditBid
                a1 = 'http://192.168.1.249:8584/hk-management-services/loanController/makeLoans?bidInfoId='
                a2 = str (a)
                add = a1 + a2
                r4 = requests.post (add, cookies=c2)
                # return r.json
                print (r4.text)  # 获取响应报文
                print (r4.status_code)
                print ("放款")



if __name__ == '__main__':
    unittest.main ()

