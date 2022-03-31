import json
import logging
from tools.operate_json import OperetionJson
from tools.operate_conf import Conf
from conf import config

log = logging.getLogger()

class GetExcelData():

    """获取excel数据"""
    def __init__(self, testdata):
            self.testdata = testdata
    def test_name(self):
            test_name = self.testdata["name"]                           # 用例名称
            return test_name
    def test_function(self):
            test_function = self.testdata["function"]                   # 用例功能
            return test_function
    def test_id(self):
            test_nub = self.testdata['id']                               # 用例id
            return test_nub
    def test_method(self):
            method = self.testdata["method"]                             # 请求方式
            return method
    def test_url(self):
            url = config.BASE_URL + self.testdata["url_address"]         # 请求url
            return url
    def test_params(self):
            try:                                                         # url后面的params参数
                params = eval(self.testdata["params"])
            except:
                params = None
            return params
    def test_headers(self):
            try:                                                         # 请求头部headers
                headers = eval(self.testdata["headers"])
                if self.testdata["token"] == "yes":
                    op_json = OperetionJson(config.TOKEN_PATH)
                    token = op_json.get_data('data')
                    headers = dict(headers, **token)
                elif self.testdata["cookie"] == "yes":
                    op_json = OperetionJson(config.COOKIE_PATH)
                    cookie = op_json.get_data('cookie')
                    headers = dict(headers, **cookie)
                elif self.testdata["token"] == "yes" and self.testdata["cookie"] == "yes":
                    op_json = OperetionJson(config.TOKEN_PATH)
                    token = op_json.get_data('data')
                    headers_g = dict(headers, **token)
                    op_json1 = OperetionJson(config.COOKIE_PATH)
                    cookie = op_json1.get_data('cookie')
                    headers = dict(headers_g, **cookie)

            except:
                headers = None
            return headers


    def test_body(self):
            try:  # 请求data数据
                bodydata = eval(self.testdata["body"])
            except:
                bodydata = {}

            # ==================单层依赖数据处理，可进行扩展==========
            body = json.dumps(bodydata)
            try:
                if self.testdata['relay_case'] != "":
                    relay_case = self.testdata['relay_case']
                    print(f"依赖的用例id为：{relay_case}")
                    log.info(f"依赖的用例id为：{relay_case}")
                    get_relay = Conf().readConf(relay_case, relay_case)
                    get_relay1 = json.loads(get_relay)
                    relay_data = self.testdata['relay_data']
                    log.info(f"依赖的数据为：{relay_data}")
                    print(f"依赖的数据为：{relay_data}")
                    uu = get_relay1[relay_data]
                    json.loads(body)[relay_data] = uu
                    log.info(f"替换依赖数据后，真实的请求数据为：{uu}")
                    print(f"替换依赖数据后，真实的请求数据为：{uu}")
                # ==================单层依赖数据处理，可进行扩展==========
                else:
                    body = json.dumps(bodydata)
            except:
                body = json.dumps(bodydata)
            return body


