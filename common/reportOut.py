#封装测试报告脚本
import unittest
from common import HTMLTestRunner    # 引入导入的报告模板
import time

def report_out(test_dir, report_dir, name_project):
    '''
    :test_dir: 用例路径
    :report_dir : 报告路径
    :name_project : 项目名称=>用于报告命名及描述
    :return: 无
    '''

    now = time.strftime("%Y_%m_%d %H_%M_%S")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 加载测试用例
    report_name = report_dir + now + '-' + name_project + '_test_report.html'  # 报告名称
    with open(report_name, 'wb') as f:  # 运行用例生成测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                               title=name_project + 'WebUI Auto Testing Report',
                                               description=(name_project + U"美多商城UI自动化功能回归测试"),
                                               verbosity=2)
        runner.run(discover)
        f.close()

    """
    stream:要操作的文件；
    title：测试报告标题；
    description：报告描述；
    verbosity：报告级别。
    """
