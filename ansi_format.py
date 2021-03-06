﻿#-*- coding:utf-8 -*-
from tkinter import *
from tkinter import filedialog
import os
import re

def srcselectPath():
    path_= filedialog.askdirectory()
    srcpath.set(path_)
    
def dstselectPath():
    path_= filedialog.askdirectory()
    dstpath.set(path_)  

def getallPath():
    for root, dirs, files in os.walk(srcpath.get()):
        for dire in dirs:
            os.chdir(dstpath.get()+root[len(srcpath.get()):])
            os.mkdir(dire)
        for name in files:
            filepath = os.path.join(root, name)
            f =  open(filepath,"r")
            ff = open(dstpath.get()+"//" + filepath[len(srcpath.get()):],"w")
            str1 = f.read()
            str2 = re.sub(r"//(.*)",r"/*\1*/",str1)
            ff.write(str2)
            f.close()
            ff.close()
  
root = Tk()
dstpath = StringVar()
srcpath = StringVar()

root.title("文件转换助手")
root.geometry("240x100+400+300")      #宽 x 高 + 左边距 + 上边距
root['bg'] =  "lightblue"
Label(root,bg = 'lightblue', text = "源路径").grid(row = 0, column = 0)
Entry(root, textvariable = srcpath).grid(row = 0, column = 1)
Button(root,bg = 'lightblue',text = "选择", command = srcselectPath).grid(row = 0, column = 2)

Label(root, bg = 'lightblue',text = "目的路径").grid(row = 1, column = 0)
Entry(root, textvariable = dstpath).grid(row = 1, column = 1)
filedialog.Button(root,bg = 'lightblue',text = "选择", command = dstselectPath).grid(row = 1, column = 2)
filedialog.Button(root,text = "转换", width = 20,bg = "lightblue",command = getallPath).grid(row = 2,column = 1)
root.mainloop()