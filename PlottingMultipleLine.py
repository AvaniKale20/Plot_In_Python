import matplotlib.pyplot as plt
# Coordinate for line one
x1=[1,3,6]
y1=[2,5,8]
# Coordinate for line two
x2=[2,5,8]
y2=[1,3,6]
# ploting the line for one
plt.plot(x1,y1,label="line 1")
plt.plot(x2,y2,label="line 2")

plt.title("Two line on same graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
# The small rectangular box giving information about type of line and its color is called legend.
# We can add a legend to our plot using .legend() function.
plt.legend()
plt.show()