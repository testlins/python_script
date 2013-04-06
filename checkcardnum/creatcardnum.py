#coding=gbk
#创建随机身份证号
#保证身份证合法：
#年龄合法、校验位正确
#
import random
import datetime
import time
def creatcardnum():
    #身份证 序列数
    squnum = str(random.randint(001,999)).zfill(3)
    nowdate = datetime.date.today()
    startnum = str(random.randint(100000,999999))
    startdate = datetime.date(1900, 1, 1)
    #当前时间和现在的间隔天数
    sepdate = (nowdate - startdate).days
    randomdate = random.randint(0,sepdate)
    xdate = startdate + datetime.timedelta(days = randomdate)
    #字符串随机时间
    finnaldate = str(xdate.year) + str(xdate.month).zfill(2) +str(xdate.day).zfill(2)
    cardlist = startnum + finnaldate + squnum
    #根据规则求身份证校验位
    values =['1','0','X','9','8','7','6','5','4','3','2']
    multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    temp = zip(cardlist[0:17],multiplier[0:17])
    multip = map(lambda x:int(x[0])*x[1],temp)
    
    finalnum = values[sum(multip)%11]
    
    cardnum = cardlist+finalnum
    print cardnum    

if __name__ == '__main__':
    while 1:
        creatcardnum()
    
