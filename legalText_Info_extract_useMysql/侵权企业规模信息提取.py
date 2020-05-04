import subprocess
import os
import re
import pymysql
import docx
import jieba
import csv
db = pymysql.connect("localhost", "root", "", "专利法律判决书库", charset='utf8')
cursor = db.cursor()
sql = "select * from `专利法律判决书库`.`allinfo` "
cursor.execute(sql)
results = cursor.fetchall()
# print(results)
cmopanySet = set()

# 公司统计

# for row in results:
#     print(row[0])
#     print(row[13])
#
#     if bool(re.search('公司',row[13])) or bool(re.search('会社',row[13])) or bool(re.search('厂',row[13])) or bool(re.search('行',row[13])) or bool(re.search('部',row[13])):
#         # sql = """UPDATE `专利法律判决书库`.`allinfo` SET `侵权企业规模` = %s WHERE `id` =  %s"""
#         # cursor.execute(sql, (0, row[0]))
#         IllegalInfo  = row[13].replace('等','')
#         # print(IllegalInfo)
#         tmpEleList = re.split("、",IllegalInfo)
#         for ele in tmpEleList:
#             if bool(re.search('公司', ele)) or bool(re.search('会社', ele)) or bool(
#                     re.search('厂', ele)) or bool(re.search('行', ele)) or bool(re.search('部', ele)):
#                 if len(ele) < 25 :
#                     cmopanySet.add(ele)
#                 # print(ele)
# print(list(cmopanySet))
#
# import pandas as pd
#
# list_to_csv = list(cmopanySet)
# print("全部公司的数量：",len(list_to_csv))
# title = ['name']
# companyPd = pd.DataFrame(columns=title,data=list_to_csv)
# print(companyPd)
# companyPd.to_csv('all_company_csv.csv', encoding='gbk', index=False)


# 执行自动化脚本，查询企业对应的注册资本



# 资本计算
csv_reader=csv.reader(open('all_company_result_csv.csv',encoding='GBK'))
date=[]    #创建列表准备接收csv各行数据
for one_line in csv_reader:
    date.append(one_line)

# 公司注册资本查询
def findCompany(cmp):
    # print(cmp)
    fcount = 0
    for line in date:
        # print(line[0])
        fcount = fcount + 1
        if cmp == line[0]:
            if str(line[1]) == '-':
                # print(10)
                return 10
            else:
                # print(line[1])
                return line[1]
        elif fcount == 2886:
            print('未找到')
            return 10

for row in results:
    print(row[0])
    print(row[13])
    subMoney = 0
    classify = 1
    if bool(re.search('公司',row[13])) or bool(re.search('会社',row[13])) or bool(re.search('厂',row[13])) or bool(re.search('行',row[13])) or bool(re.search('部',row[13])):
        # sql = """UPDATE `专利法律判决书库`.`allinfo` SET `侵权企业规模` = %s WHERE `id` =  %s"""
        # cursor.execute(sql, (0, row[0]))
        IllegalInfo  = row[13].replace('等','')
        # print(IllegalInfo)
        tmpEleList = re.split("、",IllegalInfo)
        for ele in tmpEleList:
            subMoney = subMoney + float(findCompany(ele))
            # print(ele)
    else:
        subMoney = 0
    print("总的注册资本：",subMoney)
    # 根据注册资本分类
    if subMoney >  0 and subMoney <= 10 :
        classify = 2
    elif subMoney >  10 and subMoney <= 100 :
        classify = 3
    elif subMoney > 100 and subMoney <= 500:
        classify = 4
    elif subMoney > 500 and subMoney <= 1000:
        classify = 5
    elif subMoney > 1000 :
        classify = 6
    print("公司分类：", classify)

    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `侵权企业规模` = %s WHERE `id` =  %s"""
    cursor.execute(sql, (classify, row[0]))