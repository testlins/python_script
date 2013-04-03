#coding=gbk
import os
import time
import re
import string
def checkdate(datenum):
#    datenum = raw_input("please input you birdate: ")
    if len(datenum)==8 and datenum.isdigit():
        startdate = 19000101
        #获取当天日期
        enddate = time.strftime('%Y%m%d',time.localtime(time.time()))
        if datenum>=startdate and datenum<=enddate:
#            timere = "^((0([1-9]{1}))|(1[0|1|2]))/(([0-2]([0-9]{1}))|(3[0|1]))/(\d{2}|\d{4})$"
            try:
                #判断日期合法性
                time.strptime(datenum, "%Y%m%d")
                return True
#            if re.match(timere, "10/24/2011") != None:
            except:                
                return False
        else:
            return False
    else:
        return False

        
if __name__ == '__main__':
    checkdate('20000229')
        
        