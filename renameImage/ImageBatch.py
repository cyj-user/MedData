# -*- coding: utf-8 -*- 
import os
import shutil

def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件

def specific_file_name(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.dcm':
                L.append(os.path.join(root, file))
    return L


path = "/Users/daven/个人资料/项目/肖晟老师/MedData/MedData/dr_sample/"
# file_name(path)
c = specific_file_name(path)
pos = 0
for cc in c:
	# shutil.move("name1","name2")
	shutil.move(cc,"/Users/daven/个人资料/项目/肖晟老师/MedData/MedData/" + str(pos) + ".dcm")
	pos+=1