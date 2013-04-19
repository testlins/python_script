#coding=utf-8
from Tkinter import *
import creid_rule
import id_rule
root = Tk()
def creid():
    id = creid_rule.creid_rule()
    idnum = id.cre_idnum()
    entryid.set(idnum)

def checkid():
    id = checkid_entry.get()
    checkid = id_rule.id_rule(id)
    if checkid.id_isarea() and checkid.id_isdate() and checkid.id_rule():
        area = checkid.id_isarea()
        age = checkid.calc_age()
        
        print "hahahh"
    else:
        print 'nonono'

creid_bu = Button(root,text='生成身份证',command = creid)
entryid = StringVar()
creid_entry = Entry(root,textvariable = entryid)
creid_bu.pack()
creid_entry['state'] = 'readonly'
creid_entry.pack()

checkid_entry=Entry(root,textvariable = '请输入省份证号')
checkid_entry.pack()
checkid_bu = Button(root,text='验证身份证',command = checkid)
checkid_bu.pack()


root.mainloop()



