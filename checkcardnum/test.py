#coding=utf-8
#创建sqlite数据库：id.db，用做身份证相关信息存贮
#
import os
path = r"C:\Users\casking_lxs\Desktop\20130329\sql"
files = []
for file in os.listdir(path):
    if file[-4:]=='.sql':
        fileName = os.path.join(path, file)  
        filetime = os.stat(fileName).st_mtime
        files.append((filetime,fileName))
        print path+os.sep+file
        print fileName
files.sort()
for filex in files:
    print filex[1]
    
