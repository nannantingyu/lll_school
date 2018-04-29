'''
from tkinter import *
from tkinter.filedialog import askdirectory

def selectPath():
    path_ = askdirectory()
    path.set(path_)

root = Tk()
path = StringVar()

Label(root,text = "目标路径:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)

root.mainloop()
'''
#import tkinter.filedialog
#a=tkinter.filedialog.askopenfilename()


'''
#!/usr/bin/env python
#!encoding:utf-8
#!filename:test_filedialog.py
import tkinter.filedialog as filedialog
from tkinter import *
import os
from tkinter import *
 
def callback():
    entry.delete(0,END) #清空entry里面的内容
    listbox_filename.delete(0,END)
    #调用filedialog模块的askdirectory()函数去打开文件夹
    global filepath
    filepath = filedialog.askdirectory() 
    if filepath:
        entry.insert(0,filepath) #将选择好的路径加入到entry里面
    print (filepath)
    getdir(filepath)
 
def getdir(filepath=os.getcwd()):
    """
    用于获取目录下的文件列表
    """
    cf = os.listdir(filepath)
    for i in cf:
        listbox_filename.insert(END,i)
 
if __name__ == "__main__":
    root = Tk()
    root.title("测试版本")
    root.geometry("400x400")
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=8)
 
    entry = Entry(root, width=60)
    entry.grid(sticky=W+N, row=0, column=0, columnspan=4, padx=5, pady=5)
 
    button = Button(root,text="选择文件夹",command=callback)
    button.grid(sticky=W+N, row=1, column=0, padx=5, pady=5)
    #创建loistbox用来显示所有文件名
    listbox_filename = Listbox(root, width=60)
    listbox_filename.grid(row=2, column=0, columnspan=4, rowspan=4, 
                            padx=5, pady=5, sticky=W+E+S+N)
 
    root.mainloop()
    '''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：通过打开一个文件对话窗口来选择文件，获得文件路径（包含文件名和后缀）
时间：2017年3月10日 15:40:06
"""

# _*_ coding:utf-8 _*_


import tkinter
from tkinter import filedialog


def openfiles2():
    s2fname = filedialog.askopenfilename(title='打开bmp文件', filetypes=[('bmp', '*'), ('All Files', '*')])
    print(s2fname)
    '''
def openfilecgns():
    cgnsfname = filedialog.askopenfilename(title='打开CGNS文件',filetypes=[('CGNSdat', '*.dat'), ('All Files', '*')] )
    print(cgnsfname)
 '''
root = tkinter.Tk()
root.title('丽丽毕设')
root.geometry('1000x500')
#root.geometry('500x300+500+200')
btn1 = tkinter.Button(root, text='打开bmp文件',font =("宋体",20),width=10,height=2, command=openfiles2)
#btn2 = tkinter.Button(root, text='打开CGNS文件',font = ('宋体',20),width=13,height=2, command=openfilecgns)
 
btn1.pack(side='top')
#btn2.pack(side='left')
root.mainloop()
