from selenium.webdriver.common.by import By
from test1.common.basepage import BasePage


class PfRedpackage (BasePage):
    login = (By.ID, "login")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")
    zzfu = (By.XPATH, ".//*[@id='side-menu']/li[11]/a/span[1]")
    hbgl = (By.XPATH, ".//*[@id='side-menu']/li[11]/ul/li/a/span")
    pfhb=(By.LINK_TEXT,"派发红包")
    tel=(By.NAME,"login")
    sousuo=(By.ID,"usersTable-searchForm-searchBtn")
    choose=(By.XPATH,".//*[@id='usersTable']/tbody/tr/td[1]/input") #复选框，选择用xpath定位才有效
    value=(By.ID,"packetValue")
    packetEndDate=(By.ID,"packetEndDate")
    packetSendReason=(By.ID,"packetSendReason")
    paifa=(By.LINK_TEXT,"派发")
    confirmOkBtn=(By.ID,"confirmOkBtn")
    ok=(By.ID,"alertOkBtn")
    # 财务管理
    cwgl=(By.XPATH,".//*[@id='side-menu']/li[5]/a/span[1]")
    hbsh=(By.XPATH,".//*[@id='side-menu']/li[5]/ul[6]/li/a/span")
    dhuser=(By.NAME,"acceptorTel")
    sousuo2=(By.ID,"searchForm-searchBtn")
    quanxuan=(By.NAME,"cb-check-all")
    plsh=(By.LINK_TEXT,"批量审核")
    shreason=(By.ID,"checkReasonArea")
    shok=(By.ID,"textOkBtn")


    def set_username(self, login):  # 输入用户名
        name = self.driver.find_element (*PfRedpackage.login)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*PfRedpackage.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*PfRedpackage.login_btn)
        loginbtn.click ()
    def click_zzfu(self):  # 点击增值服务
        zzfubtn = self.driver.find_element (*PfRedpackage.zzfu)
        zzfubtn.click ()
    def click_hbgl(self):  # 点击红包管理
        hbglbtn = self.driver.find_element (*PfRedpackage.hbgl)
        hbglbtn.click ()
    def click_pfhb(self):  # 点击派发红包
        pfhbbtn = self.driver.find_element (*PfRedpackage.pfhb)
        pfhbbtn.click ()
    def set_tel(self, tel):  # 输入用户
        teltxt = self.driver.find_element (*PfRedpackage.tel)
        teltxt.send_keys (tel)
    def click_sousuo(self):  # 点击搜索
        sousuobtn = self.driver.find_element (*PfRedpackage.sousuo)
        sousuobtn.click ()
    def click_choose(self):  # 选择用户
        choosebtn = self.driver.find_element (*PfRedpackage.choose)
        choosebtn.click ()
    def set_value(self, value):  # 输入金额
        valuetxt = self.driver.find_element (*PfRedpackage.value)
        valuetxt.send_keys(value)
    def set_enddate(self, packetEndDate):  # 输入过期日期
        enddatetxt = self.driver.find_element(*PfRedpackage.packetEndDate)
        enddatetxt.send_keys(packetEndDate)
    def set_packetSendReason(self, packetSendReason):  # 输入派发原因
        packetSendReasontxt = self.driver.find_element (*PfRedpackage.packetSendReason)
        packetSendReasontxt.send_keys(packetSendReason)
    def click_paifa(self):  # 点击派发
        paifabtn = self.driver.find_element (*PfRedpackage.paifa)
        paifabtn.click ()
    def click_confirmOkBtn(self):  # 确认派发
        confirmOkBtnn = self.driver.find_element (*PfRedpackage.confirmOkBtn)
        confirmOkBtnn.click ()
    def click_ok(self):  # 确认
        okbtn = self.driver.find_element (*PfRedpackage.ok)
        okbtn.click ()
    def click_cwgl(self):  # 财务管理
        cwglbtn = self.driver.find_element (*PfRedpackage.cwgl)
        cwglbtn.click ()
    def click_hbsh(self):  # 红包审核
        hbshbtn = self.driver.find_element (*PfRedpackage.hbsh)
        hbshbtn.click ()
    def set_dhuser(self, dhuser):  # 输入兑换红包用户
        dhusertxt = self.driver.find_element (*PfRedpackage.dhuser)
        dhusertxt.send_keys(dhuser)
    def click_sousuo2(self):  # 搜索红包记录
        sousuo2btn = self.driver.find_element (*PfRedpackage.sousuo2)
        sousuo2btn.click ()
    def click_quanxuan(self):  # 全选
        quanxuanbtn = self.driver.find_element (*PfRedpackage.quanxuan)
        quanxuanbtn.click ()
    def click_plsh(self):  # 批量审核
        plshbtn = self.driver.find_element (*PfRedpackage.plsh)
        plshbtn.click ()
    def set_shreason(self, shreason):  # 输入用户名
        shreasontxt = self.driver.find_element (*PfRedpackage.shreason)
        shreasontxt.send_keys(shreason)
    def click_shok(self):  # 批量审核
        shokbtn = self.driver.find_element (*PfRedpackage.shok)
        shokbtn.click ()
