
 # -*- coding: UTF-8 -*-  

from __future__ import (
    division,
    print_function,
)
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



img_try = cv2.imread('F:\\丽丽毕设\\数据集\\数据集\\111.bmp',0) 
img = Image.open("F:\\丽丽毕设\\数据集\\数据集\\111.bmp")
#img1 = Image.open("F:\\丽丽毕设\\所有暂存文件\\new\\3.bmp")
#print(img)
print('\n-------\n')
#print(img1)

#改变图片大小
(x,y) = img.size
x_s=512
y_s=512
img=img.resize((x_s,y_s),Image.ANTIALIAS)



scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\img.bmp', img)

im1 = array(img.convert('L'))
img_new=im1
#cv2.imwrite('C:\\Users\\Administrator\\Desktop\\lily\\img.bmp',img1)

#img1 = Image.open("C:\\Users\\Administrator\\Desktop\\lily\\2.bmp")
#scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\img2.bmp', img1)
#print(img)
#img = cv2.imread('F:\\丽丽毕设\\2.bmp',0) #直接读为灰度图像
'''for i in range(5): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255

'''

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
				#imm[i][j]=0

#plt.subplot(1,3,1),plt.imshow(imm,'hahah')
for i in range (10):

	imgg = cv2.medianBlur(imm,5)


plt.subplot(1,2,1),plt.imshow(imm,'gray')
scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\sanzhi.bmp', imm)
plt.subplot(1,2,2),plt.imshow(imgg,'gray')#默认彩色，另一种彩色bgr
scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\lvbo.bmp', imgg)

#cv2.imshow('img',img)
#scipy.miscv2.imwrite("C:\\Users\\Administrator\\Desktop\\lily\\aa1111.bmp",img)c.imsave("C:\\Users\\Administrator\\Desktop\\lily\\hahahahhahaha(5*5) 8.bmp", img);

plt.show()
