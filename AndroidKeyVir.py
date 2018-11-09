#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Author__: 云海星空

import tkinter
import tkinter.messagebox
import os

def actionUp():
    os.system("adb shell input keyevent 19")
def actionDown():
    os.system("adb shell input keyevent 20")
def actionOK():
    os.system("adb shell input keyevent 66")
def actionLeft():
    os.system("adb shell input keyevent 21")
def actionRight():
    os.system("adb shell input keyevent 22")
def actionChange():
    os.system("adb shell input keyevent 131")
def actionBack():
    os.system("adb shell input keyevent 4")
def actionSave():
    os.system("adb shell input keyevent 132")


top = tkinter.Tk()
'''包名的行控件 START'''
oneFragme = tkinter.Frame(top)
upButton = tkinter.Button(oneFragme, text="上", command=actionUp)
upButton.pack()
oneFragme.pack()

twoFragme = tkinter.Frame(top)
leftButton = tkinter.Button(twoFragme, text="左", command=actionLeft)
okButton = tkinter.Button(twoFragme, text="确定", command=actionOK)
rightButton = tkinter.Button(twoFragme, text="右", command=actionRight)
leftButton.pack(side=tkinter.LEFT)
rightButton.pack(side=tkinter.RIGHT)
okButton.pack(side=tkinter.RIGHT)
twoFragme.pack()

threeFragme = tkinter.Frame(top)
downButton = tkinter.Button(threeFragme, text="下", command=actionDown)
downButton.pack()
threeFragme.pack()


fourFragme = tkinter.Frame(top)
changeButton = tkinter.Button(fourFragme, text="切换", command=actionChange)
backButton = tkinter.Button(fourFragme, text="返回", command=actionBack)
saveButton = tkinter.Button(fourFragme, text="存储", command=actionSave)
changeButton.pack(side=tkinter.LEFT)
backButton.pack(side=tkinter.RIGHT)
saveButton.pack(side=tkinter.RIGHT)
fourFragme.pack()


top.title("模拟按键")
ww = 200
wh = 150
x = top.winfo_screenwidth()
y = top.winfo_screenheight()
x = (x - ww) / 2
y = (y - wh) / 2
top.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
top.mainloop()
