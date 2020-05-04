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


# for row in results:
#     yearInf = ''
#     file = docx.Document(row[1])
#     print(row[0])
#     yearInf = row[6].split("）")[0].split("（")[1]
#     print(yearInf)
#     sql = """UPDATE `专利法律判决书库`.`allinfo` SET `案件受理时间` = %s WHERE `id` =  %s"""
#     cursor.execute(sql, (yearInf, row[0]))
#     # subprocess.call("pause", shell=True)

for row in results:
    areaInf = ''
    file = docx.Document(row[1])
    print(row[0])
    areaInf = row[6].split("）")[1]
    print(areaInf[0])
    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `地区变量` = %s WHERE `id` =  %s"""
    cursor.execute(sql, (areaInf[0], row[0]))
    # subprocess.call("pause", shell=True)