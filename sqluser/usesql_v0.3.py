# -*- coding: gbk -*-
#�ű����ܣ�����ָ�����ݿ⣻
#ɨ��ͬ�ļ����µ�.sql�ļ�,���벢ִ�С�
#�����쳣������־��¼����
#author��linxs
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
#ȡsql�е��ļ�����ѭ�����ļ� ִ��
#�˰汾valuesֵ�����У��ᱨ��hy000
sqldir = os.listdir(os.getcwd()+os.sep+"sql")
print sqldir
for file in sqldir:
    if file[-4:]=='.sql':
        fileopen = open(os.getcwd()+os.sep+"sql"+os.sep+file, "r+")
        sqldo = fileopen.read()
        try:
            cursor1.execute(sqldo)
            cursor1.commit()
            mylog.info(file+' ִ�гɹ�')
            fileopen.close()
        except pyodbc.Error, dberror:
            mylog.error(file+' ִ��ʧ�ܣ��������')
            mylog.error(dberror)
cursor1.close()




