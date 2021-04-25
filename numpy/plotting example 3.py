import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y_1 = [10, 20, 30, 40, 50]


plt.plot(x,y_1,linestyle = '--',marker = '.')



y_2 = [25, 30, 45, 90, 65]

plt.plot(x,y_2,linewidth = 3,color = 'k')

plt.grid(True)

plt.show()
