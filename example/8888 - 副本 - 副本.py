# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
import tkinter         # 导入Tkinter模块
from PIL import Image, ImageTk

root = tkinter.Tk()

canvas1 = tkinter.Canvas(root,
    width = 200,      # 指定Canvas组件的宽度
    height = 200,      # 指定Canvas组件的高度
    bg = 'white')

canvas = tkinter.Canvas(root,
    width = 200,      # 指定Canvas组件的宽度
    height = 200,      # 指定Canvas组件的高度
    bg = 'white')      # 指定Canvas组件的背景色
im = tkinter.PhotoImage(file='C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png')     # 使用PhotoImage打开图片
#image = Image.open("C:\\Users\\Administrator\\Desktop\\lily\\lvbo1.png")
#im = ImageTk.PhotoImage(image)
#canvas1 .create_image(0,0,anchor='nw',image = im)      # 使用create_image将图片添加到Canvas组件中
canvas.create_image(0,0,anchor='nw',image = im)      # 使用create_image将图片添加到Canvas组件中
canvas.create_text(0,0,       # 使用create_text方法在坐标（302，77）处绘制文字
   text = 'Use Canvas'      # 所绘制文字的内容
   ,fill = 'gray')       # 所绘制文字的颜色为灰色
canvas.create_text(300,75,
   text = 'Use Canvas',
   fill = 'blue')
canvas.pack(side='left')
canvas1.pack(side='left')
         # 将Canvas添加到主窗口
root.mainloop()