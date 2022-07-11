'''
用例
'''
import pytest
from PageObject import *

loggers = logging.getLogger(__name__)

# 创建一个夹具
@pytest.mark.run(order=1)
@pytest.fixture(scope="session") # 定义为session 只执行一次
def driver():
    # driver = get_webdriver() # 启动浏览器
    driver = webdriver.Chrome()
    loggers.info("浏览器已启动")
    driver.get("http://appfront.huice.com")
    # 前置部分，在测试用例之前执行
    # 写登录逻辑
    yield driver # yield 生成器的写法
    # 后置部分，在测试用例之后执行
    print('关闭浏览器')
    driver.quit()

@pytest.mark.run(order=2)
def test_login(driver):
    # 1. 打开页面，实例Page
    driver.get('http://appfront.huice.com/customer/account/login')
    page = LoginPage(driver)

    # 2. 调用page方法，完成交互
    page.login("728821370@qq.com","tian123456")

    # 登录成功断言一下
    print(page.loc_asss(),'00000')
    assert page.loc_asss() == "你好, !"
    loggers.info("用户信息登录成功")


Clist = "user1,user2,email,phone,street1,value,sheng,chengshi,code" # 参数
caselist = [ # 用例
    ['tian','jc','123@qq.com','13812345678','福庆路街道55号','Antigua and Barbuda','安提瓜和巴布','',''],
    ['tian','jc','123@qq.com','13812345678','福庆路街道55号','Antigua and Barbuda','安提瓜和巴布','北京城市','01001'],
     ]

@pytest.mark.skip(driver,reason='测试用例不依次执行，需调用执行~')
@pytest.mark.parametrize(Clist,caselist)
def test_gouwu(driver,user1,user2,email,phone,street1,value,sheng,chengshi,code):
    loggers.info("测试用例开始执行")
    driver.get('http://appfront.huice.com/computer')
    page = GouwuPage(driver)
    page.gouwu()
    time.sleep(5)
    page.input_info(user1,user2,email,phone,street1,value,sheng,chengshi,code)
    page.btn()
    loggers.info("测试用例执行完毕~")

@pytest.mark.run(order=3)
@pytest.mark.parametrize(Clist,caselist)
def test_clear(driver,user1,user2,email,phone,street1,value,sheng,chengshi,code):
    driver.get('http://appfront.huice.com/customer/address')
    page = Clear_add(driver)
    # 判断有货运地址就先清除掉货运地址
    if page.loc() != 'tian':
        test_gouwu(driver,user1,user2,email,phone,street1,value,sheng,chengshi,code)
        loggers.info("填写货运地址信息---")
    else:
        page.clears()
        loggers.info("删除货运地址信息~~~")
        test_gouwu(driver,user1,user2,email,phone,street1,value,sheng,chengshi,code)
        loggers.info("填写货运地址信息---")


if __name__ == '__main__':
    pytest.main(['-vs'])
