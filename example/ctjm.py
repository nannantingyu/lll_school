from __future__ import (
    division,
    print_function,
)

import cv2
import sys
import array
import os as _os
import numpy as np
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.misc

from PIL import Image
from skimage import data,filters
from skimage.data import data_dir
from skimage.io import imread, use_plugin
from skimage._shared._warnings import expected_warnings
from skimage.data._binary_blobs import binary_blobs
from skimage.data import img_as_bool
from pylab import *

import tkinter
from tkinter import filedialog

global path1
path1='123123'

global path2
path2='111'

global _ave
_ave=0

#global yuantu
#yuantu=''

#global count1
#count1=0

#传参
def chuancan(A):
	global path2
	A=path2    

def junzhi2(a):
    sum=0
    ave=a.mean()
    global _ave
    _ave=ave
    #print("ave=")
    #print(ave)



#button1打开文件对话框
def openfiles2():    
    #global count1
    #count1=count1+1
    s2fname = filedialog.askopenfilename(title='打开bmp文件', filetypes=[('bmp', '*'), ('All Files', '*')])
    print(s2fname)
    global path1
    path1=s2fname
    global path2
    path3=path1.split('.')
    path2=path3[0]

    chuancan(path2)
    #print(path2)
    #print(path1)

    img = Image.open(s2fname)  #打开图片
    img1=Image.open(s2fname)

    #更改图片尺寸
    (x,y) = img.size  
    x_s=512
    y_s=512
    img=img.resize((x_s,y_s),Image.ANTIALIAS)
    img1=img1.resize((x_s,y_s),Image.ANTIALIAS)


    #灰度化
    im1 = array(img.convert('L'))
    im2 = array(img.convert('L'))
    #scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\huidu.png', im1)
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\yuantu.png',img1)
    
    #string_path='C:\\Users\\Administrator\\Desktop\\lily\\yuantu%d.png'%(count1)
    #scipy.misc.imsave(string_path, img1)
    #global yuantu
    #yuantu=string_path
    img3 = Image.open('C:\\Users\\Administrator\\Desktop\\lily\\yuantu.png')
    img3 = img3.resize((200, 200), Image.ANTIALIAS)
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\yuantu1.png',img3)

    #将图片三值化

    img_new=im1
    im=img_new
    imm=im
    junzhi2(imm)
    threshold=_ave-10
    for i in range(0,im.shape[0]):
        for j in range(0,im.shape[1]):
            if imm[i][j]>=threshold:
                imm[i][j]=255
            else:
                if imm[i][j]>threshold-50:
                    imm[i][j]=125
                else:
                    imm[i][j]=0

    #中值滤波                
    for i in range (10):   #迭代次数
        imgg = cv2.medianBlur(imm,5)  #5*5

    plt.subplot(1,3,1),plt.imshow(im2,'gray')
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\huidu.png', im2)        
    plt.subplot(1,3,2),plt.imshow(imm,'gray')
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\sanzhi.png', imm)
    plt.subplot(1,3,3),plt.imshow(imgg,'gray')#默认彩色，另一种彩色bgr
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png', imgg)

    im = tkinter.PhotoImage(file='C:\\Users\\Administrator\\Desktop\\lily\\yuantu1.png')
    canvas1.create_image(0, 0, anchor='nw', image=im)
    canvas1.pack()
    # plt.show()

    #path1='C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png'
    #return path1
#plt.show()
    


#button2显示中值滤波（去躁）    
def xianshi_lvbo():
    #global yuantu
    '''
    img3 = Image.open('C:\\Users\\Administrator\\Desktop\\lily\\yuantu.png')
    img3 = img3.resize((400, 360), Image.ANTIALIAS)
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\yuantu1.png',img3)
    img_png = tkinter.PhotoImage(file = 'C:\\Users\\Administrator\\Desktop\\lily\\yuantu1.png')
    label_img = tkinter.Label(root, image = img_png,width = 400,height = 400,text = 'left')  
    #label_img.pack()
'''

    
    # im = tkinter.PhotoImage(file='C:\\Users\\Administrator\\Desktop\\lily\\yuantu1.png')
    # canvas1.create_image(0,0,anchor='nw',image = im)
    # plt.show()
    pass
    
#button3创建文件夹
def mkdir(path):# 引入模块
	global path2
	print(path2)
	import os
	path=path.strip()# 去除首位空格  
	path=path.rstrip("\\")# 去除尾部 \ 符号

	isExists=os.path.exists(path)
	if not isExists:
		os.makedirs(path) 
 
		print (path+' 创建成功')
		return True
	else:
		print (path+' 目录已存在')   
		return False
	import example
	example.main()

    # 定义要创建的目录
#mkpath="C:\\Users\\Administrator\\Desktop\\hahhh"
#mkdir(mkpath)

#button4调取提取
def tiqu():
    im = tkinter.PhotoImage(file='C:\\Users\\Administrator\\Desktop\\lily\\yuantu1.png')
    canvas2.create_image(0,0,anchor='nw',image = im)
    import tq
    tq.mn()
    

#button5提取显示
def xianshi_tiqu():
    
    im = tkinter.PhotoImage(file=path2+"\\"+'2.png')
    canvas3.create_image(0,0,anchor='nw',image = im)
    
    fname = filedialog.askopenfilename(initialdir = path2)
    #filename = tkFileDialog.askopenfilename(initialdir = 'F:\\丽丽毕设\\数据集\\数据集\\0028-2')
    print(fname)


#窗体
root = tkinter.Tk()
root.title('毕设')
root.geometry('615x600+600+0')
#root.geometry('500x300+500+200')
canvas1 = tkinter.Canvas(root,
    width = 200,      # 指定Canvas组件的宽度
    height = 200,      # 指定Canvas组件的高度
    bg = 'white') 
canvas2 = tkinter.Canvas(root,
    width = 200,      # 指定Canvas组件的宽度
    height = 200,      # 指定Canvas组件的高度
    bg = 'white') 
canvas3 = tkinter.Canvas(root,
    width = 200,      # 指定Canvas组件的宽度
    height = 200,      # 指定Canvas组件的高度
    bg = 'white') 
        
label_text = tkinter.Label(root,text = '基于感兴趣区域的细胞提取系统',bg = 'gray',width = 40,height = 4, font=("黑体", 20, "bold"),justify = 'left').pack(fill='x')
btn1 = tkinter.Button(root, text='打开bmp文件', bg="red", fg="white",font =("宋体",12),width=12,height=2, command=openfiles2)
btn2 = tkinter.Button(root, text='显示预处理', bg="green", fg="black",font =("宋体",12),width=12,height=2, command=xianshi_lvbo)
btn3 = tkinter.Button(root, text='创建文件夹',bg="red", fg="white",font = ('宋体',12),width=12,height=2, command=lambda : mkdir(path=path2))
btn4 = tkinter.Button(root, text='打开提取文件',bg="green", fg="black",font = ('宋体',12),width=12,height=2, command=tiqu)
btn5 = tkinter.Button(root, text='显示提取文件',bg="red", fg="white",font = ('宋体',12),width=12,height=2, command=xianshi_tiqu)
label_text1 = tkinter.Label(root,text = '图片展示',bg = 'gray',width = 10,height = 2, font=("黑体", 12,"bold"),justify = 'left')
#label_text2 = tkinter.Label(root,text = '提取展示',bg = 'gray',width = 10,height = 2, font=("黑体", 12,"bold"),justify = 'left')
#label_text3 = tkinter.Label(root,text = '提取展示',bg = 'gray',width = 10,height = 2, font=("黑体", 12,"bold"),justify = 'left')
btn1.pack(side='top',fill='x') 
btn2.pack(side='top',fill='x')
btn3.pack(side='top',fill='x')
btn4.pack(side='top',fill='x')
btn5.pack(side='top',fill='x')
label_text1.pack()
canvas1.pack(side='left')
canvas2.pack(side='left')
canvas3.pack(side='left')
#import os
#if os.access("C:\\Users\\Administrator\\Desktop\\lily\\yuantu.png", os.F_OK):
    
#import os  
#path = "C:\\Users\\Administrator\\Desktop\\aa" #文件夹目录  
#files= os.listdir(path) #得到文件夹下的所有文件名称 
#print(files) 
#for file in files: #遍历文件夹         
 #       img_png3 = tkinter.PhotoImage(file = "C:\\Users\\Administrator\\Desktop\\aa\\"+str(file)+"")  
 #       label_img3 = tkinter.Label(root, image = img_png3,width = 100,height = 100,text = 'left')  
 #       label_img3.pack()

#list1 = open('C:\\Users\\Administrator\\Desktop\\lily')




#---------------------------------------------------------------------------------------------------------------------------
#滚动条
'''
scrollbar = tkinter.Scrollbar(root)
scrollbar.pack( side = 'right', fill='y' )

mylist = tkinter.Listbox(root, yscrollcommand = scrollbar.set ,width=100)
#for line in range(100):
 #  mylist.insert('end', "F:\\丽丽毕设\\所有暂存文件\\haha2\\" + str(line)+".bmp")
#f = open('C:\\Users\\Administrator\\Desktop\\aa',encoding='utf-8',)
#raw = f.read()

import os  
path8 = "C:\\Users\\Administrator\\Desktop\\aa" #文件夹目录  
files= os.listdir(path8) #得到文件夹下的所有文件名称 
#print(files) 
strA=""
temp=[]
i=0
for file in files: #遍历文件夹  
    #if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
     #   f = open(path+"/"+file); #打开文件 

    mylist. insert('end', "C:\\Users\\Administrator\\Desktop\\aa\\" + str(file))
    #print(mylist.get(i))
    strA="C:\\Users\\Administrator\\Desktop\\aa\\" + str(file)
    temp.append(strA)
    # i=i+1

    img_png = tkinter.PhotoImage(file = strA)  
    label_img=tkinter.Label(root, image = img_png,width = 100,height = 100,text = 'left') 
    #label_img.pack()
    label_img.pack(side='left',expand='yes',fill='none')
    
    #label_img[i].pack(padx=i*2.5 ,pady=i*1.2)
 
mylist.pack( side = 'right', fill = 'both' )
scrollbar.config( command = mylist.yview )
'''
#----------------------------------------------------------------------------------------------------------------------
'''
for i in range(len(temp)):
    img_png = tkinter.PhotoImage(file = temp[i])  
    print("img_png====")
    print(temp[i])
    label_img=tkinter.Label(root, image = img_png,width = 100,height = 100,text = 'left')
    #label_img=tkinter.Label(root, image = img_png,width = 100,height = 100,text = 'left') 
    #label_img.pack(ipadx=i*33.5 ,ipady=i*36.2)
    #label_img.pack(padx=i*33.5 ,pady=i*36.2)

label_img.pack(side = 'left')
'''
#btn2.pack(side='left')

root.mainloop()