#coding=gbk
#身份证校验
#先做位数校验和出生年月日校验
#先用正则判断是否为合法日期
#在判断日期是否在startdate和目前时刻之间
#增加年龄计算
import os
import time
import re
#import checkdate
import calc_age
def cardcheck(cardnum):
    #身份证最后一位包含数字
    values =['1','0','X','9','8','7','6','5','4','3','2']
    #身份证从第一位到十七位乘数
    multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    if len(cardnum)==18 and cardnum[0:17].isdigit() and cardnum[-1] in values:
        birdate = cardnum[6:14]
        #调用checkdate检查日期合法性
        if calc_age.calc_age(birdate):
            #最后一位校验码规则:
            """
            将身份证号码分别乘以不同的系数。从第1位到第17位的系数分别为：7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 1
            将这17位数字和系数相乘的结果相加。
            用加出来和除以11，得到余数。
            余数的结果只可能为0 1 2 3 4 5 6 7 8 9 10这11种，分别对应的最后一位身份证的号码为1 0 X 9 8 7 6 5 4 3 2。
            """    
                    
                    
            temp = zip(cardnum[0:17],multiplier[0:17])
            multip = map(lambda x:int(x[0])*x[1],temp)
            sumnub = sum(multip)

            if values[sumnub%11]==cardnum[-1]:
                print "CardId is true"
                print "The people age is %s"%calc_age.calc_age(birdate)
                return True
            else:
                return False               
        else:
            return False
    else:
        return False

            
        
        

if __name__ == '__main__':        
    cardcheck('459671198311018096')

        
        