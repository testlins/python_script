#coding=gbk
#创建随机身份证号
#保证身份证合法：
#年龄合法、校验位正确
#按年龄大小生成
import random
import datetime
import time
import sqlite3
import calc_age
def creatcardnum(flag,age):
    #获取区域id随机数
    
    iddb = sqlite3.connect("id.db")
    iddb.text_factory = str
    cu = iddb.cursor()
    listid=[]
    cu.execute('SELECT id FROM id_main')
    #为啥可以for循环，还不懂
    for id in cu:
        listid.append(id[0])
#    listlen = len(listid)
    #获取随机数注意列表是从0开始，列表id比长度少1
    #不然会报错IndexError: list index out of range
    startnum = str(listid[random.randint(0,(len(listid)-1))])
    #身份证 序列数
    squnum = str(random.randint(001,999)).zfill(3)
    nowdate = datetime.date.today()
    startdate = datetime.date(1900, 1, 1)
    midddate =calc_age.calc_date(age)
    #当前时间和现在的间隔天数
    if flag=='>':
        #大于age，则出生日期小于输入年龄
        sepdate = (midddate - startdate).days
        randomdate = random.randint(0,sepdate)
        xdate = startdate + datetime.timedelta(days = randomdate)
        #字符串随机时间
        finnaldate = str(xdate.year) + str(xdate.month).zfill(2) +str(xdate.day).zfill(2)
        cardlist = startnum + finnaldate + squnum
        
    elif flag=='<':
        #小于age，则出生日期大于输入年龄
        sepdatenow = (nowdate - startdate).days
        sepdatemidd = (midddate - startdate).days
        randomdate = random.randint(sepdatemidd,sepdatenow)
        xdate = startdate + datetime.timedelta(days = randomdate)
        #字符串随机时间
        finnaldate = str(xdate.year) + str(xdate.month).zfill(2) +str(xdate.day).zfill(2)
        cardlist = startnum + finnaldate + squnum
        
    else:
        print "flag error"        
        
    #根据规则求身份证校验位
    values =['1','0','X','9','8','7','6','5','4','3','2']
    multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    temp = zip(cardlist[0:17],multiplier[0:17])
    multip = map(lambda x:int(x[0])*x[1],temp)
    
    finalnum = values[sum(multip)%11]
    
    cardnum = cardlist+finalnum
    print cardnum    

if __name__ == '__main__':
    print "input age number and '>' or '<'"
    while 1:
        
        creatcardnum('11',10)
    
