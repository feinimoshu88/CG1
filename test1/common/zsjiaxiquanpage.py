from selenium.webdriver.common.by import By
from test1.common.basepage import BasePage


class ZsJiaxiquan (BasePage):
    login = (By.ID, "login")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")
    kqgl = (By.XPATH, ".//*[@id='side-menu']/li[20]/a/span[1]")  #卡券管理菜单
    zskq = (By.XPATH, ".//*[@id='side-menu']/li[20]/ul[2]/li/a/span")#赠送卡券
    kqtype = (By.ID, "type")

    # choosekqtype = (By.XPATH, ".//*[@id='type']/option[1]") #全部
    choosehbjxq=(By.XPATH,".//*[@id='type']/option[2]")  #加息券
    choosehb = (By.XPATH, ".//*[@id='type']/option[3]")  # 投资红包
    choosetxq = (By.XPATH, ".//*[@id='type']/option[4]")  # 提现券
    choosehyq = (By.XPATH, ".//*[@id='type']/option[5]")  # 好友券
    sousuo=(By.ID,"searchForm-searchBtn")
    all=(By.NAME,"cb-check-all")
    xzuser=(By.LINK_TEXT,"选择用户赠送")
    tel=(By.NAME,"login")
    search=(By.ID,"usersTable-searchForm-searchBtn")
    xztel=(By.XPATH,".//*[@id='usersTable']/tbody/tr/td[1]/input")   #选择输入的用户
    reason=(By.ID,"reason")
    zengsong=(By.LINK_TEXT,"赠送")
    confirmOkBtn=(By.ID,"confirmOkBtn")
    def set_username(self, login):  # 输入用户名
        name = self.driver.find_element (*ZsJiaxiquan.login)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*ZsJiaxiquan.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*ZsJiaxiquan.login_btn)
        loginbtn.click ()
    def click_kqgl(self):  # 点击卡券管理
        kqglbtn = self.driver.find_element (*ZsJiaxiquan.kqgl)
        kqglbtn.click ()
    def click_zskq(self):  # 点击赠送卡券
        zskqbtn = self.driver.find_element (*ZsJiaxiquan.zskq)
        zskqbtn.click ()
    def click_kqtype(self):  # 点击卡券产品类型
        kqtypebtn = self.driver.find_element (*ZsJiaxiquan.kqtype)
        kqtypebtn.click ()
    def click_choosejxq(self):  # 选择加息券
        choosekqtypebtn = self.driver.find_element (*ZsJiaxiquan.choosehbjxq)
        choosekqtypebtn.click ()

    def click_choosehb(self):  # 选择红包
        choosekqtypebtn = self.driver.find_element (*ZsJiaxiquan.choosehb)
        choosekqtypebtn.click ()
    def click_choosetxq(self):  # 选择提现券
        choosekqtypebtn = self.driver.find_element (*ZsJiaxiquan.choosetxq)
        choosekqtypebtn.click ()
    def click_choosehyq(self):  # 选择好友券
        choosekqtypebtn = self.driver.find_element (*ZsJiaxiquan.choosehyq)
        choosekqtypebtn.click ()
    def click_sousuo(self):  # 选择加息券、红包、提现券
        sousuobtn = self.driver.find_element (*ZsJiaxiquan.sousuo)
        sousuobtn.click ()
    def click_all(self):  # 全选
        allbtn = self.driver.find_element (*ZsJiaxiquan.all)
        allbtn.click ()
    def click_xzuser(self):  # 点击选择用户赠送
        xzuserbtn = self.driver.find_element (*ZsJiaxiquan.xzuser)
        xzuserbtn.click ()
    def set_tel(self, tel):  # 输入用户
        teltxt = self.driver.find_element (*ZsJiaxiquan.tel)
        teltxt.send_keys(tel)
    def click_search(self):  # 搜索
        searchbtn = self.driver.find_element (*ZsJiaxiquan.search)
        searchbtn.click ()
    def click_xztel(self):  # 勾选输入的用户
        xztelbtn = self.driver.find_element (*ZsJiaxiquan.xztel)
        xztelbtn.click ()
    def set_reason(self, reason):  # 输入密码
        reasontxt = self.driver.find_element (*ZsJiaxiquan.reason)
        reasontxt.send_keys(reason)
    def click_zengsong(self):  # 勾选输入的用户
        zengsongbtn = self.driver.find_element (*ZsJiaxiquan.zengsong)
        zengsongbtn.click ()
    def click_confirmOkBtn(self):  # 勾选输入的用户
        confirmOkbtn = self.driver.find_element (*ZsJiaxiquan.confirmOkBtn)
        confirmOkbtn.click ()