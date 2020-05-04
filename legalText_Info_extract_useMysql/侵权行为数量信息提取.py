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

for row in results:
    lineCount = 0
    IllegalNum = 0
    # 制造、销售、生产、使用、进口 都是侵权行为
    # manufacturing, sales, production, use,import
    manufacturingFlag = 0
    sales = 0
    production = 0
    use = 0
    illegalImport = 0
    print(row[0])
    file = docx.Document(row[1])
    for p in file.paragraphs:
        lineCount = lineCount + 1
        if bool(re.search('制造', p.text)) and manufacturingFlag == 0:
            manufacturingFlag = 1
        if bool(re.search('销售', p.text)) and sales == 0:
            sales = 1
        if bool(re.search('生产', p.text)) and production == 0:
            production = 1
        if bool(re.search('使用', p.text)) and use == 0:
            use = 1
        if bool(re.search('进口', p.text)) and illegalImport == 0:
            illegalImport = 1
        if manufacturingFlag == 1 and sales == 1 and production == 1 and use == 1 and illegalImport == 1:
            break
    IllegalNum = manufacturingFlag + sales + production + use + illegalImport
    print(IllegalNum)

    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `侵权行为数量` = %s WHERE `id` =  %s"""
    cursor.execute(sql, (IllegalNum, row[0]))



