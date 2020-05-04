import csv
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
csv_data = []
for row in results:
    line_data = []
    # 'id'
    line_data.append(row[0])

    # '专利类型4
    line_data.append(row[4])

    #'案件受理年份7'
    line_data.append(row[7])

    # #'案件判决年份8'
    #
    # str_split_0_4 = row[8]
    # print(str_split_0_4)
    # # print(str_split_0_4[0:4])
    # line_data.append(str_split_0_4[0:4])

    #'专利权人是否为外国人10'
    line_data.append(row[10])

    #'原告数量11'
    line_data.append(row[11])

    #'原告类型12',
    line_data.append(row[12])

    #'被告数量14'
    line_data.append(row[14])

    #'被告类型15',
    line_data.append(row[15])

    #'侵权企业规模16'
    line_data.append(row[16])

    # '请求赔偿金额17'
    # 0：0万
    # 1：0-1万
    # 2：1-10万
    # 3：10-20万
    # 4：20-50万
    # 5：50-100万
    # 6：100-1000万
    # 7：1000万+
    money_flag1 = 0
    nowMoney1 = row[17]
    nowMoney1 = float(nowMoney1)
    if nowMoney1 == 0:
        pass
    elif nowMoney1 > 0 and nowMoney1 <= 1:
        money_flag1 = 1
    elif nowMoney1 > 1 and nowMoney1 <= 10:
        money_flag1 = 2
    elif nowMoney1 > 10 and nowMoney1 <= 20:
        money_flag1 = 3
    elif nowMoney1 > 20 and nowMoney1 <= 50:
        money_flag1 = 4
    elif nowMoney1 > 50 and nowMoney1 <= 100:
        money_flag1 = 5
    elif nowMoney1 > 100 and nowMoney1 <= 1000:
        money_flag1 = 6
    elif nowMoney1 > 1000:
        money_flag1 = 7
    line_data.append(money_flag1)

    #'地区变量18'
    line_data.append(row[18])

    # '侵权行为数量19'
    line_data.append(row[19])

    # 请是否恶意侵权21
    line_data.append(row[21])

    # '赔偿金额20'
    # 0：0万
    # 1：0-1万
    # 2：1-10万
    # 3：10-20万
    # 4：20-50万
    # 5：50-100万
    # 6：100-1000万
    # 7：1000万+
    money_flag = ''
    nowMoney = row[20]
    nowMoney = float(nowMoney)
    if nowMoney == 0:
        money_flag = '0万'
    elif nowMoney>0 and nowMoney <= 1:
        money_flag = '0-1万'
    elif nowMoney>1 and nowMoney <= 10:
        money_flag = '1-10万'
    elif nowMoney> 10 and nowMoney <= 20:
        money_flag = '10-20万'
    elif nowMoney > 20 and nowMoney <= 50 :
        money_flag = '20-50万'
    elif nowMoney > 50 and nowMoney <= 100 :
        money_flag = '50-100万'
    elif nowMoney > 100 and nowMoney <= 1000:
        money_flag = '100-1000万'
    elif nowMoney > 1000:
        money_flag = '1000万+'
    line_data.append(money_flag)


    csv_data.append(line_data)

import pandas as pd
list_to_csv = list(csv_data)
print("全部含有赔偿金额的文本的数量：",len(list_to_csv))
# title=['id','专利类型','案件受理年份','案件判决年份','专利权人是否为外国人','原告数量','原告类型','被告数量','被告类型','侵权企业规模','请求赔偿金额','地区变量','侵权行为数量','是否恶意侵权','赔偿金额']
title=['id','专利类型','案件受理年份','专利权人是否为外国人','原告数量','原告类型','被告数量','被告类型','侵权企业规模','请求赔偿金额','地区变量','侵权行为数量','是否恶意侵权','赔偿金额']
outPd = pd.DataFrame(columns=title,data=list_to_csv)
print(outPd)
outPd.to_csv('all_original_data_3_csv(删除案件判决年份).csv', encoding='utf', index=False)