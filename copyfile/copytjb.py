# -*- coding:utf-8 -*-
from win32com.shell import shell, shellcon
import os
import tempfile
import filecmp
import time
import ConfigParser
import mylog

mylog = mylog.initlog()
config = ConfigParser.ConfigParser()
with open('copytjb.ini','r+') as cfgfile:
    config.readfp(cfgfile)
    olddir = config.get('dirinfo','olddir')
    newdir = config.get('dirinfo','newdir')
    scofile = config.get('dirinfo','scofile')
    localfile = config.get('dirinfo','localfile')
    #win平台下编码成utf-8
    lookup = (config.get('filter','lookup')).decode('gbk').encode('utf-8')
    sleeptime = config.get('time','sleeptime')
    killpro = config.get('process','killpro')
    processname = config.get('process','processname')
    
def ischange(scofile,localfile):
    if not os.path.exists(localfile):
        localfile = file(localfile,'w')
        localfile.close()
        mylog.info('文件创建成功')
        return True
        
    else:
        if not filecmp.cmp(scofile,localfile):
            mylog.info('report对比有改变')
            return True
        else:
            mylog.info('report没改变，不做操作')
            return False

def findstrinfile(filename, lookup):
    if lookup not in open(filename,'rt').read():
        mylog.info('集成操作成功')
        return True
    else:
        mylog.info('集成失败，请通知相关人员，不做操作')
        return False

def kill(processname):
    if killpro == 'True':
        command = 'taskkill /F /IM %s'%processname
        os.system(command)
        mylog.info('程序已关闭/未打开')
    else:
        #print '酱油'
        pass
    

def copytjb():
    mylog.info('准备复制olddir，scofile')
    try:
        shell.SHFileOperation ((0, shellcon.FO_COPY, olddir, newdir,shellcon.FOF_NOCONFIRMMKDIR|shellcon.FOF_NOCONFIRMATION, None, None))
        shell.SHFileOperation ((0, shellcon.FO_COPY, scofile, localfile,shellcon.FOF_NOCONFIRMATION, None, None))
        mylog.info('复制olddir，scofile成功')
    except:
        mylog.error('复制失败，请关闭相关程序，再试')


if __name__ == '__main__':
    while True:
        if ischange(scofile,localfile) and findstrinfile(scofile,lookup):
            kill(processname)
            copytjb()
        time.sleep(int(sleeptime))