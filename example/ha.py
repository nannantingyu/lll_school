from __future__ import (
    division,
    print_function,
)
# _*_ coding:utf-8 _*_

import a
import cv2
import sys
import array
#reload(sys)

#sys.setdefaultencoding('utf-8')
import cv2
import os as _os
import numpy as np
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
from PIL import Image
import matplotlib.pyplot as plt
import a 
import scipy.signal as signal
from skimage import data,filters
import scipy.misc

from skimage.data import data_dir
from skimage.io import imread, use_plugin
from skimage._shared._warnings import expected_warnings
from skimage.data._binary_blobs import binary_blobs
from skimage.data import img_as_bool

from PIL import Image

from pylab import *

from PIL import Image

import tkinter 
from tkinter import filedialog

#path1="123123"
global path1
path1='123123'

global path2
path2='111'


def chuancan(A):
	global path2
	A=path2

#button1 打开文件对话框
def openfiles2():
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
    #img = Image.open(s2fname)  #打开图片
    img = Image.open(s2fname)  #打开图片
    img1=Image.open(s2fname)

    (x,y) = img.size  #更改图片尺寸
    x_s=512
    y_s=512
    img=img.resize((x_s,y_s),Image.ANTIALIAS)
    img1=img1.resize((x_s,y_s),Image.ANTIALIAS)

    im1 = array(img.convert('L'))   #将图片灰度化
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\img.png', im1)
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\yuantu.png', img1)
    

    
    #将图片三值化
    img_new=im1
    im=img_new
    imm=im
    threshold=160
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

    plt.subplot(1,2,1),plt.imshow(imm,'gray')
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\sanzhi.png', imm)
    plt.subplot(1,2,2),plt.imshow(imgg,'gray')#默认彩色，另一种彩色bgr
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png', imgg)
    #img.save('C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp', imgg)
    #cv2.imwrite('C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp', imgg)
    #plt.imsave('C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp', imgg)

    #path1='C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png'
    #return path1

    #path2='C:\\Users\\Administrator\\Desktop\\lily\\sanzhi.bmp'
    #return path2

#plt.show()



def xianshi_tiqu():
	fname = filedialog.askopenfilename(initialdir = path2)
	#filename = tkFileDialog.askopenfilename(initialdir = 'F:\\丽丽毕设\\数据集\\数据集\\0028-2')
	print(fname)
    



#中值滤波显示（去躁）
def xianshi_lvbo():
    #img1=imread(path1)
    #plt.subplot(111)
    #plt.imshow(img1)
    
    img_png = tkinter.PhotoImage(file = 'C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png')  
    label_img = tkinter.Label(root, image = img_png,width = 400,height = 400,text = 'left')  
    label_img.pack()

    
    plt.show()




def tiqu():
    import example
    example.mn()

def mkdir(path):
    # 引入模块
	global path2
	print(path2)
	import os
 
    # 去除首位空格
	path=path.strip()
    # 去除尾部 \ 符号
	path=path.rstrip("\\")
 
    # 判断路径是否存在   # 存在     True   # 不存在   False
	isExists=os.path.exists(path)
 
    # 判断结果
	if not isExists:
		os.makedirs(path) 
 
		print (path+' 创建成功')
		return True
	else:
        # 如果目录存在则不创建，并提示目录已存在
		print (path+' 目录已存在')   
		return False
	import example
	example.main()

# 定义要创建的目录
#mkpath="C:\\Users\\Administrator\\Desktop\\hahhh"
#mkdir(mkpath)
# 调用函数


#窗体
root = tkinter.Tk()
root.title('毕设')
root.geometry('350x765')
#root.geometry('500x300+500+200')
label_text = tkinter.Label(root,text = '基于感兴趣区域的细胞提取系统',bg = 'gray',width = 40,height = 4, font=("黑体", 20, "bold"),justify = 'left').pack()

btn1 = tkinter.Button(root, text='打开bmp文件',bg = 'gray',font =("宋体",12),width=12,height=2, command=openfiles2)
btn2 = tkinter.Button(root, text='显示预处理',bg = 'gray',font =("宋体",12),width=12,height=2, command=xianshi_lvbo)
#btn3 = tkinter.Button(root, text='打开提取文件',bg = 'gray',font = ('宋体',12),width=12,height=2, command=tiqu)
btn3 = tkinter.Button(root, text='创建文件夹',bg = 'gray',font = ('宋体',12),width=12,height=2, command=lambda : mkdir(path=path2))
btn4 = tkinter.Button(root, text='打开提取文件',bg = 'gray',font = ('宋体',12),width=12,height=2, command=tiqu)
btn5 = tkinter.Button(root, text='显示提取文件',bg = 'gray',font = ('宋体',12),width=12,height=2, command=xianshi_tiqu)


btn1.pack(side='top') 
btn2.pack(side='top')
btn3.pack(side='top')
btn4.pack(side='top')
btn5.pack(side='top')

#import os  
#path = "C:\\Users\\Administrator\\Desktop\\aa" #文件夹目录  
#files= os.listdir(path) #得到文件夹下的所有文件名称 
#print(files) 
#for file in files: #遍历文件夹         
 #       img_png3 = tkinter.PhotoImage(file = "C:\\Users\\Administrator\\Desktop\\aa\\"+str(file)+"")  
 #       label_img3 = tkinter.Label(root, image = img_png3,width = 100,height = 100,text = 'left')  
 #       label_img3.pack()



#list1 = open('C:\\Users\\Administrator\\Desktop\\lily')
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
    label_img.pack(side='right',expand='yes',fill='none')
    
   
    #label_img[i].pack(padx=i*2.5 ,pady=i*1.2)
 


mylist.pack( side = 'right', fill = 'both' )

scrollbar.config( command = mylist.yview )

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