# -*- coding: utf-8 -*-

import gensim
import math
import jieba
import jieba.analyse as analyse
import datetime
import csv
from easydict import EasyDict as edict
import argparse
import warnings

warnings.filterwarnings("ignore")

''' ------------------------------------------------------- 
    基本步骤：
        1.分别统计两个文档的关键词
        2.两篇文章的关键词合并成一个集合,相同的合并,不同的添加
        3.计算每篇文章对于这个集合的词的词频 TF-IDF算法计算权重
        4.生成两篇文章各自的词频向量
        5.使用训练好的Word2Vec模型对VSM向量进行强化（如果存在近义词，那么久增加该词的权重）
        6.计算两个向量的余弦相似度,值越大表示越相似                             
    ------------------------------------------------------- '''


# 统计关键词及个数
def CountKey(fileName, resultName):
    try:
        # 计算文件行数
        lineNums = len(open(fileName, 'r', encoding="utf-8").readlines())
        # print(u'文件行数: ' + str(lineNums))

        # 统计格式 格式<Key:Value> <属性:出现个数>
        i = 0
        table = {}
        source = open(fileName, mode="r", encoding="utf-8")
        result = open(resultName, mode="w", encoding="utf-8")

        while i < lineNums:
            line = source.readline()
            line = line.rstrip('\n')
            # print(line)

            words = line.split(" ")  # 空格分隔
            # print(str(words).encode('utf-8').decode('utf-8'))  # list显示中文

            # 字典插入与赋值
            for word in words:
                if word != "" and word in table:  # 如果存在次数加1
                    num = table[word]
                    table[word] = num + 1
                elif word != "":  # 否则初值为1
                    table[word] = 1
            i = i + 1

        # 键值从大到小排序 函数原型：sorted(dic,value,reverse)
        dic = sorted(table.items(), key=lambda asd: asd[1], reverse=True)
        for i in range(len(dic)):
            # print 'key=%s, value=%s' % (dic[i][0],dic[i][1])
            result.write("<" + dic[i][0] + ":" + str(dic[i][1]) + ">\n")
        return dic

    except Exception as e:
        print('Error:', e)
    finally:
        source.close()
        result.close()
        # print('CountKey END\n')


# 统计关键词及个数 并计算相似度
def MergeKeys(dic1, dic2):
    # 合并关键词 采用三个数组实现
    arrayKey = []
    for i in range(len(dic1)):
        arrayKey.append(dic1[i][0])  # 向数组中添加元素
    for i in range(len(dic2)):
        if dic2[i][0] not in arrayKey:
            # 合并
            arrayKey.append(dic2[i][0])
    else:
        print('')

    # test = str(arrayKey).encode('utf-8').decode('utf-8')  # 字符转换
    # print(test)

    # 计算词频 infobox可忽略TF-IDF
    arrayNum1 = [0] * len(arrayKey)
    arrayNum2 = [0] * len(arrayKey)

    # 赋值arrayNum1
    for i in range(len(dic1)):
        key = dic1[i][0]
        value = dic1[i][1]
        j = 0
        while j < len(arrayKey):
            if key == arrayKey[j]:
                arrayNum1[j] = value
                break
            else:
                j = j + 1

    # 赋值arrayNum2
    for i in range(len(dic2)):
        key = dic2[i][0]
        value = dic2[i][1]
        j = 0
        while j < len(arrayKey):
            if key == arrayKey[j]:
                arrayNum2[j] = value
                break
            else:
                j = j + 1

    print("专利文本空间向量模型：", arrayNum1)
    print("产品特征文本空间向量模型：", arrayNum2)
    # print(len(arrayNum1), len(arrayNum2), len(arrayKey))

    # 计算两个向量的点积
    x = 0
    i = 0
    while i < len(arrayKey):
        x = x + arrayNum1[i] * arrayNum2[i]
        i = i + 1
    # print(x)

    # 计算两个向量的模
    i = 0
    sq1 = 0
    while i < len(arrayKey):
        sq1 = sq1 + arrayNum1[i] * arrayNum1[i]  # pow(a,2)
        i = i + 1
    # print(sq1)

    i = 0
    sq2 = 0
    while i < len(arrayKey):
        sq2 = sq2 + arrayNum2[i] * arrayNum2[i]
        i = i + 1
    # print(sq2)

    result = float(x) / (math.sqrt(sq1) * math.sqrt(sq2))
    return result


# jieba分词,不去除停用词
def jiebaFuc(filePath, segWordDonePath):
    fileTrainRead = []
    with open(filePath, 'r', encoding='utf-8') as fileTrainRaw:
        for line in fileTrainRaw:  # 按行读取文件
            fileTrainRead.append(line)

    # jieba分词后保存在列表中
    fileTrainSeg = []
    for i in range(len(fileTrainRead)):
        fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11], cut_all=False)))])
        if i % 100 == 0:
            print(i)

    # 保存分词结果到文件中
    with open(segWordDonePath, 'w', encoding='utf-8') as fW:
        for i in range(len(fileTrainSeg)):
            fW.write(fileTrainSeg[i][0])
            fW.write('\n')


# jieba分词，去除停用词
def stripdata(filePath, fileSegWordDonePath):
    # jieba 默认启用了HMM（隐马尔科夫模型）进行中文分词
    # print("当前文件：",filePath)
    Rawdata = open(filePath, 'r+', encoding='utf-8')
    cutFile = Rawdata.read()
    seg_list = jieba.cut(cutFile, cut_all=True)  # 分词

    # seg_list = jieba.analyse.extract_tags(cutFile, topK=20)

    # 获取字典，去除停用词
    line = "/".join(seg_list)
    # print("分词结果：", line)
    word = stripword(line, fileSegWordDonePath)
    # 列出关键字
    # print("\n关键字：\n"+word)


# 停用词分析
def stripword(seg, fileSegWordDonePath):
    # 打开写入关键词的文件
    keyword = open(fileSegWordDonePath, 'w+', encoding='utf-8')
    # print("去停用词：\n")
    wordlist = []

    # 获取停用词表
    stop = open('Y:\\myPyCharmWorkStation\\graduation_project\\VSM_Word2Vec_model_package\\stopWordFile\\cn_stopwords.txt', 'r+', encoding='utf-8')
    stopword = stop.read().split("\n")
    # print("读取的停用词:",stopword)
    # 遍历分词表
    for key in seg.split('/'):
        # 去除停用词，去除单字，去除重复词
        # print("去除的停用词为：")
        if not (key.strip() in stopword) and (len(key.strip()) > 1) and not (key.strip() in wordlist):
            wordlist.append(key)
            # print("去除的停用词为：",key)
            keyword.write(key + "\n")

    # 停用词去除END
    stop.close()
    keyword.close()
    return '/'.join(wordlist)


# 分词函数调用函数
def Participle(claimsFile, productFile, claimsParticipleFile, productParticipleFile):
    claimsFilePath = claimsFile
    productFilePath = productFile
    claimsFileSegWordDonePath = claimsParticipleFile
    productFileSegWordDonePath = productParticipleFile

    # jiebaFuc(claimsFilePath,claimsFileSegWordDonePath)
    # jiebaFuc(productFilePath,productFileSegWordDonePath)
    # 分词调用，对权利要求说明和产品特征文本进行分词,同时去除停止词
    stripdata(claimsFilePath, claimsFileSegWordDonePath)
    stripdata(productFilePath, productFileSegWordDonePath)


# 使用Word2Vec增强VSM模型
def UseW2VForceVSM(tmpkeyDic):
    keyDic = tmpkeyDic
    # keyDic的结构为 list + 元组，这里是将元组转换为list
    # print(keyDic)
    for tup in keyDic:
        keyDic[keyDic.index(tup)] = list(tup)
    # print(keyDic)
    # 模型载入
    model = gensim.models.Word2Vec.load('Y:\\myPyCharmWorkStation\\graduation_project\\VSM_Word2Vec_model_package\\wiki.zh.text.model')
    # print("-----------------------------------模型增强开始-------------------------------")
    for i in range(len(keyDic)):
        # print("-----------------------------------单词增强-------------------------------")
        word = keyDic[i][0]
        if word in model:
            result = model.most_similar(word)
            # print(u"\n与'%s'最相似的词为： " % word)
            # print(result)
            TList = []
            for ii in range(len(result)):
                if result[ii][1] > 0.5:
                    TList.append(result[ii])
            # print("相似度列表：",TList)
            Wj = keyDic[i][1]
            for j in range(len(TList)):
                keyDic[i][1] = keyDic[i][1] + Wj * TList[j][1]
        else:
            pass
            # print(u"单词'%s'不在字典中！" % word)
    # print("-----------------------------------模型增强结束-------------------------------")
    # print(keyDic)
    return keyDic


def interface(textUUIDParam):  # 传入关键字（UUID）以保证输出文件的唯一性
    textUUID = textUUIDParam + '_'
    inputPath = 'Y:\\myPyCharmWorkStation\\graduation_project\\VSM_Word2Vec_model_package\\input\\'
    outputPath = 'Y:\\myPyCharmWorkStation\\graduation_project\\VSM_Word2Vec_model_package\\output\\'
    # 起始时间
    start_time = datetime.datetime.now()
    print("程序起始时间：", start_time)

    # 文本参数设置
    claimsFile = inputPath + textUUID + "claims_init.txt"
    # print(claimsFile)
    productFile = inputPath + textUUID + "product_init.txt"
    claimsParticipleFileName = outputPath + textUUID + "claims_participle.txt"
    productParticipleFileName = outputPath + textUUID + "product_participle.txt"
    claimsParticipleResultFileName = outputPath + textUUID + "Result_Key_Claims.txt"
    productParticipleResultFileName = outputPath + textUUID + "Result_Key_Product.txt"

    # 文章分词
    print("开始文本分词！请等待...")
    Participle(claimsFile, productFile, claimsParticipleFileName, productParticipleFileName)
    print("文本分词已完成！")

    # 计算专利权利要求中的关键词及个数
    print("开始统计文本中的关键词！请等待...")
    claimsDic = CountKey(claimsParticipleFileName, claimsParticipleResultFileName)
    print("关键词统计已完成！")

    # 计算产品特征中的关键词及个数
    print("开始计算关键词权重！请等待...")
    productDic = CountKey(productParticipleFileName, productParticipleResultFileName)
    print("关键词权重已计算完毕！")

    # VSM模型增强
    print("正在查阅同义词词典！请等待...")
    claimsDic = UseW2VForceVSM(claimsDic)
    productDic = UseW2VForceVSM(productDic)
    print("词典已经查阅完毕！")

    # 合并两篇文章的关键词及相似度（余弦相似度）计算
    print("开始计算文本相似度！请等待...")
    textSimilarityResult = MergeKeys(claimsDic, productDic)
    print("文本相似度(专利侵权概率)：", textSimilarityResult)
    if textSimilarityResult > 0.5:
        textSimilarity = 'YES'
        print("经判定该产品构成了专利侵权。")
    else:
        textSimilarity = 'NO'
        print("经判定该产品并未构成专利侵权。")

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
    outputFileHeader = ['textSimilarityResult', 'textSimilarity', 'start_time', 'stop_time', 'total_time']
    w = csv.DictWriter(f, outputFileHeader)
    w.writeheader()
    csv_dict = edict()
    csv_dict.textSimilarityResult = str(textSimilarityResult)
    csv_dict.textSimilarity = str(textSimilarity)
    csv_dict.start_time = str(start_time)
    csv_dict.stop_time = str(stop_time)
    csv_dict.total_time = str(total_time)
    w.writerow(csv_dict)
    f.close()


if __name__ == '__main__':
    # 模型封装
    parser = argparse.ArgumentParser(description='These are the parameters of the training model')
    parser.add_argument('--textUUIDParam', type=str, default=None, required=True, help='File unique identification')

    args = parser.parse_args()  # parse_args()从指定的选项中返回一些数据
    interface(textUUIDParam=args.textUUIDParam)
