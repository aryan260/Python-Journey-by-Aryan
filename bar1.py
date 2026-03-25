import matplotlib.pyplot as plt
import numpy as np

x= ["python","java","c++","javascript"]
y=[85,70,60,82]
z=[20,30,40,50]
width=0.2
p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel("languages", fontsize=20, color='r')
plt.ylabel("No.",fontsize=20,color='b')
plt.title("aryan")
# c=["y","b","m","g"]

plt.bar(p,y,width,color="c",align="center",label="popularity")
plt.bar(p1,z,width,color="r",align="center",label="popularity1")

plt.xticks(p+width/2,x,rotation=90)
plt.legend()
plt.show()