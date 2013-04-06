#coding=gbk
#抓取身份证区域信息脚本
#
import urllib
import re
def grabarea():
    data = urllib.urlopen("http://www.stats.gov.cn/tjbz/xzqhdm/t20130118_402867249.htm").read()
#    regetcode = re.compile(r'lang=EN-US>.+<o:p></o:p></SPAN></P></TD>')
    regetcode = r'lang=EN-US>.+<o:p></o:p></SPAN></P></TD>'
    re1 = re.findall(regetcode,data)
#    re2 = re.findall(r'\d+',re1)
    file1 = open(r'2.txt','w+')
    for i in re1:
        re2 = re.search(r'\d+',i)
        re3 = re2.group()
        print i
        print re3
        file1.write(str(re3))
#        file1.write(str(i))
        file1.write('\r\n')
    file1.close()

if __name__ == '__main__':
    grabarea()
    
    
    
