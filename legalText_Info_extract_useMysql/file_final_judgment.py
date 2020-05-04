import subprocess
import os
import re
import pymysql
import docx
import jieba
# path = 'D:\\毕设\\专利法律文件\\普通发明\\'
# path = 'D:\\毕设\\专利法律文件\\实用新型专利\\'
path = 'D:\\毕设\\专利法律文件\\外观专利\\'

db = pymysql.connect("localhost", "root", "", "专利法律判决书库", charset='utf8')
cursor = db.cursor()
# sql = "select * from `专利法律判决书库`.`发明专利` "
# sql = "select * from `专利法律判决书库`.`实用新型专利` "
sql = "select * from `专利法律判决书库`.`外观专利` "
cursor.execute(sql)
results = cursor.fetchall()
print(results)

for row in results:
    # path_id = row[0]
    # f = open(row[1],encoding='utf-8')
    # fread = f.read()
    file = docx.Document(row[1])
    print(row[1])
    for p in file.paragraphs:
        print(p.text)
        print(bool(re.search("驳回上诉，维持原判", p.text)))
        if bool(re.search("驳回上诉，维持原判", p.text)) :
            os.remove(row[1])
            break

