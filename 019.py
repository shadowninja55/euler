import numpy as np

M = np.array([[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]])
B = np.repeat(M, 4, axis=0)
B[3, 1] = 29
D = np.insert(np.repeat([B], 25, axis=0).ravel()[:-1], 0, 365)
print(np.sum(np.cumsum(D) % 7 == 6))
