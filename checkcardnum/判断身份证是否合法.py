#coding=gbk
#身份证校验
#先做位数校验和出生年月日校验
#先用正则判断是否为合法日期
#在判断日期是否在startdate和目前时刻之间
import os
import time
import re
import checkdate
def cardcheck():
    cardnum = '430724198809192111'
    values =[1,0,'X',9,8,7,6,5,4,3,2]
    multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2 ]
    if len(cardnum)==18 and cardnum[0:17].isdigit() and cardnum[-1] in values:
        birdate = cardnum[6:14]
        if checkdate.checkdate(birdate):
            temp = zip(cardnum[0:17],multiplier[0:17])
            multip = map(lambda x:int(x[0]*x[1]),temp)
            sumnub = sum(multip)
            if values[sumnub%11]==cardnum[-1]:
                print "good"
            else:
                print 'no'                
        else:
            cardcheck()
    else:
        print 'nonono'

            
        
        

        
#cardcheck('456785198809192345')
cardcheck()
        
        