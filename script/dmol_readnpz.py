#!/home/weiwei/psi4conda/bin/python3
#241022 for lxy

import numpy as np
import re

#data = np.load('merged_file.npy',allow_pickle=True)
data = np.load('Merge.npz',allow_pickle=True)

output_file_path = "outputnpz_data.txt"
with open(output_file_path, 'w') as file:
    for line in data:
        file.write(str(line) + '\n')

print("Data has been written to", output_file_path)

