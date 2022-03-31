
# 作用：框架的主入口函数

# coding=utf-8

import time
from common.reportOut import report_out
import os
from common.logOut import log_out
#from common.sendMail import send_main
import logging


def acquire_report_address(reports_address):
    # 测试报告文件夹中的所有文件加入到列表
    test_reports_list = os.listdir(reports_address)
    # 按照升序排序生成新的列表
    new_test_reports_list = sorted(test_reports_list)
    # 获取最新的测试报告
    the_last_report = new_test_reports_list[-1]
    # 最新的测试报告地址
    the_last_report_address = os.path.join(reports_address, the_last_report)
    return the_last_report_address

def run_case():
    print("======开始执行！！！======")
    curpath = os.path.dirname(os.path.realpath(__file__))
    report_dir = os.path.join(curpath, "report/")        # 测试报告存放目录
    log_dir = os.path.join(curpath, "log/")
    test_dir = os.path.join(curpath, "case/")        # 测试用例读取目录
    name_project = "MeiDuo"
    log_out(log_dir, name_project)
    report_out(test_dir, report_dir, name_project)
    time.sleep(5)
    #send_main(acquire_report_address(report_dir), mail_to=['1915672407@qq.com'])  # mail_to为要发送给谁，可以写对应的邮箱，用逗号隔开即可
    print("======执行结束！！！======")

if __name__ == '__main__':
    run_case()
