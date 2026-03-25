import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70]
x1=[10,40,90,16,36,49]

y=[x,x1]

plt.boxplot(y,labels=["Python","c++"],showmeans=True,sym=" ",boxprops=dict(color="r"),capprops=dict(color="r"),whiskerprops=dict(color="g"))

#plt.boxplot(x1,labels=["Python"],showmeans=True,sym=" ",boxprops=dict(color="r"),capprops=dict(color="r"),whiskerprops=dict(color="g"))

plt.show()
