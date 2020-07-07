import random
import matplotlib.pyplot as plt

x=[]
y=[]
s=[]

for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    s.append(random.randint(10,100))

print(x)
print(y)
print(s)

plt.scatter(x,y,s=s,c=s,cmap='jet',alpha=0.5)
plt.colorbar()
plt.show()

