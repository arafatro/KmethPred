# -*- coding: utf-8 -*-
"""vectorgenerate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AEy4AczTjMtAkulrIc9ieaA3dPYX5a3W
"""

# from google.colab import drive
# drive.mount('/content/drive')

import numpy as np
import pandas as pd
import sys
import numpy.ma as ma
import os

folder = 'C:/feature/Advance/Nea'
filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]
Length = (len(filepaths))

file = 'C:/feature/Advance/Nea/PSSM.'

res_vec = np.zeros((Length,210))
for v in range(1, Length+1):
    num = str(v)
    pos = file + num
    
    positive = []
    with open(pos, 'r', encoding="utf-8",errors='ignore') as f:
        for line in f:
            positive.append(line.split())


        
    data = positive[2:-6]
    #positive[-7]

    df = pd.DataFrame(data)
    df.head()

    df = df.iloc[1:,2:22]

    XX = np.asarray(df)
    YY = np.ascontiguousarray(XX, dtype=np.int32)

    Transpose = YY.transpose()  #transpose pssm matrix [20*L]

    M = np.zeros([Transpose.shape[0], Transpose.shape[1]])

    for i in range(Transpose.shape[0]):
        for j in range (Transpose.shape[1]):
            M[i, j] = (Transpose[i,j] - np.mean(Transpose[i, :])) / np.std(Transpose[i, :])

    transpose_M = M.transpose()


    result = np.dot(M, transpose_M)



    lower_tril = np.tril(result)

    il1 = np.tril_indices(20)
    remove_upper_value = lower_tril[il1]


    Vector = np.ravel(remove_upper_value)
    
    
    
    array_vec = np.array(Vector)
    res_vec[v-1] = array_vec
    
    
    
    np.savetxt('INPUT1.csv', res_vec, delimiter=',', fmt='%.18e')