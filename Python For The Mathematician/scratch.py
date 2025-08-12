import numpy as np

A = np.array([[[1,2]],[[3,4]]])
B = np.array([[[0,0]],[[7,7]]])
C = np.concatenate([A,B], axis = 0)
D = np.concatenate([A,B], axis = 2)
A.append(B)
print(C)
print(D)