import matplotlib.pyplot as plt
x=[10,20,30,40,50]
y=[5,15,25,35,45]
s=[100,100,100,100,100]
plt.scatter(x,y,color="r",sizes=s)
plt.title("Scatter Plot Example")
plt.xlabel("x-axis",fontsize=15)
plt.ylabel("y-axis",fontsize=15)
plt.show()