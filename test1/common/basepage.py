import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config

hturl = Config().get ('HTURL')
class BasePage (object):
    def __init__(self):
        self.driver = selenium.webdriver.Chrome()
        # # fp = selenium.webdriver.FirefoxProfile (r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hwtosi65.default")
        # # self.driver =selenium.webdriver.Firefox (fp)  # 启动带插件的firefox
        # self.driver=selenium.webdriver.Firefox()  #启动不带插件的firefox
        # self.base_url = "http://192.168.1.249:8484/hk-management-services/index.html"  #测试环境
        # 预发布环境
        # self.base_url="http://39.105.87.46:8501/hk-management-services/login.html?_v=20180525targetUrlAfterLogin=http://39.105.87.46:8501/hk-management-services/index.html"
        self.base_url = hturl
        self.driver.get(self.base_url)
