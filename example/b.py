 # -*- coding: UTF-8 -*-  
from __future__ import (
    division,
    print_function,
)
import a
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
__all__=['load']



def load(f, as_grey=False):
    """Load an image file located in the data directory.

    Parameters
    ----------
    f : string
        File name.
    as_grey : bool, optional
        Convert to greyscale.

    Returns
    -------
    img : ndarray
        Image loaded from ``skimage.data_dir``.
    """
    use_plugin('pil')
    return imread(_os.path.join(data_dir, f), as_grey=as_grey)
def erzhi(im,threshold):
	imm=im
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


		return imm				

		
        #return imm

     
def quzao(im):

	return im

       

def main():
	img1=imread("F:\\丽丽毕设\\2.bmp")

	imm = Image.open("F:\\丽丽毕设\\2.bmp") 
	'''
	box=(100,150,250,350)
	print('===\n')
	
	box=(100,200,300,300)
	region = imm.crop(box)
	region.save('C:\\Users\\Administrator\\Desktop\\lily\\111.bmp')
	'''

    
	
	#img1.shape
	im = array(imm.convert('L'))
	print("aaaa\n")
	print(imm.size)


	im2 = 255 - im 
	im3 = (100.0/255) * im +100
	im4 = 255.0 * (im/255.0)**2

	print(im4.shape[0])
	print(im4[1][2])
	print(im4)
	


	plt.figure(num=3, figsize=(12, 7))
	subplot(231)
	title('1')
	plt.imshow(im)
	subplot(232)
	title('2')
	plt.imshow(im2)

	subplot(233)
	title('3')
	plt.imshow(im4)

	subplot(234)

	title('4')
	#二值
	#plt.imshow(gray, cmap = plt.get_cmap('gray')
	im5=erzhi(im4,100)
	scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\sanzhi.bmp', im5)
	
	#for i in range (10):
	#	im111 = cv2.medianBlur(im5,5)
	

		
	#scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\new.bmp', im111)
	

	plt.imshow(im5)


	subplot(235)
	title('5')

	im6=im5
	signal.medfilt(im6,(5,5))
	plt.imshow(im6)
	t=im6
	scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\a1.bmp', t)
	t=erzhi(t,100)
	scipy.misc.imsave('C:\\Users\\Administrator\\Desktop\\lily\\sanzhi11.bmp', t)
	
	#t.save('/Users/wangyunqi/Desktop/预处理/1.bmp')

	subplot(236)
	title('6')
	im7=im6
	edges = filters.sobel(im2)
	#plt.figure(figsize=(60,60)) 
	plt.imshow(edges,plt.cm.binary_r)
	
	#scipy.misc.imsave('/Users/wangyunqi/Desktop/预处理/2.bmp', edges1)


	plt.axis('on')

	#plt.figure(figsize=(60,60)) 
	print("=========/n")
	print(t)

	plt.show()


if __name__ == "__main__":
    main()
