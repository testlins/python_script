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
        self.last_numrule = ['1','0','X','9','8','7','6','5','4','3','2']
        self.multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        self.area = area
        self.birdate = birdate
        self.sex = sex
    
    def cre_areaid(self):
        """计算地区编码或随机获取"""
        area = self.area
        connect = id_db.id_db()
        if area:
            print connect.select_areaid(area)
            return str(connect.select_areaid(area))
        else:
             print connect.select_allareaid()[random.randint(1,(len(connect.select_allareaid())-1))]
             return str(connect.select_allareaid()[random.randint(1,(len(connect.select_allareaid())-1))])
    
    def cre_bridate(self):
        """指定生日或随机获取"""
        bridate = self.birdate
        if bridate:
            print bridate
            return str(bridate)
        else:
            nowdate = datetime.date.today()
            startdate = datetime.date(1900,1,1)
            sepdate = (nowdate-startdate).days
            randomdate = startdate + datetime.timedelta(days=random.randint(0,sepdate))
            #bridate = str(randomdate.year) + str(randomdate.month).zfill(2) + str(randomdate.day).zfill(2)
            bridate = datetime.datetime.strftime(randomdate,'%Y%m%d')
            #print bridate
            return bridate
            
            
    def cre_squnum(self):
        """根据性别得到序列号"""
        sex = self.sex
        squnum = str(random.randint(00,99)).zfill(2)
        if sex == '男':
            #print squnum + str(random.randrange(1,11,2))
            return squnum + str(random.randrange(1,11,2))
        elif sex == '女':
            return squnum + str(random.randrange(0,10,2))            
        else:
            return squnum + str(random.randint(0,9))
    
    def cre_idnum(self):
        """计算最后一位，得到身份证号"""
        multiplier = self.multiplier
        last_numrule = self.last_numrule
        #subid_num = creid_rule.cre_areaid() + creid_rule.cre_bridate() + creid_rule.cre_squnum()
        subid_num = self.cre_areaid() + self.cre_bridate() + self.cre_squnum()
        temp = zip(subid_num[0:17],multiplier[0:17])
        mult_id = map(lambda x:int(x[0])*x[1],temp)
        sum_id = sum(mult_id)
        last_num = last_numrule[sum_id%11]
        id_num = subid_num + last_num
        #print last_num,id_num
        return id_num
        
            
if __name__ == '__main__':
    a = creid_rule('北京市')
#    a = creid_rule()
    a.cre_areaid()
    a.cre_squnum()
    a.cre_bridate()
    a.cre_idnum()

        