import matplotlib.pyplot as plt
# import numpy as np

coordinates = [[1,5],[2,4],[3,3]]
print(coordinates)
# print(coordinates[1][0])
# #
#
x = []
y = []

for i in range(0,len(coordinates)):
    print(i)

for i in range(0,len(coordinates)):
    x.append(coordinates[i][0])
    y.append(coordinates[i][1])


plt.plot(x,y)
plt.show()
