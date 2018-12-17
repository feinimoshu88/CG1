from selenium.webdriver.common.by import By
from test1.common.basepage import BasePage

class BlackWhitepage (BasePage):
    login = (By.ID, "login")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")
    blackwhitegl = (By.XPATH, ".//*[@id='side-menu']/li[15]/a/span[1]")
    yhgnmd = (By.XPATH, ".//*[@id='side-menu']/li[15]/ul[2]/li/a/span")
    tianjia=(By.LINK_TEXT,"添加")
    tel=(By.XPATH,".//*[@id='rosInfoForm']/div/div/div[1]/input")
    gntype=(By.XPATH,".//*[@id='rosInfoForm']/div/div/div[2]/select")
    white=(By.XPATH,".//*[@id='rosInfoForm']/div/div/div[3]/select/option[2]")
    black = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[3]/select/option[1]")
    # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[5]")  # 债权转让
    # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[6]")  # 新手标投资
    # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[13]")  # 提现
    choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[10]")  # 投资ok
    # choosetype = (By.XPATH, ".//*[@id='rosInfoForm']/div/div/div[2]/select/option[17]")  # 销售ok

    mingdantype=(By.XPATH,".//*[@id='rosInfoForm']/div/div/div[3]/select")
    save=(By.XPATH,".//*[@id='rosInfoForm']/div/div/div[4]/button[1]")  #保存
    alertOkBtn=(By.ID,"alertOkBtn")

    def set_username(self, login):  # 输入用户名
        name = self.driver.find_element (*BlackWhitepage.login)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*BlackWhitepage.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*BlackWhitepage.login_btn)
        loginbtn.click ()
    def click_BlackWhitegl(self):  # 点击黑白名单管理
        BlackWhitepagebtn = self.driver.find_element (*BlackWhitepage.blackwhitegl)
        BlackWhitepagebtn.click ()
    def click_yhgnmd(self):  # 点击用户功能名单
        yhgnmdbtn = self.driver.find_element (*BlackWhitepage.yhgnmd)
        yhgnmdbtn.click ()
    def click_tianjia(self):  # 点击添加
        tianjiabtn = self.driver.find_element (*BlackWhitepage.tianjia)
        tianjiabtn.click ()
    def set_tel(self,tel):  # 输入用户
        teltxt = self.driver.find_element (*BlackWhitepage.tel)
        teltxt.send_keys(tel)
    def click_gntype(self):  # 点击功能类型
        gntypebtn = self.driver.find_element (*BlackWhitepage.gntype)
        gntypebtn.click()
    def click_choosetype(self):  # 选择添加的功能
        choosetypebtn = self.driver.find_element (*BlackWhitepage.choosetype)
        choosetypebtn.click ()
    def click_mingdantype(self):  # 选择加黑名单  还是白名单
        mingdantypebtn = self.driver.find_element (*BlackWhitepage.mingdantype)
        mingdantypebtn.click ()
    def click_white(self):  # 点击白名单
        whitebtn = self.driver.find_element (*BlackWhitepage.white)
        whitebtn.click()
    def click_black(self):  # 点击黑名单
        blackbtn = self.driver.find_element(*BlackWhitepage.black)
        blackbtn.click()
    def click_save(self):  # 点击保存
        savebtn = self.driver.find_element (*BlackWhitepage.save)
        savebtn.click()
    def click_alertOkBtn(self):  # 点击确认
        alertOkBtnn = self.driver.find_element (*BlackWhitepage.alertOkBtn)
        alertOkBtnn.click ()
