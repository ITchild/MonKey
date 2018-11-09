import tkinter
import tkinter.messagebox
import os

top = tkinter.Tk()
'''包名的行控件 START'''
pageFragme = tkinter.Frame(top)
lPage = tkinter.Label(pageFragme, text="测试包名")
lPage.pack(side="left")
pageName = tkinter.Entry(pageFragme)
pageName.insert(0, "com.ck.u8x_ck")
pageName.pack(side="right")
pageFragme.pack()
'''包名的行控件 END'''
'''运行次数的行控件 START'''
runNumFragme = tkinter.Frame(top)
runNumPage = tkinter.Label(runNumFragme, text="运行次数")
runNumPage.pack(side="left")
runNum = tkinter.Entry(runNumFragme)
runNum.insert(0, 5000)
runNum.pack(side="right")
runNumFragme.pack()
'''运行次数的行控件 END'''

def testMonkey():
    pageNameS = pageName.get()
    if not ("." in pageNameS):
        tkinter.messagebox.askokcancel("提示", "包名输入不合法（***.***.***的形式）")
        return
    num = runNum.get() + ""
    if not num.isdigit():
        tkinter.messagebox.askokcancel("提示", "运行次数，请输入数字")
        return
    os.system("adb shell monkey -p " + pageNameS + " -v -v " + num)


okButton = tkinter.Button(top, text="运行MonKey测试", command=testMonkey)
okButton.pack()
top.title("MonKey测试工具")
ww = 200
wh = 150
x = top.winfo_screenwidth()
y = top.winfo_screenheight()
x = (x - ww) / 2
y = (y - wh) / 2
top.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
top.mainloop()
