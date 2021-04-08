import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
a=[[6.8,50],[2.87,46],[3.8,30],[4.9,29],[5.53,38]]


l = []
i = []



for j in range(0,len(a)):
    l.append(float(a[j][0]))
    i.append((a[j][1]))
    # print(i)
# print(l)
# print(i)


for j in range(0,len(l)):
    l[j]=str(l[j])[::-1].find('.')

# print(l)


max = l[0]
for j in range(1, len(l)):
    if l[j] > max:
        max = l[j]
# print(max)

res = 1/10**(max)
# print(res)


def steep(res,a):
    x=np.zeros((21,1))
    y=np.zeros((21,1))
    Intensity = y.copy()
    Lambda = x.copy()
    for ind,k in enumerate(np.array(a)[:,1]):
        for j in range(0,11):
            x[10-j] = -j*(res)
            x[10+j] = j*(res)
            y[10-j] = k/2**j
            y[10+j] = k/2**j
        Intensity = np.hstack((Intensity,y))
        Lambda = np.hstack((Lambda,x+np.array(a)[ind,0]))
    return Lambda[:,1:] , Intensity[:,1:]
Lambda , Intensity = steep(res,a)

# print(Lambda)
# print(Intensity)

# print(Intensity[0,:])

lambda_1 = np.argsort(Lambda[0,:])


# for i in range(0,len(lambda_1)):
Intensity = Intensity[:,lambda_1].copy()
Lambda = Lambda[:,lambda_1].copy()

# print(Intensity)

def points(z):

    divisions=((Lambda[20][z-1]-Lambda[0][0])/res)+1
    return int(divisions)

p=points(len(a))
# print(p)


spec = np.zeros((1,p))
# print(spec.shape)

M=[]
N=[]
for i in range(0,len(a)):
    m=int((Lambda[0][0]-Lambda[0][i])/res)

    M.append(abs(m))

    # n=p-int(((Lambda[20][len(a)-1]-Lambda[20][i]))/res)
    N.append(abs(m)+21)


# print(M)
# print(N)

Intensity_t=np.transpose(Intensity)
# print(Intensity_t.shape)
#
#
Intensity_f=Intensity_t.reshape(1,-1)
# print(Intensity_f.shape)
#
c=[]

count =0
while (count < len(Intensity_f)+1):

    c.append(count)
    count = count + 20
# print(spec[0,5:10].shape)
#
# print(M)
# print(N)

for i in range(0,4):
    print(M[i],N[i])
    # print(spec[0,M[i]:N[i]].shape)
    spec[0,M[i]:N[i]]=spec[0,M[i]:N[i]]+Intensity_t[i,:]

print(spec.shape)
x = np.array([i for i in range(0,p)])
print(x.shape)

total = np.vstack((x.reshape(1,-1),spec))
print(total.T.shape)
total = total.T
np.savetxt("data.csv", total, delimiter=",")
# sns.lineplot(x.reshape(1,-1),spec)
# plt.show()












# for i in range(0,5):
#     plt.plot(Lambda[:,i],Intensity[:,i])
# plt.show()
