# -*- coding:utf-8 -*-
# 作者：NoamaNelson
# 日期：2021/8/16 13:17
# 文件名称：get_token.py
# 作用：封装token和cookie的获取方法，并把获取到的结果存到对应的配置文件中
# 联系：VX(NoamaNelson)
# 博客：https://blog.csdn.net/NoamaNelson


import json
import requests
from conf import config
from tools.operate_json import OperetionJson
from conf import config

# 特别提醒：以下token和cookie的获取方法根据具体项目修改，本次是依据学生管理系统修改的


class OperationHeader:

    def __init__(self, response):
        # self.response = json.loads(response)
        self.response = response

    def get_response_token(self):
        """获取登录返回的token"""
        token = {"data": {"token": self.response['data']['token']}}
        return token

    def write_token(self):
        op_json = OperetionJson()
        op_json.write_data(self.get_response_token())

    def get_response_msg(self):
        reponse_msg = {"msg": self.response['msg']}
        return reponse_msg

    def get_response_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.response.cookies)
        # cookie = self.response['Set-Cookie'].split(";")[0]
        return cookie

    def write_cookie(self):
        op = OperetionJson()
        cookie_login_done = self.get_response_cookie()
        print(f"登录之后的cookie为：{cookie_login_done}")
        cookie_login_doing = json.loads(config.COOKIE_PATH)
        print(f"登录之前携带的cookie为：{cookie_login_doing}")
        values1 = cookie_login_done["session"]
        values2 = cookie_login_doing["cookie"]
        cookie_login_get = {"cookie": "session=" + values1 + ";" + values2}
        print(f"后续接口依赖的cookie为：{cookie_login_get}")
        op.write_mydata(cookie_login_get)

if __name__ == "__main__":
    url = "http://mp-meiduo-python.itheima.net/login/"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = {"admin": "admin", "pwd": "admin"}
    res = requests.post(url=url, json=data, headers=headers)
    aa = OperationHeader(res)
    aa.write_cookie()
