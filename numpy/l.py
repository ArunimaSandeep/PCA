import math as ma
import numpy as np
import matplotlib.pyplot as plt
def lorentzian(x_c,w=5,a=50):
    x_min = x_c-2*w
    x_max = x_c+2*w
    P=[]
    X=[]
    for x in np.linspace(x_min,x_max,50):
        p = (2*a/ma.pi)*(w/(4*(x-x_c)**2+(w**2)))
        P.append(p)
        X.append(x)
    print(P)
    return P,X

P,X = lorentzian(300)
plt.scatter(X,P)
plt.show()
