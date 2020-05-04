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
print(results)


for row in results:
    print(row[0])
    rowCount = 0
    file = docx.Document(row[1])
    for p in file.paragraphs:
        if rowCount == 1 :
            print(p.text)
            sql = """UPDATE `专利法律判决书库`.`allinfo` SET `审理法院` = %s WHERE `id` =  %s"""
            cursor.execute(sql,(p.text, row[0]))
        # print(p.text)
        rowCount = rowCount + 1
    # subprocess.call("pause", shell=True)

