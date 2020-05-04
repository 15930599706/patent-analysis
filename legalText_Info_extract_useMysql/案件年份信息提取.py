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
    print("当前判决书为：《《《《",row[2])
    rowCount = 0
    file = docx.Document(row[1])
    for p in file.paragraphs:
        # 案件年份信息
        if rowCount == 3 :
            print(p.text)
            sql = """UPDATE `专利法律判决书库`.`allinfo` SET `案件年份` = %s WHERE `id` =  %s"""
            cursor.execute(sql,(p.text, row[0]))
        rowCount = rowCount + 1
