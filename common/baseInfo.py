from selenium import  webdriver
from common.readExcel  import  ExcelData
from selenium.webdriver.common.by import By
from common.creenShot import save_creenshot
import  time
import logging
from conf import config

class InitInfo(object):


    #初始化  封装
    # 此处正确的，通过访问self.name的形式，实现了：
    # 1.给实例中，增加了name变量
    # 2.并且给name赋了初值，为xxxx
    def __init__(self):
        self.login_name = "admin"  # 登录用户名
        self.login_password = "admin"  # 登录密码
        self.base_url =config.BASE_URL  # 登录网站
        self.driver = webdriver.Chrome()  # 指定使用Chrome浏览器
        self.log = logging.getLogger()  # 初始化log

    # 登录
    def login(self):
        # 引用文件读取类，获取表格数据
        self.e= ExcelData("登录")
        self.log.info("========登录======")
        # 首页打开
        self.driver.get(self.base_url)
        # 获取用户名+密码
        username=self.driver.find_element(By.CLASS_NAME,self.e.get_data("username"))
        username.clear()
        time.sleep(0.5)
        username.send_keys(self.login_name)  # 输入用户名
        self.log.info("输入的用户名为：{}".format(self.login_name))  # 加入log
        password=self.driver.find_element(By.CLASS_NAME,self.e.get_data("password"))
        password.clear()
        time.sleep(0.5)
        password.send_keys(self.login_password)  # 密码输入框
        self.log.info("输入的密码为：{}".format(self.login_password))  # 加入log

        time.sleep(1)
        #登录操作
        self.driver.find_element(By.CLASS_NAME,self.e.get_data("submit")).click()
        time.sleep(0.5)
        #判断是否登录成功
        if self.base_url == self.e.get_data("current_url"):
            print("登录成功！！！")
            self.log.info("======登录成功！！！======")  # 加入log
            # 截图保存
            save_creenshot(self.driver)
            # mainWindow变量保存当前窗口的句柄
            #self.mainWindow = wd.current_window_handle
        else:
            print("登录失败！！！请检查代码。。。")
            self.log.info("======登录失败！！！请检查代码。。。======")

    def login_out(self):
       time.sleep(1)
       self.driver.quit()
       self.log.info("======退出浏览器======")


# 调用
if __name__=='__main__':
    wb=InitInfo()
    wb.login()
    wb.login_out()



