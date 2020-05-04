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
    print(row[0])
    print(row[9])
    print(row[10])
    if row[10] is None :
        file = docx.Document(row[1])
        for p in file.paragraphs:
            lineCount = lineCount + 1
            if lineCount < 20 :
                if bool(re.search('美利坚合众国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, row[0]))
                if bool(re.search('大韩民国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, p.text))
                if bool(re.search('大不列颠及北尔爱兰联合王国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, row[0]))
                if bool(re.search('联邦德国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, row[0]))
                if bool(re.search('意大利共和国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, row[0]))
                if bool(re.search('德意志联邦共和国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, row[0]))
                if bool(re.search('法兰西共和国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, row[0]))
                if bool(re.search('日本国', p.text)) :
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (1, row[0]))
                else:
                    sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
                    cursor.execute(sql, (0, row[0]))
    # if bool(re.search('会社', row[9])) or bool(re.search('(中国)', row[9])):
    #     sql = """UPDATE `专利法律判决书库`.`allinfo` SET `专利权人是否为外国人` = %s WHERE `id` =  %s"""
    #     cursor.execute(sql, (1, row[0]))


