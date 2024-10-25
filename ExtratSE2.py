#!/home/weiwei/psi4conda/bin/python3
#!Jackeyli@240715
#workflow--readme
#1.读取当前文件夹下所有以 dmol_3 开始的文件夹下 .outmol 结尾的文件
#2.读取原子个数，元素数量; 输出结构，KS能量。
#3.整合读取。

import os
import sys
import numpy as np

class read_outputdmol():
    #获取地址
    def __init__(self, outdmol_path: str) -> None:
        self.outdmol_path = outdmol_path #正常获得地址
    #获取原子数
    def atom_number(self) -> str:
        f1 = open(self.outdmol_path)
        lines = f1.readlines() 
        for line in lines:
            if 'N_atoms =' in line:
                global atom_n
                atom_n = int(line.split()[2])
                #print(atom_n,path)
        return atom_n
    #输出离子步优化结构
    def Iron_step(self) -> dict:
        structures = []
        label_etot = []
        atom_n = self.atom_number()
        f1 = open(self.outdmol_path)
        lines = f1.readlines()
        strat_line = False       
        for line in lines:
            for i,line in enumerate(lines):
                #离子步输出结构
                if "df              ATOMIC  COORDINATES (au)" in line: 
                    output_coordinate = lines[i+2:i+2+atom_n] #选择文件结构所在行
                    formatted_output_coordinate = [[ float(x.strip().split()[2]), float(x.strip().split()[3]), float(x.strip().split()[4])] for x in output_coordinate]#整理输入结构格式
                    formatted_output_species = [x.strip().split()[1] for x in output_coordinate]
                    data_dict = {'coordinates':formatted_output_coordinate, 
                                 'species': formatted_output_species,
                                }                  
                    structures.append(data_dict)
                elif  'Total Energy           Binding E                   Time   Iter' in line:
                    ks_energy = lines[i+1].split()[1]
                    if ks_energy.endswith("Ha"):
                        #去掉后两位的Ha， 13.6056923 eV与Ha换算
                        KS_energy = float(ks_energy[:-2]) * 27.212
                    structures.append(KS_energy)
            return  structures                                                
                             
if __name__ == '__main__':
    #current_directory = os.getcwd() #获取当前工作目录
    current_directory = input("input your path, please: ",).strip()
    absolute_path = os.path.abspath(current_directory)
    folder_name = os.path.basename(absolute_path)
    if not os.path.isdir(current_directory):
        print("提供的路径无效，请检查路径并重新运行程序。")
        sys.exit(1)
    folder_prefix = 'dmol3'
    outdmol_paths = []#存储所有文件地址
    data = []
    #获取 dmol_3 开始的文件夹路径
    for root, dirs, files in os.walk(current_directory): #遍历当前文件下
        if os.path.basename(root).startswith(folder_prefix):#以dmol3开始的文件
            file_path = os.path.join(root, "dmol.outmol")#获取output路径
            if os.path.isfile(file_path):
                outdmol_paths.append(file_path)
    #获取.outmol 结尾的文件路径
    with open('output_paths.txt', 'w') as file:  
        for idx,path in enumerate(outdmol_paths,0):
            #获取单个文件路径
            abs_path = os.path.abspath(path)
            outdmol = read_outputdmol(path)
            file.write(f"{idx} {abs_path}\n")  
            data.append(outdmol.Iron_step())   
    data = np.array(data, dtype=object)                        
    np.save( folder_name + '.npy' , data)