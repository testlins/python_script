#coding=utf-8
import sqlite3


class vemdb(object):
    """数据库操作
    没有容错机制"""
    def __init__(self):
        self.conn_vemdb = sqlite3.connect('db/vem.db')
        self.conn_vemdb.text_factory = str
        #self.conn_vemdb.row_factory   = dict_factory
        self.cursor_vemdb =self.conn_vemdb.cursor()
        
    def select_price(self,Id):
        cursor_vemdb = self.cursor_vemdb
        cursor_vemdb.execute('select price from Commodity where Id="%d"'%Id)
        price = cursor_vemdb.fetchone()
        #cursor_vemdb.close()
        return  price[0]
        #for price in cursor_vemdb:
        #   return price[0]
    
    def select_info(self):
        info = []
        cursor_vemdb = self.cursor_vemdb
        cursor_vemdb.execute('select Id,price,Name from Commodity')
        for Id,price,Name in cursor_vemdb:
            info.append((Id,price,Name))

        return info

    


    def select_subinventory(self,Id):
        cursor_vemdb = self.cursor_vemdb
        cursor_vemdb.execute('select subinventory from subinventory where Id="%d"'%Id)
        subinventory = cursor_vemdb.fetchone()
        return subinventory[0]

    
    def select_submoney(self):
        SubMoney = {}
        cursor_vemdb = self.cursor_vemdb
        cursor_vemdb.execute('select MoneyID,MoneyNum from SubMoney')
        #rs = cursor_vemdb.fetchall()
        for MoneyID,MoneyNum in cursor_vemdb:
            SubMoney[MoneyID]=MoneyNum
        #cursor_vemdb.close()
        return SubMoney

    def update_submoney(self,MoneyID,MoneyNum):
        cursor_vemdb = self.cursor_vemdb
        cursor_vemdb.execute('update SubMoney set MoneyNum="%d" where MoneyID="%d"'%(MoneyNum,MoneyID))
        #cursor_vemdb.commit()
               
    def update_subinventory(self,Id,subinventory):
        cursor_vemdb = self.cursor_vemdb
        cursor_vemdb.execute('update subinventory set subinventory="%d" where Id="%d"'%(subinventory,Id))   


if __name__ == '__main__':
    x =vemdb()
    #x.select_price(3)
    x.select_submoney()
    x.select_info()
    #x.update_submoney(1,9)