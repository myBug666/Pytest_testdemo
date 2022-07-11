1. 项目地址：http://appfront.huice.com/
    需要在电脑本地配置相关文件   C:\Windows\System32\drivers\etc
    '''
    139.198.109.63 bbs.huice.com
    139.198.109.63 appfront.huice.com
    139.198.109.63 appadmin.huice.com
    139.198.109.63 appserver.huice.com
    139.198.109.63 apphtml5.huice.com
    139.198.109.63 appapi.huice.com
    139.198.109.63 img.huice.com
    139.198.109.63 vue.huice.com
    139.198.109.63 m.huice.com
    0.0.0.0 account.jetbrains.com
    0.0.0.0 oauth.account.jetbrains.com
    0.0.0.0 jrebel.npegeek.com
    0.0.0.0 account.jetbrains.com
    0.0.0.0 oauth.account.jetbrains.com
    0.0.0.0 jrebel.npegeek.com
    0.0.0.0 account.jetbrains.com
    0.0.0.0 oauth.account.jetbrains.com
    0.0.0.0 jrebel.npegeek.com
    192.168.233.136 huiceserver
    '''
2. 配置pytest.ini 实现日志输出和生产allure报告数据文件
    使用allure generate --clean ./report/result/ -o ./report/html/  生产HTML报告
3. PageObject.py PO页面封装
4. test_case.py 用例封装
