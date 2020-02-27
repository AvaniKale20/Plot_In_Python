import matplotlib.pyplot as plot
# from matplotlib import pyplot

# create one vector which contain coordinate for x-axis
# Define the x-axis and corresponding y-axis values as lists.
# x asix value
x=[1,2,3]

# y axis value
# create 2nd vector which contain coordinate for y-axis
y=[2,4,1]

# Give a name to x-axis and y-axis using .xlabel() and .ylabel() functions.
# naming the x axis
plot.xlabel('x - axis')
# naming the y axis
plot.ylabel('y - axis')
# title for a graph-Give a title to your plot using .title() function.
plot.title('My first graph!')
# plotting the points-
plot.plot(x,y)
# function show the plot-to view your plot, we use .show() function
plot.show()