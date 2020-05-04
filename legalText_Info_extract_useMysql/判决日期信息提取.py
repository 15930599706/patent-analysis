
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
    file = docx.Document(row[1])
    for p in file.paragraphs:
        if bool(re.search(r'[〇|一|二|三|四|五|六|七|八|九]{2,4}年[一|二|三|四|五|六|七|八|九|十]{1,2}月(?:[一|二|三|四|五|六|七|八|九|十]{1,3}日)?', p.text)):
            if len(p.text) <= 15 :
                zh_Data = p.text.lstrip()
                # print(p.text.lstrip())
                # 一些处理0
                zh_Data = zh_Data.replace('××', '十')
                zh_Data = zh_Data.replace('○', '〇')
                zh_Data = zh_Data.replace('0', '〇')
                zh_Data = zh_Data.replace('异', '日')
                zh_Data = zh_Data.replace('本件', '二〇')
                zh_Data = zh_Data.replace('O', '〇')
                # print(zh_Data)

                year = zh_Data.split("年")[0]
                month = zh_Data.split("年")[1].split("月")[0]
                day = zh_Data.split("年")[1].split("月")[1].split("日")[0]
                if len(day) >= 3:
                    day = day[0] + day[2]
                chinese_english = dict(〇=0, 一=1, 二=2, 三=3, 四=4, 五=5, 六=6, 七=7, 八=8, 九=9, 十=10)
                year = "".join(str(chinese_english[i]) for i in year)
                month = "".join(str(chinese_english[i]) for i in month)
                day = "".join(str(chinese_english[i]) for i in day)
                if len(month) == 3:
                    month = month[0] + month[2]
                if len(day) == 3:
                    day = day[0] + day[2]
                final_date = year + "." + month + "." + day
                print(final_date)
                sql = """UPDATE `专利法律判决书库`.`allinfo` SET `判决日期` = %s WHERE `id` =  %s"""
                cursor.execute(sql,(final_date, row[0]))
    # subprocess.call("pause", shell=True)

