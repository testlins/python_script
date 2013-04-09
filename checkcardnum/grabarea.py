#coding=gbk
#抓取身份证区域信息脚本
#
import urllib
import re
def grabarea():
    data = urllib.urlopen("http://www.stats.gov.cn/tjbz/xzqhdm/t20130118_402867249.htm").read()
#    regetcode = re.compile(r'lang=EN-US>.+<o:p></o:p></SPAN></P></TD>')
    regetid = r'lang=EN-US>.+<o:p></o:p></SPAN></P></TD>'
    regetarea = 'mso-bidi-font-family: Tahoma">.+<SPAN lang=EN-US><o:p></o:p></SPAN></SPAN></P></TD></TR>'
    idnum = re.findall(regetid,data)
    areainfo = re.findall(regetarea,data)
#    print areainfo
    file1 = open(r'2.txt','w+')
#    for middid in idnum:
#        reid = re.search(r'\d+',middid)
#        id = reid.group()
#        print id
    for middarea in areainfo:
        area1 = re.search('[\x80-\xff]+',middarea)
        area = area1.group()
        print area
        file1.write('insert into id_main (id) values("%s")'%(area))
        file1.write('\n')
    file1.close()

if __name__ == '__main__':
    grabarea()
    
    
    
