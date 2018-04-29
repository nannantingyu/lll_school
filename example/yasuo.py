 # -*- coding: UTF-8 -*-  

from PIL import Image
import os as _os
import os.path
import sys
import a 

f_name=[]

def file_name(file_dir):   
	aaa=
    for dirs in os.walk(file_dir):  
        
        print(dirs) #当前路径下所有子目录 
        aaa=dirs
        print("\n") 
        f_name=dirs
      

file_name("/Users/wangyunqi/Desktop/丽丽毕设/数据集/数据集")

#f_name=dirs
print(f_name)
print(aaa)



'''
path = sys.argv[1]
small_path = (path[:-1] if path[-1]=='/' else path) +'_small'
if not os.path.exists(small_path):
    os.mkdir(small_path)
for root, dirs, files in os.walk(path):
    for f in files:
        fp = os.path.join(root, f)
        img = Image.open(fp)
        w, h = img.size
        img.resize((w/2, h/2)).save(os.path.join(small_path, f), "JPEG")
        print fp
        '''