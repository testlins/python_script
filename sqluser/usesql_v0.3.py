# -*- coding:gbk -*-
#脚本功能，连接指定数据库；
#扫描同文件夹下的.sql文件,读入并执行。
#增加异常处理，日志记录功能
#按时间升序 顺序执行
#author：linxs
#version v0.3
# -*- coding:gbk -*-
import pyodbc
import os
import ConfigParser
import mylog
mylog = mylog.initlog()
config = ConfigParser.ConfigParser()
#获取配置文件详细信息
with open("usesql.config", "r+") as  cfgfile:
    config.readfp(cfgfile)
    linkdata = config.get("info", "linkdata")
try:
    consql = pyodbc.connect(linkdata)
    mylog.info("数据库连接成功")
    cursor1 = consql.cursor()
    mylog.info("游标建立成功")    
except pyodbc.Error, dberror:
    mylog.error("数据库连接失败")
    mylog.error(dberror)
#此版本values值有两行，会报错hy000
path = os.getcwd()+os.sep+"sql"
sqldir = os.listdir(os.getcwd()+os.sep+"sql")

#取出sql文件最后修改时间，并排序

files = []
#for file in sqldir:
#    if file[-4:]=='.sql':
#        fileName = os.path.join(path,file)  
#        filetime = os.stat(fileName).st_mtime
 #       files.append((filetime,fileName))

#网上的例子是函式编程 学习下
files = [(os.path.getmtime(path+os.sep+file),os.path.join(path,file))for file in sqldir if file[-4:]=='.sql']
files.sort()
#循环执行sql文件
for filex in files:
    fileopen = open(filex[1], "r+")
    sqldo = fileopen.read()

#sqldo = [open(filex[1],"r+").read() for filex in files]
#print sqldo    
    try:
        cursor1.execute(sqldo)
        cursor1.commit()
        mylog.info((os.path.split(filex[1]))[1]+' 执行成功')
        fileopen.close()
    except pyodbc.Error, dberror:
        mylog.error((os.path.split(filex[1]))[1]+' 执行失败，请检查语句')
        mylog.error(dberror)
cursor1.close()




