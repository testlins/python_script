#coding=utf-8
#身份证通用验证规则
#
#
import os
import random
import datetime
import re
import id_db
import mylog

class id_rule(object):
    """
    身份证通用验证规则

    """
    def __init__(self,id_num):
        """
        初始化idnum
        """
        self.last_num = ['1','0','X','9','8','7','6','5','4','3','2']
        self.multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        if id_num[0:17].isdigit() and len(id_num)==18 and id_num[-1] in self.last_num:
            self.id_num = id_num
            self.id_area = id_num[0:6]
            self.id_date = id_num[6:14]
            self.id_sex = id_num[16]
        else:
            print 'id_num error'
            pass
    
    def id_isarea(self):
        """
        判断是否为合法地区，并返回地区信息
        """
        id_area = self.id_area
        connectdb = id_db.id_db()
        if connectdb.select_area(id_area):
            return connectdb.select_area(id_area)
        else:
            print 'error area'
            return False
            
        
    
    def id_isdate(self):
        """
        判断是否为日期，并返回日期
        """
        date = self.id_date
        startdate = 19000101
        nowdate = datetime.date.strftime(datetime.date.today(),'%Y%m%d')
        if date >= startdate and date <= nowdate :
            try:
                datetime.datetime.strptime(date,'%Y%m%d')
                return date
            except:
                return False
        else:
            return False

    
    def calc_age(self):
        """
        计算年龄
        """
        date = self.id_date
        nowyear = datetime.date.today().year
        brithyear = datetime.datetime.strptime(date,'%Y%m%d').year
        age = nowyear - brithyear
        print age
        return age
    
    def id_rule(self):
        """
        身份证校验位规则
        """
        multiplier = self.multiplier
        last_num = self.last_num
        id_num = self.id_num
        temp = zip(id_num[0:17],multiplier[0:17])
        mult_id = map(lambda x:int(x[0])*x[1],temp)
        sum_id = sum(mult_id)
        if last_num[sum_id%11]==id_num[-1]:
            return True
        else:
            return False
    
    def id_numsex(self):
        """
        判断性别
        """
        id_sex = int(self.id_sex)
        if id_sex%2 == 0:
            return '女'
        else:
            return '男'
        
        
        
if __name__ == '__main__':    
    a = id_rule('430724198809192111')
    a.calc_age()
    a.id_isdate()
    a.id_rule()
    a.id_isarea()
    a.id_numsex()
