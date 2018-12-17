import unittest

# from test.case.test_baidu6 import TestBaiDu
# from test.case.test_pclogin import TestLogin
#
# from test.case.test_xjtuijianbiao import TestNewtjb
# from test.case.test_pp_y1_sn import TestPPy1sn
# from test1.case.test_login import Test_Login
from test1.case.register_sm_yhok import Test_smyh
from test1.case.test_login_new_sbay_dayok import Test_Newsanbiaoday
from test1.case.test_login_散标_直投_按月ok import Test_Newsanbiaomonth
from test1.case.test_login_newbkbok import Test_Newbkb
from test1.case.test_login_newtiyanbiaook import Test_Newtiyanbiao
from test1.case.test_login_newtuijianbiaook import Test_Newtuijianbiao
from test1.case.test_login_newxinshoubiaook import Test_Newxinshoubiao
from test1.case.test_login_newyyy6_pchyqtz_shfkok import Test_Newyyy_pchyq_tz_shfk

from test1.case.test_login_newyyyok import Test_Newyyy
from test1.case.test_login_newyyyok import Test_Newyyy
from test1.case.test_login_newjjyok import Test_Newjjy
# from test1.case.test_pcinvest_sh_fkok import TestPCinvest_sh_fk
from test1.case.test_login_pf2_lq_redpackageok import Test_Pf_pclqredpackage

from test1.case.test_login_pf_redpackageok import Test_Pfredpackage
from test1.case.test_login_pf_tiyanjinok import Test_FfTiyanjin
from test1.case.test_login_tjwhite_nameok import Test_Tjwhitename
from test1.case.test_login_zs_jiaxiquanok import Test_Zsjiaxiquan


from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH

if __name__=='__main__':
    suite=unittest.TestSuite()
    # suite.addTest(Test_Login("test_Login")) #登录
    # 直接用addTest方法添加单个TestCase
    # suite.addTest (TestBaiDu ("test_search"))
    # suite.addTest(TestLogin("login"))
    # suite.addTest(TestNewbkb("test_newbkb"))
    # suite.addTest(TestNewtjb("test_newtjb"))
    suite.addTest(Test_smyh("test_Login"))  #注册并实名
    suite.addTest(Test_Tjwhitename("test_Login")) #添加 投资白名单
    # suite.addTest(Test_Pfredpackage("test_Login")) #派发红包
    suite.addTest (Test_Pf_pclqredpackage ("test_Login"))  # 派发并且领取红包
    # suite.addTest()
    suite.addTest (Test_Zsjiaxiquan ("test_Login"))  # 赠送加息券
    # suite.addTest (Test_Newyyy ("test_Login"))  #新建月月盈
    # suite.addTest(Test_Newyyy22("test_Login")) #新建-投资-放款
    # suite.addTest(Test_Newxinshoubiao(("test_Login")))  #新建新手标
    #suite.addTest(Test_Newbkb("test_Login"))  #新建爆款标
    # suite.addTest(Test_Newtuijianbiao("test_Login")) #新建推荐标
    # suite.addTest(Test_Newtiyanbiao("test_Login"))   #新建体验标
    # suite.addTest(Test_Newsanbiaomonth("test_Login")) #新建散标 按月
    # suite.addTest(Test_Newsanbiaoday("test_Login")) #新建散标 按日
    # suite.addTest(Test_Newsanbiao("test_Login"))
    # suite.addTest(Test_FfTiyanjin("test_Login"))  #派发体验金
    # suite.addTest(Test_Newyyy_pchyq_tz_shfk("test_Login")) #好友券投资

    # suite.addTest(TestNewjjy("test_newjjy"))
    # suite.addTest(TestNewniannianying("test_newniannianying"))
    # suite.addTest(TestNewxsb("test_newxsb"))
    # suite.addTest(TestNewsanbiao("test_newsanbiao"))   #新建散标
    # suite.addTest(TestNewsanbiaoday("test_newsanbiaoday"))
    # suite.addTest(TestNewsanbiaomonth("test_newsanbiaomonth"))
    # suite.addTest(TestNewtyb("test_newtyb"))
    # suite.addTest(TestNewyyyycx("test_newtyyy_ycx"))
    # suite.addTest(TestNewjjyycx("test_newjjy_ycx"))
    # suite.addTest(TestNewnnyycx("test_newtnny_ycx"))
    # suite.addTest(TestTouziyyy1("test_touziyyy"))
    # suite.addTest(TestTouzijjy("test_touzijjy"))
    # suite.addTest(TestTouzinny("test_touzinny"))
    # suite.addTest(TestPPy1s1("test_ppy1s1"))
    # suite.addTest(TestPPy2s1("test_ppy2s1"))
    # suite.addTest(TestPPy1sn("test_ppy1sn"))


    # runner = unittest.TextTestRunner (verbosity=2)
    # runner.run (suite)

    if __name__ == '__main__':
        report = REPORT_PATH + '\\report.html'
        print (report)
        with open (report, 'wb') as f:
            runner = HTMLTestRunner (f, verbosity=2, title='hkjf测试报告', description='修改html报告')
            runner.run (suite)
            # e = Email (title='hkjf测试报告',
            #            message='这是今天的测试报告，请查收！',
            #            receiver='hongfeimou@hongkunjinfu.com',
            #            # server='smtp.qq.com:465',
            #            server='smtp.mxhichina.com:465',
            #            sender='hongfeimou@hongkunjinfu.com',
            #            password='.hongfei123',
            #            path=report
            #            )
            # e.send ()

