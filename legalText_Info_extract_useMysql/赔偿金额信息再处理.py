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

# # 写入败诉案件
# loseCount = 0
# anomalyCount = 0
# loseCount = 0
# winCount = 0
# bohuiCount = 0
# rmbCount = 0
# id = []
# moneyText = []
# for row in results:
#     money_all = 0
#     print('-------------------------------------------')
#     print(row[16])
#     if row[16] == '0' :
#         print(row[0])
#         all_text = ''
#         file = docx.Document(row[1])
#         for p in file.paragraphs:
#             all_text = all_text + p.text
#                             # sql = """UPDATE `专利法律判决书库`.`allinfo` SET `赔偿金额` = %s WHERE `id` =  %s"""
#                             # cursor.execute(sql, (money_all, row[0]))
#         # print(all_text)
#         if bool(re.search("判决如下", all_text)):
#             result_text = re.split('判决如下',all_text)[1]
#
#             #对文本进行处理
#             if bool(re.search("：　　驳回", result_text)):
#                 loseCount =  loseCount + 1
#             else:
#                 winCount = winCount + 1
#                 if bool(re.search("驳回", result_text)):
#                     i_result_text = re.split('驳回',result_text)[0]
#                     print(i_result_text)
#                     bohuiCount = bohuiCount + 1
#                     if bool(re.search("经济损失", i_result_text)):
#                         print(re.split('经济损失',result_text)[1])
#                         rmbCount = rmbCount + 1
#
#                         moneyText.append(re.split('元', re.split('经济损失',result_text)[1])[0])
#                     else:
#                         moneyText.append(result_text)
#                     id.append(row[0])
#         else:
#             anomalyCount = anomalyCount + 1
#             print('不规则文本')
#
#         # subprocess.call("pause", shell=True)
#
# print("不规则文本数量：",anomalyCount)
# print("失败数量：",loseCount)
#
# print("成功数量：",winCount)
# print("成功中含有驳回的数量：",bohuiCount)
# print("成功中含有驳回的中含有经济损失的数量：",rmbCount)
#
# print(len(id))
# print(len(moneyText))
# data = []
# for x, y in zip(id, moneyText):
#     tmpList = []
#     tmpList.append(x)
#     tmpList.append(y)
#     print(tmpList)
#     data.append(tmpList)
# import pandas as pd
# list_to_csv = list(data)
# print("全部含有赔偿金额的文本的数量：",len(list_to_csv))
# title = ['id','money']
# moneyPd = pd.DataFrame(columns=title,data=list_to_csv)
# print(moneyPd)
# moneyPd.to_csv('all_money_csv.csv', encoding='utf', index=False)

# 写回数据库
csv_reader=csv.reader(open('all_money_csv.csv',encoding='utf'))
wdate=[]    #创建列表准备接收csv各行数据
for one_line in csv_reader:
    wdate.append(one_line)

for ele in wdate:
    print(ele[0],ele[1])
    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `赔偿金额` = %s WHERE `id` =  %s"""
    cursor.execute(sql, (ele[1], ele[0]))

