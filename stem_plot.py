import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,-3,4,5]

plt.stem(x,y,linefmt='.-.',markerfmt='g*',bottom=3,basefmt='g',label="python")
plt.legend()
plt.show()