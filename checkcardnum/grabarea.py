#coding=gbk
#ץȡ���֤������Ϣ�ű�
#
import urllib
import re
def grabarea():
    """
    �˺�����ͳ�ƾ���վ��ȡ���ݣ�����ŵ��ļ���
    """
    data = urllib.urlopen("http://www.stats.gov.cn/tjbz/xzqhdm/t20130118_402867249.htm").read()
    regetid = r'lang=EN-US>.+<o:p></o:p></SPAN></P></TD>'
    regetarea = 'mso-bidi-font-family: Tahoma">.+<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></P></TD></TR>'
    #findall�����������б��´���compile����ٶ�
    #��Լid����
    idnum = re.findall(regetid,data)
    #��Լ�ĵ�������
    areainfo = re.findall(regetarea,data)
    #id���������ݿ��б�
    listid = []
    listarea = []
    
    for middid in idnum:
        reid = re.search(r'\d+',middid)
        id = reid.group()
        listid.append(id)
    for middarea in areainfo:
        area1 = re.search(r'[\x80-\xff]+',middarea)
        area = area1.group()
        listarea.append(area)
    file1 = open(r'iddata.txt','w+')
    #id���������ļ���
    for i in range(len(listid)):
        file1.write('insert into id_main (id,area) values("%s","%s")'%(listid[i],listarea[i]))
        file1.write('\n')
    file1.close()

if __name__ == '__main__':
    grabarea()
    
    
    
