import matplotlib.pyplot as plt
x= ["python","java","c++","javascript"]
y=[85,70,60,82]
z=[20,30,40,50]
plt.xlabel("languages", fontsize=20, color='r')
plt.ylabel("No.",fontsize=20,color='b')
plt.title("aryan")
c=["y","b","m","g"]
plt.bar(x,y,width=0.5,color="c",align="center",label="popularity")
plt.bar(x,z,width=0.5,color="r",align="center",label="popularity1")
plt.legend()
plt.show()