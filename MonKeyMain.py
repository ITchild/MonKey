from tkinter import *
import os

top = Tk()
'''包名的行控件 START'''
pageFragme = Frame(top)
lPage = Label(pageFragme, text="测试包名")
lPage.pack(side="left")
pageName = Entry(pageFragme)
pageName.insert(0,"com.ck.u8x_ck")
pageName.pack(side="right")
pageFragme.pack()
'''包名的行控件 END'''
'''运行次数的行控件 START'''
runNumFragme = Frame(top)
runNumPage = Label(runNumFragme, text="运行次数")
runNumPage.pack(side="left")
runNum = Entry(runNumFragme)
runNum.insert(0,5000)
runNum.pack(side="right")
runNumFragme.pack()
'''运行次数的行控件 END'''

def testMonkey():
    pageNameS = pageName.get()
    num = runNum.get()
    os.system("adb shell monkey -p "+pageNameS+" -v -v "+num)


okButton = Button(top, text="点我", command=testMonkey)
okButton.pack()
top.title("MonKey测试工具")
top.mainloop()
