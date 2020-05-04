# keras_dnn.py
# ======================环境信息=========================
# python3.7.6
# tensorflow2.0.0b0
# Keras2.2.4
# numpy1.16.4
#easydict1.9
# ========================================================

# 导入模块
import os
import numpy as np
import argparse
import datetime
import csv
from easydict import EasyDict as edict
from tensorflow import keras as K
import warnings

warnings.filterwarnings("ignore")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

Class_dict = {'0万': 0, '0-1万': 1, '1-10万': 2, '10-20万': 3, '20-50万': 4, '50-100万': 5, '100-1000万': 6, '1000万+': 7}


def interface(textUUIDParam, featuresList):
    """
    :param textUUIDParam:
    :param featuresList: 特征值List
    :return:无返回值
    """
    textUUID = textUUIDParam + '_'
    outputPath = 'Y:\\myPyCharmWorkStation\\graduation_project\\分类模型\\DNN_model_package\\output\\'
    # 将featuresList字符串,转换为数组
    featuresList = featuresList.replace(' ', '')
    featuresList = featuresList.replace(']', '').replace('[', '').split(',')
    featuresList = list(map(int, featuresList))
    print('featuresList',featuresList)

    # 起始时间
    start_time = datetime.datetime.now()
    print("程序起始时间：", start_time)

    # 模型加载
    model = K.models.load_model("Y:\\myPyCharmWorkStation\\graduation_project\\分类模型\\DNN_model_package\\DNN.model")
    print('模型加载...')

    # 特征值list处理
    tmpL = []
    tmpL.append(featuresList)
    print('tmpL',tmpL)
    features = np.array(tmpL, dtype=np.float32)

    # 模型调用
    print('模型预测...')
    predicted = model.predict(features)
    print("Using model to predict species for features: ")
    print(features)

    print("\nPredicted softmax vector is: ")
    predicted_softmax_vector = predicted
    print(predicted_softmax_vector)

    species_dict = {v: k for k, v in Class_dict.items()}
    result = species_dict[np.argmax(predicted)]
    print("\nPredicted species is: ")
    print(result)

    # 终止时间
    stop_time = datetime.datetime.now()
    print("程序终止时间：", stop_time)
    # 程序执行总时间
    total_time = (stop_time - start_time).microseconds / 1000
    print("程序执行总时间(ms)：", total_time)

    # 保存模型输出信息
    ## 保存摘要模型报告文件
    modelOutputFileName = outputPath + textUUID + "ModelOutput.csv"
    f = open(modelOutputFileName, mode='w', newline='')
    outputFileHeader = ['result', 'features', 'predicted_softmax_vector', 'start_time', 'stop_time', 'total_time']
    w = csv.DictWriter(f, outputFileHeader)
    w.writeheader()
    csv_dict = edict()
    csv_dict.result = str(result)
    csv_dict.features = str(features)
    csv_dict.predicted_softmax_vector = str(predicted_softmax_vector)
    csv_dict.start_time = str(start_time)
    csv_dict.stop_time = str(stop_time)
    csv_dict.total_time = str(total_time)
    w.writerow(csv_dict)
    f.close()

    return


if __name__ == '__main__':
    # featuresList 的一个例子:[1, 1, 0, 1, 0, 1, 4, 4, 2, 5, 0]
    # 专利类型,专利权人是否为外国人,原告数量,原告类型,
    # 被告数量,被告类型,侵权企业规模,请求赔偿金额,
    # 地区变量,侵权行为数量,是否恶意侵权

    # 模型封装
    parser = argparse.ArgumentParser(description='These are the parameters of the training model')
    parser.add_argument('--textUUIDParam', type=str, default=None, required=True, help='File unique identification')
    parser.add_argument('--featuresList', type=str, default=None, required=True, help='Features List')
    args = parser.parse_args()  # parse_args()从指定的选项中返回一些数据
    interface(textUUIDParam=args.textUUIDParam, featuresList=args.featuresList)
