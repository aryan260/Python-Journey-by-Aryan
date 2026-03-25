import matplotlib.pyplot as plt

x=[10,20,30,40]
y=["c","c++","java","python"]
ex=[0.4,0.0,0.2,0.0]
c=["red","blue","green","yellow"]

plt.pie(x, labels=y, explode=ex, colors=c,autopct="%5.3f%%",shadow="true",radius=1.0,labeldistance=1.2,startangle=180,textprops={"fontsize":15},counterclock="false",wedgeprops={"linewidth":2,"edgecolor":"magenta"},center=(10,0))
plt.grid()
plt.show()