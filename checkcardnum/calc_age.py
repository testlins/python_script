#coding=gbk
#年龄计算出生日期
#出生日期计算年龄
import datetime
import checkdate

def calc_date(age):
    if isinstance(age,int):
        nowtime = datetime.date.today()
        middtime = datetime.date(nowtime.year-age,nowtime.month,nowtime.day)
        
#        print nowtime,middtime
        return middtime
    else:
        print "age error"
        
def calc_age(birth):
    if  birth.isdigit() and len(birth)==8 and checkdate.checkdate(birth):
        nowtime = datetime.date.today().year
        birthyear = datetime.datetime.strptime(birth,'%Y%m%d').year
#        print nowtime - birthyear
        return nowtime - birthyear
        
                
    else:
        print "date error"
if __name__ == '__main__':
    calc_date(8)
    calc_age('19880202')
