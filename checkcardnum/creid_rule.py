#coding=utf-8
#创建合法身份证相关规则
#
import id_db
import datetime
import random

class creid_rule(object):
    """
    随机创建省份证，和按条件生成省份证规则
    """
    def __init__(self,area='',birdate='',sex=''):
        self.last_num = ['1','0','X','9','8','7','6','5','4','3','2']
        self.multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        self.area = area
        self.birdate = birdate
        self.sex = sex
    
    def cre_areaid(self):
        area = self.area
        connect = id_db.id_db()
        if area:
            print connect.select_areaid(area)
            return str(connect.select_areaid(area))
        else:
             print connect.select_allareaid()[random.randint(1,(len(connect.select_allareaid())-1))]
             return str(connect.select_allareaid()[random.randint(1,(len(connect.select_allareaid())-1))])
    
    def cre_bridate(self):
        bridate = self.birdate
        if bridate:
            print bridate
            return str(bridate)
        else:
            pass
            
    def cre_squnum(self):
        sex = self.sex
        squnum = str(random.randint(00,99)).zfill(2)
        if sex == '男':
            #print squnum + str(random.randrange(1,11,2))
            return squnum + str(random.randrange(1,11,2))
        elif sex == '女':
            return squnum + str(random.randrange(0,10,2))            
        else:
            return squnum + str(random.randint(0,9))
    
    def cre_lastnum(self):
        pass
        
            
if __name__ == '__main__':
    a = creid_rule('北京市',111111)
#    a = creid_rule()
    a.cre_areaid()
    a.cre_squnum()
    a.cre_bridate()

        