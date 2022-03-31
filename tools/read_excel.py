# # -*- coding:utf-8 -*-
# # 作者：NoamaNelson
# # 日期：2021/8/4 10:15
# # 文件名称：read_excel.py
# # 作用：封装读取excel用例数据方法
# # 联系：VX(NoamaNelson)
# # 博客：https://blog.csdn.net/NoamaNelson
#
# import xlrd
# from conf import config
#
#
# class ExcelUtil():
#
#     def __init__(self, excelPath, sheetName="Sheet1"):
#         self.data = xlrd.open_workbook(excelPath)
#         #self.table = self.data.sheet_by_name(sheetName)
#         #获取所有表格名称
#         self.tables=self.data.sheet_names()
#         self.keys = self.table.row_values(0)             # 获取第一行作为key值
#         self.rowNum = self.table.nrows                   # 获取总行数
#         self.colNum = self.table.ncols                   # 获取总列数
#
#     def dict_data(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
#         else:
#             r = []
#             j = 1
#             for i in list(range(self.rowNum-1)):
#                 s = {}
#                 s['rowNum'] = i+2                        # 从第二行取对应values值
#                 values = self.table.row_values(j)
#                 for x in list(range(self.colNum)):
#                     s[self.keys[x]] = values[x]
#                 r.append(s)
#                 j += 1
#             return r
#
#
# if __name__ == "__main__":
#     aa = ExcelUtil(config.CASE_EXCEL_PATH, sheetName="Sheet1")
#     print(aa.dict_data())
