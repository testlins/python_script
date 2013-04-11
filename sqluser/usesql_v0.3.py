# -*- coding:gbk -*-
#�ű����ܣ�����ָ�����ݿ⣻
#ɨ��ͬ�ļ����µ�.sql�ļ�,���벢ִ�С�
#�����쳣������־��¼����
#��ʱ������ ˳��ִ��
#author��linxs
#version v0.3
# -*- coding:gbk -*-
import pyodbc
import os
import ConfigParser
import mylog
mylog = mylog.initlog()
config = ConfigParser.ConfigParser()
#��ȡ�����ļ���ϸ��Ϣ
with open("usesql.config", "r+") as  cfgfile:
    config.readfp(cfgfile)
    linkdata = config.get("info", "linkdata")
try:
    consql = pyodbc.connect(linkdata)
    mylog.info("���ݿ����ӳɹ�")
    cursor1 = consql.cursor()
    mylog.info("�α꽨���ɹ�")    
except pyodbc.Error, dberror:
    mylog.error("���ݿ�����ʧ��")
    mylog.error(dberror)
#�˰汾valuesֵ�����У��ᱨ��hy000
path = os.getcwd()+os.sep+"sql"
sqldir = os.listdir(os.getcwd()+os.sep+"sql")

#ȡ��sql�ļ�����޸�ʱ�䣬������

files = []
#for file in sqldir:
#    if file[-4:]=='.sql':
#        fileName = os.path.join(path,file)  
#        filetime = os.stat(fileName).st_mtime
 #       files.append((filetime,fileName))

#���ϵ������Ǻ�ʽ��� ѧϰ��
files = [(os.path.getmtime(path+os.sep+file),os.path.join(path,file))for file in sqldir if file[-4:]=='.sql']
files.sort()
#ѭ��ִ��sql�ļ�
for filex in files:
    fileopen = open(filex[1], "r+")
    sqldo = fileopen.read()

#sqldo = [open(filex[1],"r+").read() for filex in files]
#print sqldo    
    try:
        cursor1.execute(sqldo)
        cursor1.commit()
        mylog.info((os.path.split(filex[1]))[1]+' ִ�гɹ�')
        fileopen.close()
    except pyodbc.Error, dberror:
        mylog.error((os.path.split(filex[1]))[1]+' ִ��ʧ�ܣ��������')
        mylog.error(dberror)
cursor1.close()




