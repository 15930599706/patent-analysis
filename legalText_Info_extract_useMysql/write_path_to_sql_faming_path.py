import os
import re
import pymysql
from time import sleep


rootdir=os.path.join('D:\\毕设\\专利法律文件\\普通发明')

db = pymysql.connect("localhost", "root", "", "专利法律判决书库", charset='utf8')
cursor = db.cursor()

count = 1
for (dirpath,dirnames,filenames) in os.walk(rootdir):
    for filename in filenames:
        if os.path.splitext(filename)[1]=='.docx':
            # write_path.write(dirpath + '\\' + filename + '\n')
            cursor = db.cursor()
            # sql = """INSERT INTO `法院`.`小学_path`(`appraisal_id`, `movie`, `direct`) VALUES ( %s,%s, %s)"""
            sql = """INSERT INTO `专利法律判决书库`.`发明专利`(id,path,name) VALUES ( %s,%s,%s)"""
            val = (count,dirpath + '\\' + filename,re.sub(".docx","",filename))
            cursor.execute(sql, val)
            count = count + 1

