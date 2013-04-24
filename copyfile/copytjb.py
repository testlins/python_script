# -*- coding:utf-8 -*-
from win32com.shell import shell, shellcon
import os
import filecmp
import time
import ConfigParser
import mylog
import Tkinter


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
    """判断report文件是否有改变"""
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
    """通过report判断集成是否成功"""
    if lookup not in open(filename,'rt').read():
        mylog.info('集成操作成功')
        return True
    else:
        mylog.info('版本集成失败，请通知相关人员，不做操作')
        root = Tkinter.Tk()
        label =Tkinter.Label(root,text='集成失败，请通知相关人员').pack()
        root.geometry("230x30+600+300")
        root.mainloop()     
        return False

def kill(processname):
    """杀进程，后面学习其他系统监控方法"""
    if killpro == 'True':
        command = 'taskkill /F /IM %s'%processname
        os.system(command)
        mylog.info('程序已关闭/未打开')
    else:
        #print '酱油'
        pass
    

def copytjb():
    """拷文件"""
    mylog.info('准备复制olddir，scofile')
    try:
        shell.SHFileOperation ((0, shellcon.FO_COPY, olddir, newdir,shellcon.FOF_NOCONFIRMMKDIR|shellcon.FOF_NOCONFIRMATION, None, None))
        shell.SHFileOperation ((0, shellcon.FO_COPY, scofile, localfile,shellcon.FOF_NOCONFIRMATION, None, None))
        mylog.info('复制olddir，scofile成功')
    except:
        mylog.error('复制失败，请关闭相关程序，再试')

#def opentjb():
#    command = 'C:\Users\casking_lxs\Desktop\client12\H365.TJB.Client.exe'
#    os.system(command)   

def copy():
    kill(processname)
    copytjb()
if __name__ == '__main__':
    while True:
        if ischange(scofile,localfile) and findstrinfile(scofile,lookup):
            root = Tkinter.Tk()
            label =Tkinter.Label(root,text='程序已有更新').pack()
            button_sure = Tkinter.Button(root,text='更新',command = copy)
            button_sure.pack()
            root.geometry("50x50+600+300") 
            root.mainloop()
            #opentjb()
            #kill(processname)
            #copytjb()
        time.sleep(int(sleeptime))