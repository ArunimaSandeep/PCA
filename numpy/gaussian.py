import math as ma
import numpy as np
import matplotlib.pyplot as plt
def gaussian(m,s=5,i=50):
    x_min = m-2*s
    x_max = m+2*s
    P=[]
    X=[]
    for x in np.linspace(x_min,x_max,50):
        p = (i)*ma.exp(-(x-m)**2/(2*s**2))
        P.append(p)
        X.append(x)
    print(P)
    return P,X

M =[]


P,X = gaussian(300)

plt.scatter(X,P)
plt.show()
# a = function(3,4)
# print(a)
