import configparser
from conf import config
conf = configparser.ConfigParser()


class Conf:

    def readConf(self, m, n):
        """读取配置文件"""
        conf.read(config.RESPONSE_PATH)                                 # 文件路径
        name = conf.get(m, n)                                           # 获取指定section 的option值
        return name

    def writeConf(self, m, n, mm):
        """写入配置文件"""
        conf.read(config.RESPONSE_PATH)                                 # 文件路径

        if not conf.has_section(m):                                     # 判断section是否存在
            conf.add_section(m)
        if not conf.has_option(m, n):                                   # 判断的option是否存在
            conf.set(m, n, mm)                                          # 修改指定section 的option
        else:
            conf.set(m, n, mm)
        conf.write(open(config.RESPONSE_PATH, 'w'))                     # 写数据

# if __name__ == "__main__":
#      aa = Conf()
#      aa.writeConf("m", "n", "15")
if __name__ == "__main__":
    aa = Conf()
    aa.writeConf("m", "n", "15")
    r = aa.readConf("m", "n")
    print(f"读取后的数据为:{r}")
