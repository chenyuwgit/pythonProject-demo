import unittest                                          # 引入unittest框架
import time
from page.goods import Goods                             # 引入页面元素
from selenium.webdriver import ActionChains              # 后续要拖动滚动条到指定元素
import logging


class TestGoods(unittest.TestCase):
    """
    创建测试用例集
    """
    def setUp(self):
        self.goods = Goods()                             # 实例化，登录
        self.driver = self.goods.driver                  # 调用同一个driver
        self.log = logging.getLogger()  # 初始化log

    def tearDown(self):
        self.goods.b.login_out()                         # 退出浏览器

#调用Page下对应的的元素，封装测试用例，测试流程操作  这里需要操作的内容
    def test_goods(self):
        self.log.info("======购物模块======")  # 加入log
        self.goods.phone_fun().click()  # 左侧“手机”一栏
        time.sleep(0.5)
        self.goods.phone_list_fun().click()  # 手机分类
        time.sleep(1)
        self.goods.goods_fun().click()  # 点击商品
        time.sleep(0.5)
        get_title = self.goods.goods_title_fun().text  # 验证商品标题
        print("需要加入购物车的商品标题为：", get_title)
        self.log.info("需要加入购物车的商品标题为：{}".format(get_title))  # 加入log

        cart = self.goods.add_cart_fun()  # 加入购物车
        action_chains = ActionChains(self.driver)
        action_chains.click(cart).perform()  # 拖动滚动条到指定元素
        time.sleep(1)
        self.goods.ok_fun()  # 确定
        time.sleep(2)
        mycart = self.goods.my_cart_fun()  # 我的购物车
        action_chains1 = ActionChains(self.driver)
        action_chains1.click(mycart).perform()
        time.sleep(1)
        get_title_new = self.goods.get_title_fun().text  # 货物标题
        print("加入购物车后获取到的标题为：", get_title_new)
        self.log.info("加入购物车后获取到的标题为：{}".format(get_title_new))  # 加入log

        time.sleep(0.5)
        self.goods.goods_del_fun().click()  # 删除
        print("删除成功了")
        time.sleep(1)
        #self.goods.back_heads_fun().click()  # 返回首页
        # 通过前面保存的老窗口的句柄，自己切换到老窗口
        #self.driver.switch_to.window()
        time.sleep(2)
        self.assertIn(get_title_new, get_title, "加入购物车失败！！！")
        self.log.info("======加入购物车失败！！！======")

