# coding=utf-8
import sys
#sys.path.append("/data/projects/notebook/autoTest/jcj/")
from framework.HTMLTestRunner import HTMLTestRunner
import os
import unittest
import time


# 设置报告文件保存路径
report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'report')  
# 获取系统当前时间  
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


if __name__ == "__main__":

    # 设置报告名称格式
    HtmlFile = os.path.join(report_path, "testReport.html")
    with open(HtmlFile,'wb') as fp:

        suite_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jenkin_zhuce")
        suite = unittest.TestLoader().discover(suite_path)

        #runner = unittest.TextTestRunner()
        # 初始化一个HTMLTestRunner实例对象，用来生成报告
        runner = HTMLTestRunner(stream=fp, title="项目测试报告", description="用例测试情况")

        # 开始执行测试套件
        runner.run(suite)
