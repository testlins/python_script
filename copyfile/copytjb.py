# -*- coding:utf-8 -*-
#author=linxs
from win32com.shell import shell, shellcon
import os
import filecmp
import time
import ConfigParser
import mylog
import Tkinter
import win32process
import win32gui
import win32api
import win32con


mylog = mylog.initlog()
config = ConfigParser.ConfigParser()
with open('copytjb.ini','r+') as cfgfile:
    config.readfp(cfgfile)
    olddir = config.get('dirinfo','olddir')
    newdir = config.get('dirinfo','newdir')
    reportfile = config.get('dirinfo','reportfile')
    localreportfile = config.get('dirinfo','localreportfile')
    #win平台下编码成utf-8
    lookup = (config.get('filter','lookup')).decode('gbk').encode('utf-8')
    sleeptime = config.get('time','sleeptime')
    #killpro = config.get('process','killpro')
    processname = config.get('process','processname')
    svnfile = config.get('dirinfo','svnfile')
    localsvnfile = config.get('dirinfo','localsvnfile')
    opensvnfile = config.get('opensvn','opensvnfile')
    
def ischange(reportfile,localreportfile):
    """判断report文件是否有改变"""
    if not os.path.exists(localreportfile):
        localreportfile = file(localreportfile,'w')
        localreportfile.close()
        mylog.info('文件创建成功')
        return True
        
    else:
        if not filecmp.cmp(reportfile,localreportfile):
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
    #if killpro == 'True':
    command = 'taskkill /F /IM %s'%processname
    os.system(command)
    mylog.info('程序已关闭/未打开')
    #else:
        #print '酱油'
        #pass
    

def copytjb():
    """拷文件"""
    mylog.info('准备复制olddir，reportfile')
    try:
        shell.SHFileOperation ((0, shellcon.FO_COPY, olddir, newdir,shellcon.FOF_NOCONFIRMMKDIR|shellcon.FOF_NOCONFIRMATION, None, None))
        shell.SHFileOperation ((0, shellcon.FO_COPY, reportfile, localreportfile,shellcon.FOF_NOCONFIRMATION, None, None))
        shell.SHFileOperation ((0, shellcon.FO_COPY, svnfile, localsvnfile,shellcon.FOF_NOCONFIRMATION, None, None))
        mylog.info('复制olddir，reportfile成功')
    except:
        mylog.error('复制失败，请关闭相关程序，再试')

def opensvnlog():
    if opensvnfile == 'True':
        command = 'c:/windows/system32/notepad.exe  %s'%localsvnfile
        os.system(command)
    else:
        pass

def dotime():
    nowtime = list(time.localtime())
    if nowtime[3]>=16: 
        print nowtime[4]
        exe_path = r"D:\Program Files (x86)\Spasvo\AutoRunner"
        exe_file = r'AutoRunner.exe'
        #command = r'"D:\Program Files (x86)\Spasvo\AutoRunner\AutoRunner.exe"'
        #command = ur'c:\windows\system32\notepad.exe'
        #command = r'"C:\Program Files (x86)\Youdao\YoudaoNote\RunYNote.exe"'
        #os.popen(command)
        handle = win32process.CreateProcess(os.path.join(exe_path, exe_file),
                '', None, None, 0,
                win32process.CREATE_NO_WINDOW,
                None ,
                exe_path,
                win32process.STARTUPINFO())
        return True

def chickmouse():
    time.sleep(5)
    win32api.SetCursorPos((150, 60))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.05)
    

def copy():
    kill(processname)
    copytjb()
    opensvnlog()

if __name__ == '__main__':
    while True:
        dotime()
        if dotime():
            chickmouse()
        elif ischange(reportfile,localreportfile) and findstrinfile(reportfile,lookup) and not dotime():
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