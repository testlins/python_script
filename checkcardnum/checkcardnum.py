#coding=gbk
#���֤У��
#����λ��У��ͳ���������У��
#���������ж��Ƿ�Ϊ�Ϸ�����
#���ж������Ƿ���startdate��Ŀǰʱ��֮��
import os
import time
import re
import checkdate
def cardcheck(cardnum):
    #���֤���һλ��������
    values =['1','0','X','9','8','7','6','5','4','3','2']
    #���֤�ӵ�һλ��ʮ��λ����
    multiplier =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2 ]
    if len(cardnum)==18 and cardnum[0:17].isdigit() and cardnum[-1] in values:
        birdate = cardnum[6:14]
        #����checkdate������ںϷ���
        if checkdate.checkdate(birdate):
            #���һλУ�������:
            """
            �����֤�����ǰ17λ���ֱ���Բ�ͬ��ϵ�����ӵ�һλ����ʮ��λ��ϵ���ֱ�Ϊ��7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2
            ����17λ���ֺ�ϵ����˵Ľ����ӡ�
            �üӳ����ͳ���11���õ�������
            �����Ľ��ֻ����Ϊ0 1 2 3 4 5 6 7 8 9 10��11�֣��ֱ��Ӧ�����һλ���֤�ĺ���Ϊ1 0 X 9 8 7 6 5 4 3 2��
            """            
            temp = zip(cardnum[0:17],multiplier[0:17])
            multip = map(lambda x:int(x[0]*x[1]),temp)
            sumnub = sum(multip)
            if values[sumnub%11]==cardnum[-1]:
                return True
            else:
                return False               
        else:
            return False
    else:
        return False

            
        
        

if __name__ == '__main__':        
#cardcheck('456785198809192345')
    cardcheck('440524188001010014')
        
        