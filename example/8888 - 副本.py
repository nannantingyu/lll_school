'''
# -*- coding: utf-8 -*-
import os
 
 
def listfiels(path):
    path = path.replace("\\", "/")
    mlist = os.listdir(path)
 
    for m in mlist:
        mpath = os.path.join(path, m)
        if os.path.isfile(mpath):
            pt = os.path.abspath(mpath)
            # print pt.decode("gbk").encode("utf-8") #会报错
            print ('pt')
        else:
            pt = os.path.abspath(mpath)
            print ('pt')
            listfiels('pt')
 
 
listfiels("C:\\Users\\Administrator\\Desktop\\aa\\")
  '''

#import os
#os.system("C:\\Users\\Administrator\\Desktop\\aa\\")  
'''
import os                                             #导入操作文件夹需要的os模块  
  
def linkFilesInDirs(rootDir, outputFile):             #定义函数，参数为要操作的根文件夹，和最后要输出的新文件  
    fw=open(outputFile, 'w')                          #以写方式打开文件  
    for dirName in os.listdir(rootDir):               #列出rootDir目录下的所有文件夹和文件，并遍历结果  
        if os.path.isdir(dirName):                    #判断该结果是否是文件夹  
            print ('process in dir: %s')%dirName  
            for fileName in os.listdir(dirName):      #如果该结果是文件夹，则列出其目录下的所有文件并遍历  
                if not os.path.isdir(fileName):       #判断是否是文件，只有是文件才被处理  
                    fr=open(os.path.join(dirName,fileName), 'r') #以读的方式打开该文件  
                    for eachLine in fr:               #遍历该文件的每一行  
                        line = eachLine.strip().decode('utf-8', 'ignore')  
                        outStr = line  
                    fw.write(outStr.strip().encode('utf-8') + '\n') #将内容写入到一个新的文件中  
                    fr.close()  
    fw.close()  
  
linkFilesInDirs('myDir', 'C:\\Users\\Administrator\\Desktop\\aa\\')   
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# -*- coding:utf-8 -*-



'''
import re
import os
import time
#str.split(string)分割字符串
#'连接符'.join(list) 将列表组成字符串
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
            i+=1 #注意这里的i是一个陷阱
        #或者
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        #if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用

img_dir = 'C:\\Users\\Administrator\\Desktop\\aa\\'
img_dir = img_dir.replace('\\','/')
#f = open('img_dir')
#raw = f.read()

start = time.time()
i = 0
change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))
'''


import os  
path = "C:\\Users\\Administrator\\Desktop\\aa" #文件夹目录  
files= os.listdir(path) #得到文件夹下的所有文件名称 
print(files)
s = []  
for file in files: #遍历文件夹  
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开  
        f = open(path+"/"+file); #打开文件  
        iter_f = iter(f); #创建迭代器  
        str = ""  
          for line in iter_f: #遍历文件，一行行遍历，读取文本  
              str = str + line  
          s.append(str) #每个文件的文本存到list中  
print(s) #打印结果 