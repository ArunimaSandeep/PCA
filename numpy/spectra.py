import numpy as np
import matplotlib.pyplot as plt



X=[0, 0.02, 0.08, 0.1, 0.2]
y_max = 50

x=np.zeros((21,1))


y=np.zeros((21,1))


def steep(inc):
    for i in range(0,11):
        x[10-i] = -i*(inc)
        x[10+i] = i*(inc)
        y[10-i] = y_max/2**i
        y[10+i] = y_max/2**i
steep(0.01)
# print(x)

for j in X:
    for k in x:
        x=X+x

# if x==X+x:
#     print(x)
# else:
#     print(0)


# plt.plot(x,y)
# plt.show()
