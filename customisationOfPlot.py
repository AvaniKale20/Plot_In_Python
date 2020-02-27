import matplotlib.pyplot as plt
# import matplotlib.colors

x=[2,4,6,1,8]
y=[1,3,4,6,7]

plt.plot(x,y, color='green',linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
