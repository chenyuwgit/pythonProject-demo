# -*- coding:utf-8 -*-


import time

def save_creenshot(driver):

 try:
     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
     pic_path = "D:\\python-workpase\\pythonProject-demo\\creenshort\\.."+now+'_screen.png'                           # 保存截图到指定路径
     # print(pic_path)
     url = driver.save_screenshot(pic_path)                                       # 调用python自带的截图功能
     print("%s ：截图成功！！！" % url)
 except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)

