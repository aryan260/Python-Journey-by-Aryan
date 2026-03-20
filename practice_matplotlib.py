import matplotlib.pyplot as plt
import random
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y=[x**2 for x in x] 

plt.plot(x,y)
plt.grid()
plt.show()
##########################

x=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
y=[100,200,500,300,400,600,150]

plt.title("Data hai kisi chiz ka")
plt.xlabel('Days of the week')
plt.ylabel('Temperature in kelvin')
plt.legend()
plt.plot(x,y,label='Temperature',color='red')
plt.show()

##############################
x=[1,2,3,4,5,6,7,8,9,10]
y1=[x for x in x]
y2=[x**2 for x in x]
plt.plot(x,y1,color='red',label='linear')
plt.plot(x,y2,color='blue',label='quadratic')
plt.legend()
plt.show()

##############################
x=np.random.randint(10,30,(20))
y=np.random.randint(10,30,(20))
plt.scatter(x,y)
plt.show()

##############################
x=["ankush","atharva","rajan","john","doe","emily","sophia","oliver","liam","ava"]
y=[np.random.randint(60,100,(10))]

plt.title("Marks of students")
plt.grid(True)
plt.scatter(x,y)
plt.show()