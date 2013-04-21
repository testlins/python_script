#coding=utf-8
#创建sqlite数据库：id.db，用做身份证相关信息存贮
#
import sqlite3
iddb = sqlite3.connect("id.db")
iddb.text_factory = str
cu = iddb.cursor()
 
def creattable():
    cu.execute('create table id_main(id integer primary key UNIQUE,area varchar(30))')

def insertdb():
    cu.execute('insert into id_main values(3,"第三")')
    cu.execute('insert into id_main values(1,"第一")')
    iddb.commit()

def selectdb():
    cu.execute('select * from id_main where id="130730"')
    qs =cu.fetchall()
    print qs

def sqlfile():
    opensqlfile = open('iddata.txt','rb')
#    print sqldo
    for line in opensqlfile:
#        print line
        cu.execute(line)
#        cu.execute(line)
    iddb.commit()
    

if __name__ == '__main__':
    creattable()
#    insertdb()
#    selectdb()
    sqlfile()
    #selectdb()