import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7]
no=[2,3,1,4,5,8,6]
no2=[3,4,2,5,6,9,7]
colors=[10,49,30,29,56,20,30 ]
sizes=[500,200,400,800,600,100,1200]
plt.scatter(day,no,c=colors,s=sizes,cmap="viridis",alpha=0.5)
plt.scatter(day,no2,color="r",s=sizes,alpha=0.5)
t=plt.colorbar()
t.set_label("ColorBar",fontsize=15)
plt.title("Scatter plot",fontsize=20)
plt.xlabel("day",fontsize=15)
plt.ylabel("no",fontsize=15)
plt.show()