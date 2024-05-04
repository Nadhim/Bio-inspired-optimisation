import random

a = ['a','b','c']

weight = [10,1,1]


d=[]

for i in range(1000):
    d.append(random.choices(a,weight)[0])
print(d)

for i in a:
    print(d.count(i)/1000)

# import math

# print(0.9534*math.sin(10*math.pi*0.9534)+2.0)

