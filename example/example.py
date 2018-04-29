# -*- coding: utf-8 -*-
from __future__ import (
    division,
    print_function,
)
import sys
from importlib import reload

reload(sys)

#sys.setdefaultencoding('utf-8')

'''
import ha
if __name__ == "__main__":
    B.openfiles2(x,y)
    '''
import selectivesearch
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
import ha

def main():
    print()
def mn():
    num=0
    print (skimage)
    #print(skimage.data.astronaut())
    #print(tupian())
    print("-------------\n")
    #/Users/wangyunqi/Desktop/丽丽毕设/2.bmp
    #img=imread("C:\\Users\\Administrator\\Desktop\\lily\\a1.bmp")
    img=imread("C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png")
    orig = Image.open("C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png")
    orig1=Image.open("C:\\Users\\Administrator\\Desktop\\lily\\yuantu.png")
    #orig = Image.open("C:\\Users\\Administrator\\Desktop\\lily\\a1.bmp")

    img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)  #将预处理的图片转换成RGB格式

    print(img)
   # a.A()
    #img=250 - img


    # loading astronaut image
    #img = skimage.data.astronaut()

    #img = tupian()

    # perfom selective search
    img_lbl, regions = selectivesearch.selective_search(img, scale=0.9, sigma=0.6, min_size=120)  #调用selective_search算法
    #img_lbl, regions = selectivesearch.selective_search(img, scale=800, sigma=0.9, min_size=150)  #调用selective_search算法
    
    #img_lbl, regions = selectivesearch.selective_search(img, scale=1.0, sigma=0.8, min_size=50)

    #识别图像的范围
    candidates = set()
    for r in regions:
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
        if w<10:
            continue
        if h<10:
            continue

        #if w / h > 1.2 or h / w > 1.2:
        #    continue
           
         
        candidates.add(r['rect'])
        print(r['rect'])  #无
        
        #裁剪
        box=(x,y,x+w,h+y)
        print('===__--===\n')
        #元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
        print(box)
        print('===__--===\n')
        
        t=orig1.crop(box)
        #t = ImageGrab.grab(box)
        ha.path2
        print(ha.path2)
        t.save(ha.path2+"\\"+str(num)+".png")
        #t.save("F:\\丽丽毕设\\所有暂存文件\\haha2\\"+str(num)+".png")
        
        num=num+1
   

    # draw rectangles on the original image
    
    #画框
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
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

    
    '''
    plt.show()

if __name__ == "__main__":
    main()
