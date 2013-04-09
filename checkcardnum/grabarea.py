#coding=gbk
#抓取身份证区域信息脚本
#
import urllib
import re
def grabarea():
    """
    此函数从统计局网站获取数据，并存放到文件中
    """
    data = urllib.urlopen("http://www.stats.gov.cn/tjbz/xzqhdm/t20130118_402867249.htm").read()
    regetid = r'lang=EN-US>.+<o:p></o:p></SPAN></P></TD>'
    regetarea = 'mso-bidi-font-family: Tahoma">.+<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></P></TD></TR>'
    #findall返回类型是列表，下次用compile提高速度
    #粗约id数据
    idnum = re.findall(regetid,data)
    #粗约的地区数据
    areainfo = re.findall(regetarea,data)
    #id、地区数据空列表
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
    #id、区域存放文件中
    for i in range(len(listid)):
        file1.write('insert into id_main (id,area) values("%s","%s")'%(listid[i],listarea[i]))
        file1.write('\n')
    file1.close()

if __name__ == '__main__':
    grabarea()
    
    
    
