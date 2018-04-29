'''
from skimage import data,filters
import matplotlib.pyplot as plt
import cv2

#image = data.camera()
image = cv2.imread('C:\\Users\Administrator\\Desktop\\lily\\yuantu.bmp',0) #直接读为灰度图像
thresh = filters.threshold_li(image)   #返回一个阈值
dst =(image <= thresh)*1.0   #根据阈值进行分割

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()

#encoding:utf-8

#
#自适应阈值化处理
#

#!/usr/bin/python  
# -*- coding: UTF-8 -*-  
  
import tkinter
from tkinter import filedialog 
   
root = tkinter.Tk()
root.title('应用程序窗口')        #窗口标题  
root.resizable(False, False)    #固定窗口大小  
windowWidth = 800               #获得当前窗口宽  
windowHeight = 500              #获得当前窗口高  
screenWidth,screenHeight = root.maxsize()     #获得屏幕宽和高  
geometryParam = '%dx%d+%d+%d'%(windowWidth, windowHeight, (screenWidth-windowWidth)/2, (screenHeight - windowHeight)/2)  
root.geometry(geometryParam)    #设置窗口大小及偏移坐标  
root.wm_attributes('-topmost',1)#窗口置顶  
  
#label文本  
label_text = tkinter.Label(root, text = '文本');  
label_text.pack();  
  
#label图片  
img_gif = tkinter.PhotoImage(file = 'C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.bmp')  
label_img = tkinter.Label(root, image = img_gif)  
label_img.pack()  
  
#不带图button  
button = tkinter.Button(root, text = '不带图按钮')  
button.pack()  
  
#带图button，image  
button_img_gif = tkinter.PhotoImage(file = 'button_gif.gif')  
button_img = tkinter.Button(root, image = button_img_gif, text = '带图按钮')  
button_img.pack()  
  
#带图button，bitmap  
button_bitmap = tkinter.Button(root, bitmap = 'error', text = '带图按钮')  
button_bitmap.pack()  
  
root.mainloop()  
'''
import matplotlib.pyplot as plt
from PIL import Image
import tkinter
from tkinter import filedialog 

root = tkinter.Tk() 
scrollbar = tkinter.Scrollbar(root)
scrollbar.pack( side = 'right', fill='y' )

mylist = tkinter.Listbox(root, yscrollcommand = scrollbar.set ,width=100)
for line in range(100):
   mylist.insert('end', "This is line number " + str(line))

mylist.pack( side = 'left', fill = 'both' )
scrollbar.config( command = mylist.yview )

'''  
label_text = tkinter.Label(root,text = 'welcome to jcodeer.cublog.cn',bg = 'yellow',width = 40,height = 3,wraplength = 80,justify = 'left').pack()
#居中对齐，文本居左
label_text = tkinter.Label(root, text = '文本');  
label_text.pack();  
'''
img_png = tkinter.PhotoImage(file = 'C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png')  
label_img = tkinter.Label(root, image = img_png)  
label_img.pack()
img_png1 = tkinter.PhotoImage(file = 'C:\\Users\\Administrator\\Desktop\\lily\\1.png')  
label_img = tkinter.Label(root, image = img_png1)  
label_img.pack()
#bm = tkinter.BitmapImage(file='C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.bmp')


#label = Label(root,bitmap=bm)
#label.bm = bm
#label.pack()
root.mainloop()
'''
class ScrollText:
    def __init__(self):
 
        # 窗口和标题
        window = tkinter.Tk()
        window.title("滚动条示例")
 
        # 创建一个纵向滚动的滚动条,打包到窗口右侧，铺满Y方向
        scrollbar = tkinter.Scrollbar(window,orient='vertical')#orient默认为纵向
        scrollbar.pack(fill='y', side='right')
 
        # 打包一个文本域到窗口，y方向滚动文本的监听丢给滚动条的set函数（文本域主动关联滚动条）
        text = tkinter.Text(window,width=100, yscrollcommand=scrollbar.set)
        text.pack()
 
        # 拉动滚动条时，改变文本域在y方向上的视图（滚动条主动关联文本域）
        scrollbar.config(command=text.yview)
 
        # 消息循环
        window.mainloop()
    
ScrollText()
