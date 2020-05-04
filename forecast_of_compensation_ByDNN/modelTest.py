# 导入模块
import os
import numpy as np
import subprocess
# import keras as K
# import tensorflow as tf
import tensorflow.compat.v1 as tf
from tensorflow import keras as K
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import warnings

warnings.filterwarnings("ignore")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

Class_dict = {'0万': 0, '0-1万': 1, '1-10万': 2, '10-20万': 3, '20-50万': 4, '50-100万': 5, '100-1000万': 6, '1000万+': 7}

ansList = []

if __name__ == '__main__':
    # 模型加载
    model = K.models.load_model("DNN.model")

    # 测试集读取
    dataDF = pd.read_csv("test.csv")
    target_var = '赔偿金额'  # 目标变量
    # # 数据集的特征，features是表头
    # features = list(dataDF.columns)
    # features.remove(target_var)
    predictDF = dataDF
    # predictDF = predictDF.drop(target_var, axis=1)
    predictList = predictDF.values.tolist()
    print(type(predictList))
    print(predictList)
    # subprocess.call("pause", shell=True)
    for ele in predictList:
        # 去除案件受理年份
        tmpList = []
        head = ele[0:1]
        back = ele[2:12]
        head.extend(back)
        tmpList.append(head)

        print(tmpList)
        unknown = np.array(tmpList, dtype=np.float32)
        predicted = model.predict(unknown)
        print(predicted)
        species_dict = {v: k for k, v in Class_dict.items()}
        print("\nPredicted species is: ")
        print(species_dict[np.argmax(predicted)])
        ele.append(species_dict[np.argmax(predicted)])
    print(predictList)


    import pandas as pd
    list_to_csv = list(predictList)
    print("全部含有赔偿金额的文本的数量：", len(list_to_csv))
    outPd = pd.DataFrame(data=list_to_csv)
    print(outPd)
    outPd.to_csv('test_result.csv', encoding='utf', index=False)

    allNums = 0
    rightNums = 0
    for ele in predictList:
        if ele[12] == ele[13]:
            rightNums += 1
        allNums += 1

    acc = rightNums / allNums
    print(allNums, rightNums, acc)






    # unknown = np.array([[1, 2015, 0, 0, 1, 1, 1, 6, 5, 3, 5, 0]], dtype=np.float32)
    # predicted = model.predict(unknown)
    # print("Using model to predict species for features: ")
    # print(unknown)
    # print("\nPredicted softmax vector is: ")
    # print(predicted)

