#coding=utf-8
from Tkinter import *
import creid_rule
import id_rule
root = Tk()

def creid():
    '''随机创建身份证号，并获取相关信息'''
    creid = creid_rule.creid_rule()
    idnum = creid.cre_idnum()
    entryid.set(idnum)
    checkcreid(idnum)

    
def checkid():
    """检测身份证号，获取相关信息"""
    id = checkid_entry.get()
    #if len(id)>18:
       # checkid_entry.delete(18,END)
    #age_entry.delete(0,END)
    #label1.delete(0,END)
    agelabel.set('')
    sexlabel.set('')
    arealabel.set('')
    errorlabel.set('')
    try:
        checkid = id_rule.id_rule(id)
        if checkid.id_isarea() and checkid.id_isdate() and checkid.id_rule():
            area = checkid.id_isarea()
            age = checkid.calc_age()
            sex = checkid.id_numsex()
            agelabel.set(age)
            sexlabel.set(sex)
            arealabel.set(area)
        else:
            errortext = '输入号码错误'
            errorlabel.set(errortext)
            checkid_entry.delete(0,END)
    except:
        errortext = '输入18位身份证'
        errorlabel.set(errortext)

def checkcreid(id):
    """为获取生成身份证信息而创建的类，是否可以和上面的合并"""
    agelabel.set('')
    sexlabel.set('')
    arealabel.set('')
    errorlabel.set('')
    try:
        checkid = id_rule.id_rule(id)
        if checkid.id_isarea() and checkid.id_isdate() and checkid.id_rule():
            area = checkid.id_isarea()
            age = checkid.calc_age()
            sex = checkid.id_numsex()
            agelabel.set(age)
            sexlabel.set(sex)
            arealabel.set(area)
        else:
            errortext = '输入号码错误'
            errorlabel.set(errortext)
            checkid_entry.delete(0,END)
    except:
        errortext = '输入18位身份证'
        errorlabel.set(errortext)

        





def checkid_callback(a):
    """检测键盘输入"""
    #id = checkid_entry.get()
    #if len(id)>18:
     #   checkid_entry.delete(18,END)
    l = list(checkid_entry.get())  
    last_num = ['1','0','X','9','8','7','6','5','4','3','2']
    """if l[17] not in last_num:
        errortext = '输入字符类型错误11'
        errorlabel.set(errortext)  
        checkid_entry.delete(17, 17) """         
    for i in range(len(l)-1,-1,-1):
#    for i in range(0,len(l)):
        #print i
        if i==17:
           if l[i] not in last_num:
            checkid_entry.delete(17)
            errortext = '最后一位为0~9,或X'
            errorlabel.set(errortext)  
            #checkid_entry.delete(17)
        elif i>17:
            checkid_entry.delete(18,END)
            
        else:
            if not(48 <= ord(l[i]) <= 57 ):
                checkid_entry.delete(i,i+1)
                errortext = '字符类型错误'
                errorlabel.set(errortext)  
                #checkid_entry.delete(i,i+1)  
                
    

creid_bu = Button(root,text='生成身份证',command = creid)
entryid = StringVar()
creid_entry = Entry(root,textvariable = entryid, width = 18)
creid_bu.pack()
creid_entry['state'] = 'readonly'
creid_entry.pack()

checkid_entry=Entry(root,textvariable = '请输入身份证号', width = 18)
#checkid_entry=MaxLengthEntry(root,textvariable = '请输入身份证号', width = 18)
checkid_entry.bind('<KeyRelease>', checkid_callback)
checkid_entry.pack()
checkid_bu = Button(root,text='验证身份证',command = checkid)
checkid_bu.pack()

#年龄label
agelabel = StringVar()
age_label = Label(root,textvariable = agelabel)
age_label.pack()

#性别信息
sexlabel = StringVar()
sex_label = Label(root,textvariable = sexlabel)
sex_label.pack()
#区域信息
arealabel = StringVar()
area_label = Label(root,textvariable = arealabel)
area_label.pack()
#错误信息
errorlabel = StringVar()
error_label = Label(root,textvariable=errorlabel)
error_label.pack()

root.mainloop()



