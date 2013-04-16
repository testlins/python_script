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
        self.connid_db.text_factory = str
        self.cursorid = self.connid_db.cursor()
    
    def select_area(self,id):
        cursorid = self.cursorid
        cursorid.execute('select area from id_main where id="%s"'%id)
        for area in cursorid:
            #print area[0].encode('GB18030')
            #print area[0]
            return area[0]
    
    def select_areaid(self,area):
        cursorid = self.cursorid
        cursorid.execute('select id from id_main where area="%s"'%area)
        for areaid in cursorid:
            #print areaid[0]
            return areaid[0]
                
        
    
    def select_allareaid(self):
        listid = []
        cursorid = self.cursorid
        cursorid.execute('select id from id_main')
        for id in cursorid:
            listid.append(id[0])
        #print listid[0]
        return listid
    
    


        

if __name__ == '__main__':
    id_db =id_db()
    id_db.select_area(110106)
    id_db.select_allareaid()
    print id_db.select_areaid('北京市')
        
