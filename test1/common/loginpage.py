from selenium.webdriver.common.by import By
from test1.common.basepage import BasePage

class LoginPage (BasePage):
    login = (By.ID, "login")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")
    jkbgl = (By.XPATH, ".//*[@id='side-menu']/li[2]/a/span[1]")
    ckzjkb = (By.XPATH, ".//*[@id='side-menu']/li[2]/ul[1]/li/a/span")
    new = (By.LINK_TEXT,"添加")
    bidProduct= (By.NAME,"bidProductId")

    yyyay=(By.XPATH,".//*[@id='bidForm']/div/div/div[1]/select/option[2]")  # 月月盈-按月付息ok
    jjyay = (By.XPATH, ".//*[@id='bidForm']/div/div/div[1]/select/option[3]") # 季季按月付息
    nnyay = (By.XPATH,".//*[@id='bidForm']/div/div/div[1]/select/option[4]")    # 年年按月付息
    yyydq = (By.XPATH, ".//*[@id='bidForm']/div/div/div[1]/select/option[5]") # 月月盈-到期一次还本付息
    jjydq = (By.XPATH, ".//*[@id='bidForm']/div/div/div[1]/select/option[6]")    # 季季-到期一次还本付息
    nnydq = (By.XPATH, ".//*[@id='bidForm']/div/div/div[1]/select/option[7]")    # 年年-到期一次还本付息
    tyb = (By.XPATH, ".//*[@id='bidForm']/div/div/div[1]/select/option[9]")   # 体验标
    sanbiao = (By.XPATH, ".//*[@id='bidForm']/div/div/div[1]/select/option[8]") #常规借款产品ok
    xinshoubiao=(By.XPATH,".//*[@id='bidForm']/div/div/div[1]/select/option[10]")  #新手标
    haiwaiproduct=(By.XPATH,".//*[@id='bidForm']/div/div/div[1]/select/option[20]") #海外产品
    huoqiproduct=(By.XPATH,".//*[@id='bidForm']/div/div/div[1]/select/option[13]") #活期产品

    loanuse=(By.NAME,"loanUse")
    loanuseli=(By.XPATH,".//*[@id='bidForm']/div/div/div[2]/select/option[2]")
    title=(By.NAME,"title")
    bidcode = (By.NAME, "bidCode")

    totalAmount=(By.NAME,"totalAmount")
    termValue=(By.NAME,"termValue")
    interestRate = (By.NAME, "interestRate")
    raiseRate = (By.NAME, "raiseRate")
    commissionRate = (By.NAME, "commissionRate")
    serviceRate = (By.NAME, "serviceRate")
    # 逾期罚款
    advanceRepayState=(By.NAME,"advanceRepayState")  #提前还本
    anyuejixi=(By.XPATH,".//*[@id='repayCapArea']/span/div[1]/input[2]")#按月
    #driver.find_element_by_id ("returnCapDays").send_keys ("0")
    returnCapDays=(By.ID,"returnCapDays")
    # 选择借款人
    choose=(By.LINK_TEXT,"请选择")
    loanuser=(By.NAME,"login")
    search=(By.ID,"searchForm-searchBtn")
    chooseok=(By.LINK_TEXT,"选择")
    type=(By.NAME,"type")
    zcbiao=(By.XPATH,".//*[@id='bidForm']/div/div/div[29]/select/option[2]")   # 正常标  爆款标 推荐标
    bkbiao=(By.XPATH,".//*[@id='bidForm']/div/div/div[29]/select/option[3]")
    tuijianbiao=(By.XPATH,".//*[@id='bidForm']/div/div/div[29]/select/option[4]")
    zhitou = (By.XPATH, ".//*[@id='matchTypeSpan']/div/input[1]")  # 直投
    pipei=(By.XPATH,".//*[@id='matchTypeSpan']/div/input[2]")  #匹配
    save=(By.XPATH,".//*[@id='bidForm']/div/div/div[30]/button[1]")#保存标的按钮
    ok=(By.ID,"alertOkBtn")
    # 返回上架
    mingcheng=(By.NAME,"title")
    sousuo=(By.ID,"searchForm-searchBtn")
    shangjia=(By.XPATH,".//*[@id='mDataTable']/tbody/tr[1]/td[14]/a[2]")
    shangjiaok=(By.ID,"confirmOkBtn")

    def set_username(self, login):  # 输入用户名
        name = self.driver.find_element (*LoginPage.login)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*LoginPage.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*LoginPage.login_btn)
        loginbtn.click ()
    def click_jkbgl(self):  # 单击借款标管理
        jkbglbtn = self.driver.find_element (*LoginPage.jkbgl)
        jkbglbtn.click ()
    def click_ckzjkb(self):  # 单击筹款中的借款标
        ckzjkbbtn = self.driver.find_element (*LoginPage.ckzjkb)
        ckzjkbbtn.click ()
    def click_new(self):  # 单击添加
        newbtn = self.driver.find_element (*LoginPage.new)
        newbtn.click ()
    def click_bidProduct(self):  # 点击借款产品
        bidproductbtn = self.driver.find_element (*LoginPage.bidProduct)
        bidproductbtn.click ()
    def click_yyyay(self):  # 选择月月赢按月付息
        yyyaybtn = self.driver.find_element (*LoginPage.yyyay)
        yyyaybtn.click ()
    def click_jjyay(self):  # 选择季季赢按月付息
        jjyaybtn = self.driver.find_element (*LoginPage.jjyay)
        jjyaybtn.click ()
    def click_nnyay(self):  # 选择年年盈赢按月付息
        nnyaybtn = self.driver.find_element (*LoginPage.nnyay)
        nnyaybtn.click ()
    def click_yyydq(self):  # 选择月月赢到期
        yyydqbtn = self.driver.find_element (*LoginPage.yyydq)
        yyydqbtn.click ()
    def click_jjydq(self):  # 选择季季赢到期
        jjydqbtn = self.driver.find_element (*LoginPage.jjydq)
        jjydqbtn.click ()
    def click_nnydq(self):  # 选择年年赢到期
        nnydqbtn = self.driver.find_element (*LoginPage.nnydq)
        nnydqbtn.click ()
    def click_tyb(self):  # 选择体验标
        tybbtn = self.driver.find_element (*LoginPage.tyb)
        tybbtn.click ()
    def click_sanbiao(self):  # 选择常规借款产品
        sanbiaobtn = self.driver.find_element (*LoginPage.sanbiao)
        sanbiaobtn.click ()
    def click_xinshoubiao(self):  #选择新手标
        xsbbtn=self.driver.find_element(*LoginPage.xinshoubiao)
        xsbbtn.click()
    def click_haiwaiproduct(self):  #选择海外产品
        haiwaibtn=self.driver.find_element(*LoginPage.haiwaiproduct)
        haiwaibtn.click()

    def click_huoqiproduct(self):  # 选择活期产品
        huoqibtn = self.driver.find_element (*LoginPage.huoqiproduct)
        huoqibtn.click ()
    def click_loanuse(self):  # 点击借款用途
        loanuse = self.driver.find_element (*LoginPage.loanuse)
        loanuse.click ()
    def click_loanuseli(self):  # 选择借款用途
        loanuseli = self.driver.find_element (*LoginPage.loanuseli)
        loanuseli.click ()
    def set_title(self, title):  # 输入标的名称
        bidtitle = self.driver.find_element (*LoginPage.title)
        bidtitle.send_keys(title)
    def set_bidcode(self, bidcode):  # 输入标的code
        bidcodee = self.driver.find_element (*LoginPage.bidcode)
        bidcodee.send_keys(bidcode)
    def set_totalAmount(self, totalAmount):  # 输入金额
        totalamount = self.driver.find_element (*LoginPage.totalAmount)
        totalamount.send_keys(totalAmount)
    def set_termValue(self, termValue):  # 输入几个月
        termvalue = self.driver.find_element (*LoginPage.termValue)
        termvalue.send_keys (termValue)
    def set_interestRate(self, interestRate):  # 输入年利率
        interestrate = self.driver.find_element (*LoginPage.interestRate)
        interestrate.send_keys (interestRate)
    def set_raiseRate(self, raiseRate):  # 输入已加息利率
        raiseate = self.driver.find_element (*LoginPage.raiseRate)
        raiseate.send_keys (raiseRate)
    def set_shouxufei(self, commissionRate):  # 输入手续费
        shouxufei = self.driver.find_element (*LoginPage.commissionRate)
        shouxufei.send_keys (commissionRate)
    def set_serviceRate(self, serviceRate):  # 输入服务费
        servicerate = self.driver.find_element (*LoginPage.serviceRate)
        servicerate.send_keys (serviceRate)
    def click_tqhb(self): #提前还本
        tihbbtn=self.driver.find_element(*LoginPage.advanceRepayState)
        tihbbtn.click()
    def click_ayjx(self): #按月计息
        anyuejixi=self.driver.find_element(*LoginPage.anyuejixi)
        anyuejixi.click()
    def set_returnCapDays(self,returnCapDays): #按月计息
        anyuejixi1=self.driver.find_element(*LoginPage.returnCapDays)
        anyuejixi1.send_keys(returnCapDays)
    def click_choose(self):  # 请选择借款人
        choosebtn = self.driver.find_element (*LoginPage.choose)
        choosebtn.click ()
    def set_loanuser(self, loanuser):  # 输入借款人
        loanuserr = self.driver.find_element (*LoginPage.loanuser)
        loanuserr.send_keys(loanuser)
    def click_search(self):  # 搜索借款人
        searchbtn = self.driver.find_element (*LoginPage.search)
        searchbtn.click ()
    def click_searchok(self):  # 确认选择借款人
        searchokbtn = self.driver.find_element (*LoginPage.chooseok)
        searchokbtn.click ()
    def click_type(self):  # 点击标的类型
        bidtype = self.driver.find_element (*LoginPage.type)
        bidtype.click ()
    def click_zcbiao(self):  # 正常标
        zcbiaobtn = self.driver.find_element (*LoginPage.zcbiao)
        zcbiaobtn.click ()
    def click_bkbiao(self):  # 爆款标
        bkbiaobtn = self.driver.find_element (*LoginPage.bkbiao)
        bkbiaobtn.click ()
    def click_tuijianbiao(self):  # 推荐标
        tuijianbiaobtn = self.driver.find_element (*LoginPage.tuijianbiao)
        tuijianbiaobtn.click ()
    def click_save(self):  # 保存
        savebtn = self.driver.find_element (*LoginPage.save)
        savebtn.click ()
    def click_zhitou(self):  #匹配
        zhitoubtn = self.driver.find_element (*LoginPage.zhitou)
        zhitoubtn.click()
    def click_pipei(self):  #匹配
        pipeibtn = self.driver.find_element (*LoginPage.pipei)
        pipeibtn.click()
    def click_ok(self):  # 弹出框点击确认
        okbtn = self.driver.find_element (*LoginPage.ok)
        okbtn.click ()
    def set_mingcheng(self, mingcheng):  # 输入标的名称
        mingchengtxt = self.driver.find_element (*LoginPage.mingcheng)
        mingchengtxt.send_keys(mingcheng)
    def click_sousuo(self):  # 点击搜索
        sousuobtn = self.driver.find_element (*LoginPage.sousuo)
        sousuobtn.click ()
    def click_shangjia(self):  # 点击上架
        shangjiabtn = self.driver.find_element (*LoginPage.shangjia)
        shangjiabtn.click ()
    def click_shangjiaok(self):  # 点击上架
        shangjiaokbtn = self.driver.find_element (*LoginPage.shangjiaok)
        shangjiaokbtn.click ()