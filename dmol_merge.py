#!/home/weiwei/psi4conda/bin/python3
#!Jackeyli@240715
#workflow--readme
#1.读取当前文件夹下所有以 dmol_3 开始的文件夹下 .outmol 结尾的文件
#2.读取原子个数，元素数量，输出结构，KS能量。
#4.整合读取。

import os
import sys
import numpy as np



#current_directory = os.getcwd() #获取当前工作目录
current_directory = input("input your path, please: ",).strip()
absolute_path = os.path.abspath(current_directory)
folder_name = os.path.basename(absolute_path)
if not os.path.isdir(current_directory):
    print("提供的路径无效，请检查路径并重新运行程序。")
    sys.exit(1)

all_data = np.array([])

# 遍历文件夹中的所有 .npy 文件
for file_name in os.listdir(current_directory):
    if file_name.endswith('.npy'):
        # 读取每个 .npy 文件的数据
        data = np.load(os.path.join(current_directory, file_name), allow_pickle = True)
        # 使用 np.append() 方法将数据添加到all_data中
        all_data = np.append(all_data, data)

# 保存整合后的数据到一个新的 .npy 文件中
np.save(folder_name + '.npy', all_data)