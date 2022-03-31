from common.baseInfo import InitInfo
from  common.readExcel import ExcelData
from selenium.webdriver.common.by import By


class Goods(object):

    def __init__(self):
            self.a = ExcelData("购物")  # 实例化
            self.b = InitInfo()  # 实例化
            self.b.login()  # 登录
            self.driver = self.b.driver  # 调用同一个driver

    # 封装页面元素包装
    def phone_fun(self):
        #return self.driver.find_element(self.a.get_data("phone"))  # 左侧“手机”一栏
        return self.driver.find_element(By.XPATH,self.a.get_data("phone"))  # 左侧“手机”一栏

    def phone_list_fun(self):
        return self.driver.find_element(By.XPATH,self.a.get_data("phone_list"))  # 手机分类

    def goods_fun(self):
        return self.driver.find_element(By.XPATH,self.a.get_data("goods"))  # 商品

    def goods_title_fun(self):
        return self.driver.find_element(By.XPATH,self.a.get_data("goods_title"))  # 商品标题

    def add_cart_fun(self):
        return self.driver.find_element(By.XPATH,self.a.get_data("add_cart"))  # 加入购物车

    def ok_fun(self):
        return self.driver.switch_to.alert.accept()  # 确定

    def my_cart_fun(self):
        return self.driver.find_element(By.XPATH,self.a.get_data("my_cart"))  # 我的购物车

    def get_title_fun(self):
        return self.driver.find_element(By.XPATH,self.a.get_data("get_title"))  # 获取标题

    def goods_del_fun(self):
        return self.driver.find_element(By.XPATH,self.a.get_data("goods_del"))  # 删除

    def back_heads_fun(self):
        return self.driver.find_element(self.a.get_data("back_heads"))  # 返回首页



