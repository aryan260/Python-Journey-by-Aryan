import matplotlib.pyplot as plt

x=[10,20,30,40,50]
area1=[10,20,30,40,50]
area2=[10,50,30,40,50]
area3=[10,80,30,40,50]
l=["area1","area2","area3"]

plt.stackplot(x,area1,area2,area3,labels=l,colors=["r","g","y"])
plt.legend(loc=2)
plt.title("Python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()