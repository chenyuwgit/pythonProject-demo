# -*- coding:utf-8 -*-
# 作者：NoamaNelson
# 日期：2021/8/14 13:36
# 文件名称：operate_json.py
# 作用：对json格式文件进行处理
# 联系：VX(NoamaNelson)
# 博客：https://blog.csdn.net/NoamaNelson

import json
from conf import config


class OperetionJson:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = config.TOKEN_PATH
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as fp:
            data1 = fp.read()
            if len(data1) > 0:
                data = json.loads(data1)
            else:
                data = {}
            return data

    # 写json
    def write_data(self, data):
        with open(config.TOKEN_PATH, 'w') as fp:
            fp.truncate()                                       # 先清空之前的数据，再写入，这样每次登录的token都是不一样的
            fp.write(json.dumps(data))

    #写cookie值
    def write_mydata(self,data):
        with open(config.COOKIE_PATH, 'w') as fp:
            fp.truncate()                                       # 先清空之前的数据，再写入，这样每次登录的cookie都是不一样的
            fp.write(json.dumps(data))


    # 根据关键字获取数据
    def get_data(self, id):
        print(type(self.data))
        return self.data[id]



if __name__ == "__main__":
    aa = OperetionJson()
    data = {"token": "1234567hdjfhjwhfwhejrhjwe46rewrjh"}
    aa.write_data(data)
    rdata = aa.read_data()
    print(f"读取到的数据为：{rdata}")
    gdata = aa.get_data("token")
    print(f"使用关键字的方法获取到的token值为：{gdata}")

