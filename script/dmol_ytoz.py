#!/home/weiwei/psi4conda/bin/python3
#!Jackeyli@240715

import numpy as np
import os

npy_files = [f for f in os.listdir() if f.endswith('.npy')]

for npy_file in npy_files:
    npz = np.load(npy_file, allow_pickle=True)
    npz_file = npy_file.replace('.npy', '.npz')
    np.savez(npz_file, npz=npz)
