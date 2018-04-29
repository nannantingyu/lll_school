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

#打开文件对话框
def openfiles2():
    s2fname = filedialog.askopenfilename(title='打开bmp文件', filetypes=[('bmp', '*'), ('All Files', '*')])
    print(s2fname)
    global path1
    path1=s2fname
    print(path1)
    img = Image.open(s2fname)  #打开图片

    (x,y) = img.size  #更改图片尺寸
    x_s=512
    y_s=512
    img=img.resize((x_s,y_s),Image.ANTIALIAS)

    im1 = array(img.convert('L'))   #将图片灰度化
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\img.bmp', im1)
    
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
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\sanzhi.bmp', imm)
    plt.subplot(1,2,2),plt.imshow(imgg,'gray')#默认彩色，另一种彩色bgr
    scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp', imgg)
    #img.save('C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp', imgg)
    
    path1='C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp'
    return path1

    #path2='C:\\Users\\Administrator\\Desktop\\lily\\sanzhi.bmp'
    #return path2

#plt.show()

#中值滤波显示（去躁）
def xianshi_lvbo():
    #img1=imread(path1)
    #plt.subplot(111)
    #plt.imshow(img1)
    plt.show()

def tiqu():
    import example
    example.main()


    '''
def openfilecgns():
    cgnsfname = filedialog.askopenfilename(title='打开CGNS文件',filetypes=[('CGNSdat', '*.dat'), ('All Files', '*')] )
    print(cgnsfname)
 '''

#窗体
root = tkinter.Tk()
root.title('毕设')
root.geometry('1000x500')
#root.geometry('500x300+500+200')

btn1 = tkinter.Button(root, text='打开bmp文件',font =("宋体",20),width=10,height=2, command=openfiles2)
btn2 = tkinter.Button(root, text='显示预处理',font =("宋体",20),width=10,height=2, command=xianshi_lvbo)
btn3 = tkinter.Button(root, text='打开提取文件',font = ('宋体',20),width=10,height=2, command=tiqu)

btn1.pack(side='left') 
btn2.pack(side='left')
btn3.pack(side='left')

#btn2.pack(side='left')

root.mainloop()