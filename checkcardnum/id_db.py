#coding=utf-8
#定义数据库相关操作

import sqlite3
import ConfigParser

class id_db(object):
    """
    定义id对数据库的部分操作
    """
    def __init__(self):
        config = ConfigParser.ConfigParser()
        with open('id_num.config','r+') as cfgfile:
            config.readfp(cfgfile)
            id_db = config.get('id_db','dbname')
        self.connid_db = sqlite3.connect(id_db)
        self.cursorid = self.connid_db.cursor()
    
    def select_area(self,num):
        cursorid = self.cursorid
        cursorid.execute('select area from id_main where id="%d"'%num)
        qs =cursorid.fetchone()
        print qs
    
    def select_num(self,area):
        pass


        


id_db =id_db()
id_db.select_area(1)

    
        
