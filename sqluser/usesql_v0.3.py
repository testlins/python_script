# -*- coding: gbk -*-
#脚本功能，连接指定数据库；
#扫描同文件夹下的.sql文件,读入并执行。
#增加异常处理，日志记录功能
#author：linxs
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
#取sql中的文件名，循环打开文件 执行
#此版本values值有两行，会报错hy000
sqldir = os.listdir(os.getcwd()+os.sep+"sql")
print sqldir
for file in sqldir:
    if file[-4:]=='.sql':
        fileopen = open(os.getcwd()+os.sep+"sql"+os.sep+file, "r+")
        sqldo = fileopen.read()
        try:
            cursor1.execute(sqldo)
            cursor1.commit()
            mylog.info(file+' 执行成功')
            fileopen.close()
        except pyodbc.Error, dberror:
            mylog.error(file+' 执行失败，请检查语句')
            mylog.error(dberror)
cursor1.close()




