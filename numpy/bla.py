import numpy as np

x =[[6.8,55],[2.87,49],[3.8,33],[4.9,30],[5.56,36]]


fmt='%1.2f','%d'

# Directory='A'

np.savetxt('/home/user/Desktop/numpy/A/a_5.txt', x, fmt=fmt,delimiter=',')
# print("After loading, content of the text file:")
# result = np.loadtxt('a_2.txt')
# print(result)
