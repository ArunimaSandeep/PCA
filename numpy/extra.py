import numpy as np


# #
# a=[5,1,3]
# b=[2,6,4]
# c=[17,8,9]
#
# d = np.vstack((a,b,c))
#
# #print(d)
#
#
#
#
# m=d[:,2]
#
# print(m)
#
# min=print(a[0][0])



# max=2
# min=4
# divisions=-1*(max-min)/0.01
# print(divisions)
#
#
# spec = np.zeros(1,int(divisions))

#
# count = 0
# while (count < 100):
#     count = count + 21
#     print(count)

import numpy as np

ini_array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])

# printing initial arrays
print("initial array", str(ini_array1))

# Multiplying arrays
result = ini_array1.reshape([1, 9])

# printing result
print(result.shape)
