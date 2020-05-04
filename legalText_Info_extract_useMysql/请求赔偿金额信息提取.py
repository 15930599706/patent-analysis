import csv
import subprocess
import os
import re
import pymysql
import docx
import jieba

db = pymysql.connect("localhost", "root", "", "专利法律判决书库", charset='utf8')
cursor = db.cursor()
sql = "select * from `专利法律判决书库`.`allinfo` "
cursor.execute(sql)
results = cursor.fetchall()
# print(results)
# all1 = 0
# find1 = 0
# 经济损失 = 0
# 带有赔偿金额的文本 = 0
# 其他 = 0
# data = []
# for row in results:
#     KeyWordsFlag = 0
#     print(row[0])
#     # 找出一审案件
#     if row[2].split("审")[0][-1] == '一':
#         # all1 += 1
#         file = docx.Document(row[1])
#         for p in file.paragraphs:
#             if KeyWordsFlag == 0:
#                 # 诉称\诉讼请求\上诉请求
#                 if re.search("诉称", p.text) or re.search("诉讼请求", p.text) or re.search("上诉请求", p.text):
#                     KeyWordsFlag = 1
#                     find1 += 1
#
#                     if re.search("经济损失", p.text) or re.search("费用", p.text):
#                         if re.search("：", p.text):
#                             经济损失 += 1
#                             tmpText = p.text.split("：")[1]
#                             money = ''
#                             # print('tmpText', tmpText)
#                             if re.search("经济损失", tmpText):
#                                 money = tmpText.split("经济损失")[1]
#                             elif re.search("费用", tmpText):
#                                 money = tmpText.split("费用")[1]
#                             tmpData = []
#                             tmpData.append(row[0])
#                             if re.search("元", money):
#                                 print(money.split("元")[0])
#                                 带有赔偿金额的文本 += 1
#                                 tmpData.append(money.split("元")[0])
#                             else:
#                                 其他 += 1
#                                 print(tmpText)
#                                 tmpData.append(tmpText)
#                             data.append(tmpData)
#
#     # subprocess.call("pause", shell=True)
#
# # print(all1)
# print(find1)
# print(经济损失)
# print(带有赔偿金额的文本)
# print(其他)
# print(len(data))
#
# import pandas as pd
# list_to_csv = list(data)
# print("全部含有赔偿金额的文本的数量：",len(list_to_csv))
# title = ['id','money']
# moneyPd = pd.DataFrame(columns=title,data=list_to_csv)
# print(moneyPd)
# moneyPd.to_csv('请求赔偿金额_csv.csv', encoding='utf', index=False)

# 写回数据库
csv_reader=csv.reader(open('请求赔偿金额_csv.csv',encoding='utf'))
wdate=[]    #创建列表准备接收csv各行数据
for one_line in csv_reader:
    wdate.append(one_line)

for ele in wdate:
    print(ele[0],ele[1])
    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `请求赔偿金额` = %s WHERE `id` =  %s"""
    cursor.execute(sql, (ele[1], ele[0]))
