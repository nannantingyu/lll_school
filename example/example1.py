# -*- coding: utf-8 -*-
from __future__ import (
    division,
    print_function,
)
import sys

#reload(sys)

#sys.setdefaultencoding('utf-8')

import os as _os
import numpy as np
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
from PIL import Image
import matplotlib.pyplot as plt
import a 
import cv2

from skimage.data import data_dir
from skimage.io import imread, use_plugin
from skimage._shared._warnings import expected_warnings
from skimage.data._binary_blobs import binary_blobs
from skimage.data import img_as_bool
from PIL import ImageGrab 



def bijiao(a,min1):
    a.sort(reverse=True)
    #min1=[]
    for i in range(len(a)-1):
        min1.append(a[i]-a[i+1])
        #min1[i]=a[i]-a[i+1]
    #print(min1)

    return min1



def new_bijiao(a,x,flag1):
    y=100
    
    for i in range(len(a)-2):
        y=x-a[i]
        #print("得：y")
        #print(y)
        #if abs(y)<25:
        if abs(y)<10:
            flag1=1
            break
        else:
            flag1=0

    print('---finally---')
    print(flag1)
    return flag1


def main():
    #print("sfkjhskfdg")
    
    num=0  #--------------
    #print (skimage)
    #print(skimage.data.astronaut())
    #print(tupian())
    print("-------------\n")
    #/Users/wangyunqi/Desktop/丽丽毕设/2.bmp
    #img=imread("/Users/wangyunqi/Desktop/丽丽毕设/2.bmp")
    #img=imread("/Users/wangyunqi/Desktop/预处理/滤波(5*5) 5.bmp")
    #/Users/wangyunqi/Desktop/0046-2.bmp
    #img=imread("/Users/wangyunqi/Desktop/预处理/滤波(5*5) 5.bmp")
    img=imread("C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png")
    #orig = Image.open("/Users/wangyunqi/Desktop/丽丽毕设/2.bmp")
    #orig1 = Image.open("/Users/wangyunqi/Desktop/丽丽毕设/2.bmp")
    orig = Image.open("C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png")
    #orig1 = Image.open("C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp")
    #orig = Image.open("/Users/wangyunqi/Desktop/屏幕快照 2018-04-14 下午3.15.30.bmp")
    #/Users/wangyunqi/Desktop/屏幕快照 2018-04-14 下午3.12.12.png


    img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    print(img)
    #a.A()
    #img=250 - img


    # loading astronaut image
    #img = skimage.data.astronaut()

    #img = tupian()

    # perfom selective search
    #img_lbl, regions = selectivesearch.selective_search(img, scale=0.6, sigma=0.8, min_size=120)
    img_lbl, regions = selectivesearch.selective_search(img, scale=0.9, sigma=0.6, min_size=120)
    #img_lbl, regions = selectivesearch.selective_search(img, scale=0.9, sigma=0.6, min_size=120)


    #img_lbl, regions = selectivesearch.selective_search(img, scale=1.0, sigma=0.8, min_size=50)
    i=0
    j=100
    m=0
    n=100
    a=[0]
    b=[0]
    
    candidates = set()
    for r in regions:
        print("asfds--->")
        print(r['labels'])
        print(r)
        j=i
        flag1=100

        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 1:
            continue
        if r['size'] >30000:
            continue

        # distorted rects
        x, y, w, h = r['rect']
        i=x
        m=y
        
        a.append(x)
        b.append(y)
        new_bijiao(a,i,flag1)
        print("\n flag1:")
        print(flag1)
        if flag1==1:
            continue
        flag1=new_bijiao(b,i,flag1)
        print(flag1)
        if flag1==1:
            continue

        
        if abs(i-j)<5:
            continue
        if abs(m-n)<5:
            continue
       

        if w<10:
            continue
        if h<10:
            continue


        
       

        #if w / h > 1.2 or h / w > 1.2:
        #    continue
           
         
        candidates.add(r['rect'])
        #print(r['rect'])
        
        box=(x,y,x+w,h+y)
        #print('===__--===\n')
        #元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
        #print(box)
        #print('===__--===\n')
        
        


        #t=orig.crop(box)
        t=orig.crop(box)
        #t = ImageGrab.grab(box)
        t.save('F:\\丽丽毕设\\所有暂存文件\\haha2\\'+str(num)+".bmp")
        num=num+1
        



    
        

        

    # draw rectangles on the original image
    
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    
    #ax.imshow(img)
    
    ax.imshow(orig)
    c_num=0
    
    for x, y, w, h in candidates:

        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)
        c_num=c_num+1


    print("==========\n")
    print(candidates)

    print("==========\n\n")
    print(regions)
    print("==========\n\n")
    print(num)
    print(c_num)
    i=1
    '''
    for r in regions:
        print (i)
        i=i+1
        print (r['rect'])
        print('\n')
    
    print("hahahahahahah:\n")
    print(a)
    print("\n")
    print(b)
    bj=[]

    bijiao(a,bj)
    print("比较:")
    print(bj)
    '''
   
    plt.show()

    
    



if __name__ == "__main__":
    main()
