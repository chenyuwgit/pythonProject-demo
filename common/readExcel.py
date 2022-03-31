# coding:utf-8

# 作者：NoamaNelson
# 日期：2021/2/26 13:24
# 文件名称：read_Excel.py
# 作用：读取page下的WebElement.xlsx

import xlrd                                         # 引入xlrd库，用来对excel数据读取
class ExcelData():
    """
    用来封装读取Excel数据的公用方法
    """

    def __init__(self, sheetName):
        """
        :param sheetName: 初始化传入的是sheet的名称
        """
        self.excel_path = "D:\python-workpase\pythonProject-demo\page\WebElement.xls"  # 指定Excel读取的路径

        self.data = xlrd.open_workbook(self.excel_path)  # 打开Excel
        self.table = self.data.sheet_by_name(sheetName)  # 通过sheet name的方式打开Excel
        self.keys = self.table.col_values(1)             # 获取第二列作为key值
        self.row_num = self.table.nrows                  # 获取总行数
        self.col_num = self.table.ncols                  # 获取总列数

    def dict_data(self):
        if self.row_num < 1:
            print("总行数小于1")
        else:
            r = []
            s = {}
            values = self.table.col_values(2)            # 获取第三列作为values值
            for x in list(range(1, self.row_num)):       # 遍历所有的行，并把每行的数据放入list中
                s[self.keys[x]] = values[x]              # 把行对应列的数据拿出来放入s字典中
            r.append(s)                                  # 每次取到的数据放入列表
            return r

    def list_to_dict(self):
        return self.dict_data()[0]                       # 取出列表中的字典

    def get_data(self, value):
        return self.list_to_dict()[value]                # 取字典中对应的values值

if __name__ == "__main__":
    sheetName = "购物"
    a = ExcelData(sheetName)
    print("读取到excel中第二列和第三列对应的数据为：", a.dict_data())
    print("读取的数据为列中，把列中中的字典取出来为：", a.list_to_dict())
    print("取excel中current_url的具体值为：", a.get_data("phone"))  # 后续要取excel中第二列对应的元素属性值，只需要写第二列元素名称即可
