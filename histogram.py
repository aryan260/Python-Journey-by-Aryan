import matplotlib.pyplot as plt
import numpy as np
import random

#x=np.random.randint(10,60,(50))
#print(x)
no=[45, 51, 23, 29, 28, 15, 27, 27, 20, 44, 28, 52, 47, 37, 35, 46, 22, 12, 36, 11, 51, 36, 14, 44,
 10, 27, 53, 22, 48, 54, 19, 43, 32, 30, 32, 43, 29, 36, 38, 27, 16, 36, 50, 41, 33, 40, 25, 36,
 10, 36]

l=[10,20,30,40,50,60]
plt.hist(no,color="red",edgecolor="green",bins=l,orientation="vertical",rwidth=0.8,log=True,label="phenomenon")
plt.grid()
plt.xlabel("numbers")
plt.ylabel("range")
plt.axvline(45,color="r",label="line")
plt.title("Histogram practice")
plt.legend()

plt.show()