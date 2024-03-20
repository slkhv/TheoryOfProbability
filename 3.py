import numpy as np

np.random.seed(312)

n=100000

m=0

for i in range(0,n):

h = np.random.choice ([0,1,2,3,4,5,6,7,8,9],

size = 6,replace=False)

if h[0]+h[1]+h[2]+h[3]+h[4]+h[5] == 21 :

m+=1

p=m/n

print(p)