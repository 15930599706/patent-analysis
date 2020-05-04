import numpy as np
import pandas as pd
from sklearn.linear_model import BayesianRidge, LinearRegression, ElasticNet
from sklearn.svm import SVR
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor   # 集成算法
from sklearn.model_selection import cross_val_score    # 交叉验证
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# 数据导入
df = pd.read_csv('all_original_data_csv.csv',encoding = "gbk")
df = df.drop('id',axis=1)

# 自变量

# X = df[['赔偿金额']].values
X = df[['侵权行为数量','被告类型','侵权企业规模','专利类型']].values
# X = df[['侵权行为数量','被告类型','侵权企业规模','专利类型','被告数量','原告类型','专利权人是否为外国人','原告数量']].values
# X = df[['专利类型','案件受理年份','案件判决年份','专利权人是否为外国人','原告数量','原告类型','被告数量','被告类型','侵权企业规模','地区变量','侵权行为数量']].values

# 因变量
y = df[['赔偿金额']].values
# 设置交叉验证次数
n_folds = 10
# # 建立贝叶斯岭回归模型
# br_model = BayesianRidge()
# 普通线性回归
# lr_model = LinearRegression()

# # 弹性网络回归模型
# etc_model = ElasticNet()

# # 支持向量机回归
# svr_model = SVR()

# 梯度增强回归模型对象
gbr_model = GradientBoostingRegressor()

# 不同模型的名称列表
model_names = ['梯度增强回归模型']
# 不同回归模型
model_dic = [gbr_model]
# 交叉验证结果
cv_score_list = []
# 各个回归模型预测的y值列表
pre_y_list = []

# 读出每个回归模型对象
for model in model_dic:
    # 将每个回归模型导入交叉检验
    scores = cross_val_score(model, X, y, cv=n_folds)
    # 将交叉检验结果存入结果列表
    cv_score_list.append(scores)
    # 将回归训练中得到的预测y存入列表
    pre_y_list.append(model.fit(X, y).predict(X))
### 模型效果指标评估 ###
# 获取样本量，特征数
n_sample, n_feature = X.shape
# 回归评估指标对象列表
model_metrics_name = [explained_variance_score, mean_absolute_error, mean_squared_error, r2_score]
# 回归评估指标列表
model_metrics_list = []
# 循环每个模型的预测结果
for pre_y in pre_y_list:
    # 临时结果列表
    tmp_list = []
    # 循环每个指标对象
    for mdl in model_metrics_name:
        # 计算每个回归指标结果
        tmp_score = mdl(y, pre_y)
        # 将结果存入临时列表
        tmp_list.append(tmp_score)
    # 将结果存入回归评估列表
    model_metrics_list.append(tmp_list)
df_score = pd.DataFrame(cv_score_list, index=model_names)
df_met = pd.DataFrame(model_metrics_list, index=model_names, columns=['ev(方差)', 'mae(平均绝对误差)', 'mse(均方差)', 'r2(判定系数)'])

# 各个交叉验证的结果
print(df_score)

# 各种评估结果
print(df_met)

### 可视化 ###
# 创建画布
plt.figure(figsize=(18, 12))
# 颜色列表
color_list = ['r', 'g', 'b', 'y', 'c']
# 循环结果画图
for i, pre_y in enumerate(pre_y_list):
    # 子网络
    plt.subplot(2, 3, i+1)
    # 画出原始值的曲线
    plt.plot(np.arange(X.shape[0]), y, color='k', label='原始值')
    # 画出各个模型的预测线
    plt.plot(np.arange(X.shape[0]), pre_y, color_list[i], label=model_names[i])
    plt.title(model_names[i])
    plt.legend(loc='lower left')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.savefig('回归模型拟合结果_相关度前四自变量与因变量.png')
plt.show()
