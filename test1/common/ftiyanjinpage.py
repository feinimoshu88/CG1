from selenium.webdriver.common.by import By
from test1.common.basepage import BasePage


class PfTiyanjin (BasePage):
    login = (By.ID, "login")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")
    tiyanjingl = (By.XPATH, ".//*[@id='side-menu']/li[8]/a/span[1]")
    tiyanjinff = (By.XPATH, ".//*[@id='side-menu']/li[8]/ul[1]/li/a/span")

    tel=(By.NAME,"login")
    sousuo=(By.ID,"searchForm-searchBtn")
    choose=(By.XPATH,".//*[@id='mDataTable']/tbody/tr/td[1]/input") #复选框，选择用xpath定位才有效
    fftyj=(By.LINK_TEXT,"发放体验金")
    ruleType=(By.ID,"ruleType")
    touzi=(By.XPATH,".//*[@id='ruleType']/option[6]")
    money=(By.NAME,"money")

    ok=(By.ID,"textOkBtn")


    def set_username(self, login):  # 输入用户名
        name = self.driver.find_element (*PfTiyanjin.login)
        name.send_keys(login)
    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*PfTiyanjin.password)
        pwd.send_keys(password)
    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*PfTiyanjin.login_btn)
        loginbtn.click ()
    def click_tiyanjingl(self):  # 点击体验金管理
        tiyanjinglbtn = self.driver.find_element (*PfTiyanjin.tiyanjingl)
        tiyanjinglbtn.click ()
    def click_tiyanjinff(self):  # 点击体验金发放
        tiyanjinffbtn = self.driver.find_element (*PfTiyanjin.tiyanjinff)
        tiyanjinffbtn.click ()
    def set_tel(self, tel):  # 输入用户
        teltxt = self.driver.find_element (*PfTiyanjin.tel)
        teltxt.send_keys (tel)
    def click_sousuo(self):  # 点击搜索
        sousuobtn = self.driver.find_element (*PfTiyanjin.sousuo)
        sousuobtn.click ()
    def click_choose(self):  # 选择用户
        choosebtn = self.driver.find_element (*PfTiyanjin.choose)
        choosebtn.click ()
    def click_fftyj(self):  # 发放体验金
        ffbtn = self.driver.find_element (*PfTiyanjin.fftyj)
        ffbtn.click ()
    def click_ruleType(self):  # 事件类型
        ruleTypebtn = self.driver.find_element (*PfTiyanjin.ruleType)
        ruleTypebtn.click ()
    def click_touzi(self):  # 点击投资
        touzibtn = self.driver.find_element (*PfTiyanjin.touzi)
        touzibtn.click ()
    def set_money(self,money):
        moneytxt=self.driver.find_element(*PfTiyanjin.money)
        moneytxt.send_keys(money)
    def click_ok(self):  # 确认
        okbtn = self.driver.find_element (*PfTiyanjin.ok)
        okbtn.click ()

