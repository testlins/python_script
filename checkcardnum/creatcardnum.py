#coding=gbk
#����������֤��
#��֤���֤�Ϸ���
#����Ϸ���У��λ��ȷ
#
import random
import datetime
import time
import sqlite3
def creatcardnum():
    #��ȡ����id�����
    iddb = sqlite3.connect("id.db")
    iddb.text_factory = str
    cu = iddb.cursor()
    listid=[]
    cu.execute('SELECT id FROM id_main')
    #Ϊɶ����forѭ����������
    for id in cu:
        listid.append(id[0])
#    listlen = len(listid)
    #��ȡ�����ע���б��Ǵ�0��ʼ���б�id�ȳ�����1
    #��Ȼ�ᱨ��IndexError: list index out of range
    startnum = str(listid[random.randint(0,(len(listid)-1))])
    #���֤ ������
    squnum = str(random.randint(001,999)).zfill(3)
    nowdate = datetime.date.today()
    startdate = datetime.date(1900, 1, 1)
    #��ǰʱ������ڵļ������
    sepdate = (nowdate - startdate).days
    randomdate = random.randint(0,sepdate)
    xdate = startdate + datetime.timedelta(days = randomdate)
    #�ַ������ʱ��
    finnaldate = str(xdate.year) + str(xdate.month).zfill(2) +str(xdate.day).zfill(2)
    cardlist = startnum + finnaldate + squnum
    #���ݹ��������֤У��λ
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
    
