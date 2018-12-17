import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage (object):
    def __init__(self):
        self.driver = selenium.webdriver.Chrome ()
        self.base_url = "http://192.168.1.249:8484/hk-management-services/login.html?_v=20180525targetUrlAfterLogin=http://192.168.1.249:8484/hk-management-services/index.html#/creditorProperty?bidInfoId=467"
        self.driver.get(self.base_url)