#coding=utf-8
import Tkinter
import ttk
import vemrule
import vemdb

#xx = vemrule.vemrule(10,1)
#ss= xx.BuyRule()

root = Tkinter.Tk()
#agelabel = StringVar()
#age_label = Tkinter.Label(root, text = s)
#age_label.pack()

v = Tkinter.IntVar()
v.set(4)
y = vemdb.vemdb()
x = y.select_info()
z =y.select_submoney()
s = sorted(z.keys(),reverse = True)

def sel():

    
    selection = "单价"+str(x[v.get()-1][1])+"元"
    #selection = "You selected the option "+ str(x[Tkinter.Radiobutton.value][1])
    #vemrule1 =vemrule.vemrule(int(box.get()),int(x[v.get()-1][0]))
    #buy = vemrule1.BuyRule()
    #print buy
    
    label.config(text = selection)
def zhao1():
#    y = vemdb.vemdb()
#    x = y.select_info()
    #print x[v.get()-1][0]
    #print int(box.get()),int(x[v.get()-1][0])
    vemrule1 =vemrule.vemrule(int(box.get()),int(x[v.get()-1][0]))
    AllCalc1 = vemrule1.AllCalc()
    
    #lz.append(buy)
    #lz.append(AllCalc1)
    label2.config(text = AllCalc1)
    label5.config(text = "找零"+str(vemrule1.InitChange)+"元")
    #print buy



    
        
for i in range(len(x)):
    Tkinter.Radiobutton(root,variable = v,indicatoron = 0,text = x[i][2],value = x[i][0],command=sel).pack(side = "left",fill='y')


"""label3 = Tkinter.Label(root,text='投币')
label3.pack(side = "left")"""

    
box = ttk.Combobox(state='readonly')
box['values'] = s
box.pack(side = "top")

"""label4 = Tkinter.Label(root,text='单价')
label4.pack()"""

                  
label = Tkinter.Label(root)
label.pack()
    
label5 = Tkinter.Label(root)
label5.pack()


label2 = Tkinter.Label(root)
label2.pack()











"""label6 = Tkinter.Label(root,text='交易结果')
label6.pack()"""

#creid_entry = Tkinter.Entry(root,textvariable = 'd',text='test', width = 18)

#creid_entry['state'] = 'readonly'
#creid_entry.pack()






checkid_bu = Tkinter.Button(root,text='购买',command = zhao1)
checkid_bu.pack()


class vemui(object):
    """vem界面"""
    pass

root.mainloop()