# -*- coding:utf-8 -*-
# 作者：NoamaNelson
# 日期：2021/8/4 9:47
# 文件名称：config.py
# 作用：存放全局变量
# 联系：VX(NoamaNelson)
# 博客：https://blog.csdn.net/NoamaNelson

import os
import time

# ========== 项目相关 ==========
# import PROJECT_NAME as PROJECT_NAME

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))                 # 项目根目录

# ==========用例目录 Excel目录 ==========
TEST_EXCEL_PATH = os.path.join(BASE_PATH, "case")                                       # excel测试用例的路径
CASE_EXCEL_PATH = os.path.join(BASE_PATH, "case", "case_excel.xls")                    # excel测试用例的指定路径

# ========== 用户数据相关 ==========
TOKEN_PATH = os.path.join(BASE_PATH, "data", "token.json")                              # 存储登录的token

COOKIE_PATH = os.path.join(BASE_PATH, "data", "cookie.json")                            # 存储登录的cookie

RESPONSE_PATH = os.path.join(BASE_PATH, "data", "response.conf")                        # 存储所有的接口返回值

# ========== 接口请求公用数据 ==========
BASE_URL = "http://mp-meiduo-python.itheima.net/login/"                                                      # 接口请求基地址

# # ========== 登录常用账号密码 ==========
# login_name = "admin"  # 登录用户名
# login_password = "admin"

# # ========== 日志存放路径 ==========
# REPORT_PATH = os.path.join(BASE_PATH, "report")                                         # 测试报告存放路径
# REPORT_PATH_NAME = os.path.join(REPORT_PATH, f"{PROJECT_NAME}-{NOW_TIME}-result.html")  # 测试报告名称(html)
# REPORT_EXCEL = os.path.join(REPORT_PATH, f"{PROJECT_NAME}-{NOW_TIME}-result.xlsx")      # 测试报告名称(xlsx)


if __name__ == "__main__":
    print(BASE_PATH)
    print(CASE_EXCEL_PATH)
