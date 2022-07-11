'''
PO页面封装
'''
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.select import Select
import time
import logging

loggers = logging.getLogger(__name__)

class BasePage:

    # 初始化对象
    def __init__(self,driver: webdriver.Chrome):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)
        loggers.info("PO实例化成功")

    # 元素定位
    def __getattr__(self, item,):
        loggers.info(f"访问元素{item}")
        key = f"_loc_" +item
        xpath = getattr(self, key, None)
        if xpath:
            # 根据xpath进行元素定位
            return self.get_element(xpath)
        raise ArithmeticError("元素不存在")


    def get_element(self, xpath):
        '''元素定位，会自动进行等待'''
        loggers.info(f"正在定位元素{xpath}")

        # 加载到allure当中
        allure.attach( # 定位前进行截图方便排查错误
            self._driver.get_screenshot_as_png()
        )

        el = self._wait.until(
            visibility_of_element_located( # 等待元素出现
                (
                    By.XPATH,
                    xpath,
                )
            )
        )
        loggers.info(f"元素定位成功, tag_name={el.tag_name}")
        return el

    def alert_ok(self):
        alert = self._wait.until(alert_is_present()) # 等待弹窗alert出现
        alert.accept() # 点击确定
        loggers.info(f"alert弹窗处理成功")

# 登录
class LoginPage(BasePage):
    _loc_username = '//*[@id="email"]'
    _loc_password = '//*[@id="pass"]'
    _loc_btn = '/html/body/div[1]/div/div[2]/form/div[1]/div[2]/div/ul/div[2]/button/em/span'

    def login(self,username,password):
        loggers.info(f"页面交互：{locals()}") # 打包在一起记录日志当中
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.btn.click()

        loggers.info(f"页面交互成功")
        # 加载到allure当中
        allure.attach(  # 交互后进行截图，确认交互效果
            self._driver.get_screenshot_as_png()
        )

    def loc_asss(self):
        try:
            el = self._driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/p[1]/strong').text
            loggers.info(f"断言元素正常~：{el}")
            return el
        except:
            loggers.info(f"断言元素未找到：{locals()}")


# 加入购物车
class GouwuPage(BasePage):
    _loc_nav = '/html/body/div[1]/div/div[1]/div[2]/div[2]/ul[1]/li[1]/div[1]'
    _loc_nav_btn = '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[4]/div[3]/button/em/span'
    _loc_zhifu = '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div[2]/button/span/span'
    _loc_user1 = '//*[@id="billing:firstname"]'
    _loc_user2 = '//*[@id="billing:lastname"]'
    _loc_email = '//*[@id="billing:email"]'
    _loc_phone = '//*[@id="billing:telephone"]'
    _loc_street1 = '//*[@id="billing:street1"]'
    _loc_lect = '//*[@id="billing:country"]'
    _loc_sheng = '//*[@id="state"]'
    _loc_chengshi = '//*[@id="billing:city"]'
    _loc_code = '//*[@id="billing:zip"]'
    _loc_order = '//*[@id="onestepcheckout-place-order"]'

    def gouwu(self,):
        self.nav.click()
        self.nav_btn.click()
        self.zhifu.click()
        # 加载到allure当中
        allure.attach(  # 点击的截图
            self._driver.get_screenshot_as_png()
        )

    # 国家/省/城市/邮政编码
    def selects(self,value,sheng,chengshi,code):
        selectTage = self.lect
        select = Select(selectTage)
        # 根据value值选择
        select.select_by_visible_text(value)
        self.sheng.send_keys(sheng) # 省
        self.chengshi.send_keys(chengshi) # 城市
        self.code.send_keys(code) # 邮政编码

    def input_info(self,user1,user2,email,phone,street1,value,sheng,chengshi,code):
        loggers.info(f"页面输入开始")
        self.user1.clear()
        self.user1.send_keys(user1)
        self.user2.clear()
        self.user2.send_keys(user2)
        self.email.clear()
        self.email.send_keys(email)
        self.phone.send_keys(phone)
        self.street1.send_keys(street1)
        self.selects(value,sheng,chengshi,code)
        time.sleep(1)
        loggers.info("页面输入结束~")
        # 加载到allure当中
        allure.attach(  # 输入的截图
            self._driver.get_screenshot_as_png()
        )

    def btn(self):
        loggers.info(f"页面交互：{locals()}")
        self.order.click()
        loggers.info(f"页面交互成功")
        # 加载到allure当中
        allure.attach(  # btn按钮截图
            self._driver.get_screenshot_as_png()
        )

# 清楚地址信息
class Clear_add(BasePage):
    _loc_rm = '/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td[8]/a'
    _loc_val = '/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]'

    # 货运地址元素信息
    def loc(self):
        try:
            ep = self._driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]').text
            return ep
        except:
            print('没有货运地址元素信息')
            loggers.info("页面上没有货运地址信息")

    # 点击确定弹窗
    def alert(self):
        self._driver.switch_to.alert.accept()

    def clears(self):
        self.rm.click()
        self.alert()
        # 加载到allure当中
        allure.attach(  # 删除货运地址信息
            self._driver.get_screenshot_as_png()
        )







