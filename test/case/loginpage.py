from selenium.webdriver.common.by import By

from test.common.basepage import BasePage


class LoginPage (BasePage):
    login = (By.ID, "login")
    password = (By.ID, "password")
    login_btn = (By.ID, "submit")

    def set_username(self, login):  # 输入用户名
        name = self.driver.find_element (*LoginPage.login)
        name.send_keys(login)

    def set_password(self, password):  # 输入密码
        pwd = self.driver.find_element (*LoginPage.password)
        pwd.send_keys(password)

    def click_login(self):  # 单击登录
        loginbtn = self.driver.find_element (*LoginPage.login_btn)
        loginbtn.click ()


