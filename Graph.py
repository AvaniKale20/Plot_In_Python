import matplotlib.pyplot as plt
# x-coordinates of left sides of bars
left=[1,2,3,4,5]

# height of the bar
height=[5,10,30,50,10]
# label for bar
tick_label = ['one', 'two', 'three', 'four', 'five']
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.5, color = ['red', 'green'])
plt.show()
