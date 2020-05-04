import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataDf = pd.read_csv('all_original_data_2_csv.csv',encoding = "utf")
dataDf = dataDf.drop('id',axis=1)

# 可视化数据关系(数据分布)
sns.set(style='whitegrid', context='notebook')   #style控制默认样式,context控制着默认的画幅大小
sns.pairplot(dataDf, height=2)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.savefig('原始数据分布.png')

# 计算皮尔逊系数,并排序输出
dataCor = dataDf.corr()
relData = []

for i,j in zip(dataCor.columns.values.tolist(),dataCor.iloc[-1].values.tolist()):
    tmpList = []
    tmpList.append(i)
    tmpList.append(abs(j))
    # print(tmpList)
    relData.append(tmpList)
# print(sorted(relData,key=(lambda x:x[1]),reverse=True))
print("['相关因素', '相关度']")
for ele in sorted(relData,key=(lambda x:x[1]),reverse=True):
    print(ele)

# 皮尔逊系数矩阵可视化
plt.figure(figsize=(12, 12))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
sns.heatmap(dataCor, annot=True, vmax=1, square=True, cmap="Blues")
plt.savefig('原始数据相关性分析.png')
# plt.show()


