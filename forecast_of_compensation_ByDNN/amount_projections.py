# iris_keras_dnn.py
# Python 3.5.1, TensorFlow 1.6.0, Keras 2.1.5
# ========================================================
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


# 读取CSV数据集，并拆分为训练集和测试集
# 该函数的传入参数为CSV_FILE_PATH: csv文件路径
def load_data(CSV_FILE_PATH):
    dataDF = pd.read_csv(CSV_FILE_PATH)
    target_var = '赔偿金额'  # 目标变量
    # 数据集的特征，features是表头
    features = list(dataDF.columns)
    features.remove(target_var)
    features.remove('案件受理年份')
    # 目标变量的类别
    Class = dataDF[target_var].unique()

    # # 目标变量的类别字典，将目标变量转换成对应的数字
    # Class_dict = dict(zip(Class, range(len(Class))))
    Class_dict = {'0万': 0, '0-1万': 1, '1-10万': 2, '10-20万': 3, '20-50万': 4, '50-100万': 5, '100-1000万': 6, '1000万+': 7}

    # 增加一列target, 将目标变量进行编码
    dataDF['target'] = dataDF[target_var].apply(lambda x: Class_dict[x])

    # 对目标变量进行0-1编码(One-hot Encoding)，IRIS是新DF
    lb = LabelBinarizer()
    lb.fit(list(Class_dict.values()))
    transformed_labels = lb.transform(dataDF['target'])
    y_bin_labels = []  # 对多分类进行0-1编码的变量
    for i in range(transformed_labels.shape[1]):
        y_bin_labels.append('y' + str(i))
        dataDF['y' + str(i)] = transformed_labels[:, i]


    # 将数据集分为训练集和测试集
    train_x, test_x, train_y, test_y = train_test_split(dataDF[features], dataDF[y_bin_labels], \
                                                        train_size=0.7, test_size=0.3, random_state=1000)
    return train_x, test_x, train_y, test_y, Class_dict


def main():
    # 0. 开始
    print("\nIris dataset using Keras/TensorFlow ")
    # 设置随机数种子，程序每次执行生成的随机数是一样的
    # np.random.seed(4)
    # tf.set_random_seed(13)

    # 1. 读取CSV数据集
    print("Loading data into memory")
    CSV_FILE_PATH = 'all_original_data_3_csv(删除案件判决年份).csv'
    train_x, test_x, train_y, test_y, Class_dict = load_data(CSV_FILE_PATH)

    # 查看数据
    # print("train_x:", train_x)
    # print("test_x:", test_x)
    # print("train_y:", train_y)
    # print("test_y:", test_y)
    # print("Class_dict:", Class_dict)
    # subprocess.call("pause", shell=True)

    # 2. 定义模型
    init = K.initializers.glorot_uniform(seed=1)
    simple_adam = K.optimizers.Adam()
    model = K.models.Sequential()
    model.add(K.layers.Dense(units=22, input_dim=11, kernel_initializer=init, activation='sigmoid'))
    model.add(K.layers.Dense(units=33, kernel_initializer='random_uniform', activation='tanh'))
    model.add(K.layers.Dense(units=16, kernel_initializer='random_uniform', activation='tanh'))
    model.add(K.layers.Dense(units=8, kernel_initializer='random_uniform', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=simple_adam, metrics=['accuracy'])

    # 3. 训练模型
    b_size = 5
    max_epochs = 500
    print("Starting training ")
    h = model.fit(train_x, train_y, batch_size=b_size, epochs=max_epochs, shuffle=True, verbose=1)
    print("Training finished \n")

    # 4. 评估模型
    eval = model.evaluate(test_x, test_y, verbose=0)
    print("Evaluation on test data: loss = %0.6f accuracy = %0.2f%% \n" \
          % (eval[0], eval[1] * 100))

    # 5.模型保存
    model.save('DNN.model')

    # 5. 使用模型进行预测
    np.set_printoptions(precision=4)
    unknown = np.array([[1,1,0,1,0,1,4,4,2,5,0]], dtype=np.float32)
    predicted = model.predict(unknown)
    print("Using model to predict species for features: ")
    print(unknown)
    print("\nPredicted softmax vector is: ")
    print(predicted)
    species_dict = {v: k for k, v in Class_dict.items()}
    print("\nPredicted species is: ")
    print(species_dict[np.argmax(predicted)])


if __name__ == '__main__':
    main()
