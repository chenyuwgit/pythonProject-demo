# -*- coding:utf-8 -*-
# 作者：NoamaNelson
# 日期：2021/8/17 13:31
# 文件名称：operate_request.py
# 作用：封装request请求和数据处理
# 联系：VX(NoamaNelson)
# 博客：https://blog.csdn.net/NoamaNelson


import json,time
import logging
import requests
from tools.write_excel import Write_excel
from tools.operate_conf import Conf
from tools.get_excel_data import GetExcelData
from tools.readExcel01 import ExcelData
import datetime
from tools.get_token import OperationHeader

log = logging.getLogger()


def send_requests(s, testdata):
    e = GetExcelData(testdata)
    verify = False
    res = {}                                                          # 接受返回数据
    false = False
    true = True
    null = None

    try:
        time.sleep(1)
        if e.test_method() == "POST" or e.test_method() == "post":
            r = s.request(method=e.test_method(),
                          url=e.test_url(),
                          params=e.test_params(),
                          headers=e.test_headers(),
                          data=e.test_body(),
                          verify=verify)

        elif e.test_method() == "GET" or e.test_method() == "get":
            r = s.request(method=e.test_method(),
                          url=e.test_url(),
                          headers=e.test_headers(),
                          verify=verify)

        elif e.test_method() == "PUT" or e.test_method() == "put":
            r = s.request(method=e.test_method(),
                          url=e.test_url(),
                          headers=e.test_headers(),
                          data=e.test_body(),
                          verify=verify)

        elif e.test_method() == "DELETE" or e.test_method() == "delete":
            r = s.request(method=e.test_method(),
                          url=e.test_url(),
                          headers=e.test_headers(),
                          data=e.test_body(),
                          verify=verify)
        else:
            print("请求方式错误")
            log.info("请求方式错误")

        print(f"【【======请求的用例id为：{e.test_id()}======】】")
        print(f"请求的接口名称和功能为：{e.test_name()}--》{e.test_function()}")
        # print("请求的接口名称和功能为：%s --》%s" % (e.test_name(), e.test_function()))
        # print("请求的接口名称和功能为：{} --》{}".format(e.test_name(), e.test_function()))

        print(f"请求头部：{e.test_headers()}")
        print(f"请求的方式为：{e.test_method()}")
        print(f"请求的数据为：{e.test_body()}")
        # print(f"依赖的用例id为：{e.relay_case}")
        # print(f"依赖的数据为：{e.relay_data}")
        # print(f"替换依赖数据后，真实的请求数据为：{e.uu}")

        log.info(f"【【======请求的用例id为：{e.test_id()}======】】")
        log.info(f"请求的接口名称和功能为：{e.test_name()}--》{e.test_function()}")
        log.info(f"请求头部：{e.test_headers()}")
        log.info(f"请求的方式为：{e.test_method()}")
        log.info(f"请求的数据为：{e.test_body()}")
        # log.info(f"依赖的用例id为：{e.relay_case}")
        # log.info(f"依赖的数据为：{e.relay_data}")
        # log.info(f"替换依赖数据后，真实的请求数据为：{e.uu}")

        print(f"页面返回信息：{r.content.decode('utf-8')}")
        log.info(f"页面返回信息：{r.content.decode('utf-8')}")
        res['id'] = e.test_id()
        res['name'] = e.test_name()
        res['function'] = e.test_function()
        res['rowNum'] = testdata['rowNum']
        res["status_code"] = str(r.status_code)                     # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        myres = res["text"]
        myres1 = eval(myres)
        Conf().writeConf(res['id'], res['id'], myres)               # 把接口返回值存入到config中

        res['response_msg'] = str(myres1["msg"])                    # 接口返回结果中的msg
        res['response_data'] = str(myres1["data"])                  # 接口返回结果中的data
        res['response_status'] = str(myres1["status"])              # 接口返回结果中的status
        # res['response_token'] = str(myres1["data"]["token"])      # 登录用户的token值
        res["times"] = str(r.elapsed.total_seconds())               # 接口请求时间转str

        if res["status_code"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["result_msg"] = ""

        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print(f"用例测试结果: {e.test_id()}---->{res['result']}")
            log.info(f"用例测试结果: {e.test_id()}---->{res['result']}")
        else:
            res["result"] = "fail"
            res["result_msg"] = f"{testdata['checkpoint']} not in {res['text']}"
        return res
    except Exception as r_msg:
        res["result_msg"] = str(r_msg)
        return r_msg


def write_result(result, filename="result.xlsx"):
    row_nub = result['rowNum']
    wt = Write_excel(filename)
    wt.write(row_nub, 13, result['status_code'])        # 写入返回状态码statuscode,第9列
    wt.write(row_nub, 14, result['times'])              # 耗时
    wt.write(row_nub, 15, result['error'])              # 状态码非200时的返回信息
    wt.write(row_nub, 17, result['result'])             # 测试结果 pass 还是fail
    wt.write(row_nub, 18, result['result_msg'])         # 抛异常
    wt.write(row_nub, 19, result['response_status'])    # 接口中返回的status
    wt.write(row_nub, 20, result['response_msg'])       # 接口中返回的msg
    wt.write(row_nub, 21, result['response_data'])      # 接口中返回的data
    # wt.write(row_nub, 21, result['response_token'])   # 接口中返回的token
