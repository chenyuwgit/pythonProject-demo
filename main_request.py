
import time
# from tools.send_mail import send_main
import os
from conf import config
from tools.out_log import log_out
from common.reportOut import report_out


def acquire_report_address(reports_address):
    test_reports_list = os.listdir(reports_address)                                         # 测试报告文件夹中的所有文件加入到列表
    new_test_reports_list = sorted(test_reports_list)                                       # 按照升序排序生成新的列表
    the_last_report = new_test_reports_list[-2]                                             # 获取最新的测试报告
    the_last_report_address = os.path.join(reports_address, the_last_report)                # 最新的测试报告地址
    return the_last_report_address

def run_case():
    print("======开始执行！！！======")
    report_out(config.TEST_EXCEL_PATH, config.REPORT_PATH_NAME, config.PROJECT_NAME)        # 输出报告
    time.sleep(2)
    print("======执行结束！！！======")

if __name__ == '__main__':
    run_case()