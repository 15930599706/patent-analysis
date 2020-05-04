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
    print(row[0])
    print(row[9])
    print(row[12])

    # single = 0
    # mult = 1
    # # 原告数量
    # if len(row[9].split("、")) > 1 :
    #     sql = """UPDATE `专利法律判决书库`.`allinfo` SET `原告数量` = %s WHERE `id` =  %s"""
    #     cursor.execute(sql, (mult, row[0]))
    # else :
    #     sql = """UPDATE `专利法律判决书库`.`allinfo` SET `原告数量` = %s WHERE `id` =  %s"""
    #     cursor.execute(sql, (single, row[0]))
    #
    # # 被告数量
    # if len(row[12].split("、")) > 1:
    #     sql = """UPDATE `专利法律判决书库`.`allinfo` SET `被告数量` = %s WHERE `id` =  %s"""
    #     cursor.execute(sql, (mult, row[0]))
    # else:
    #     sql = """UPDATE `专利法律判决书库`.`allinfo` SET `被告数量` = %s WHERE `id` =  %s"""
    #     cursor.execute(sql, (single, row[0]))

    company = 1
    not_company = 0
    # 原告类型
    if bool(re.search('公司',row[9])) or bool(re.search('会社',row[9])):
        sql = """UPDATE `专利法律判决书库`.`allinfo` SET `原告类型` = %s WHERE `id` =  %s"""
        cursor.execute(sql, (company, row[0]))
    else:
        sql = """UPDATE `专利法律判决书库`.`allinfo` SET `原告类型` = %s WHERE `id` =  %s"""
        cursor.execute(sql, (not_company, row[0]))

    # 被告类型
    if bool(re.search('公司',row[12])):
        sql = """UPDATE `专利法律判决书库`.`allinfo` SET `被告类型` = %s WHERE `id` =  %s"""
        cursor.execute(sql, (company, row[0]))
    else:
        sql = """UPDATE `专利法律判决书库`.`allinfo` SET `被告类型` = %s WHERE `id` =  %s"""
        cursor.execute(sql, (not_company, row[0]))
