#!/home/weiwei/psi4conda/bin/python3
#!Jackeyli@240715
#workflow--readme
#1.读取当前文件夹下所有以 dmol_3 开始的Document下 .outmol 结尾的文件
#2.读取输入结构，获取结构，原子个数，元素数量。


# [Programname] -h
# [Programname] -x [directory_path] -o: 把文件夹下的xxx做处理，输出


import numpy as np
import re


#data = np.load('merged_file.npy',allow_pickle=True)
data = np.load('output.npy',allow_pickle=True)

output_file_path = "output_data.txt"
with open(output_file_path, 'w') as file:
    for line in data:
        file.write(str(line) + '\n')

print("Data has been written to", output_file_path)


#if data.ndim == 0:
#    data = np.array([data.item()])
#    
#
#output_file_path = "output_data.txt"
#with open(output_file_path, 'w') as file:
#    for line in data:
#        file.write(str(line) + '\n')
#
#print("Data has been written to", output_file_path)


#output_file_path = "output_data.txt"
#with open(output_file_path, 'w') as file:
#    if data.ndim == 0:
#        file.write(str(data) + '\n')
#    else:
#        for line in data:
#            file.write(str(line) + '\n')
#
#print("Data has been written to", output_file_path)




