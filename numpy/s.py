
import numpy as np
import matplotlib.pyplot as plt

x=np.zeros((21,1))
#print(x)

y=np.zeros((21,1))

y_max=20
def steep(inc):
    for i in range(0,11):
        x[10-i] = -i*(inc)
        x[10+i] = i*(inc)
        y[10-i] = y_max/2**i
        y[10+i] = y_max/2**i
steep(0.1)
print(x)


plt.plot(x,y)
plt.show()
