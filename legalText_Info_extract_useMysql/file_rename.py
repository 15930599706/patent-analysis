import os
import re
# path = 'D:\\毕设\\专利法律文件\\普通发明\\'
# path = 'D:\\毕设\\专利法律文件\\实用新型专利\\'
path = 'D:\\毕设\\专利法律文件\\外观专利\\'
rootdir=os.path.join(path)

for (dirpath,dirnames,filenames) in os.walk(rootdir):
    for filename in filenames:
        print(filename)
        try:
            os.rename(path+filename,path+re.sub(r"-?[1-9]\d*-","",filename))
        except:
            continue

