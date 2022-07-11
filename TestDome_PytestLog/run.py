# encoding:utf-8
import pytest
import os
import time


if __name__ == '__main__':
    pytest.main(['-v', '-s', './test_case.py'])

    # 获取时间戳
    time_stamp = time.strftime('%Y%m%d_%H-%M-%S')
    # 输出结果，生成json报告文件
    pytest.main(['-v','-s','--alluredir','./report/result'])
    os.system('allure generate --clean ./report/result/ -o ./report/html/' '测试报告_' + time_stamp)
                                      # 生成json文件目录    生成html报告存放目录
