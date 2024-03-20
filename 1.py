import numpy as np

np.random.seed(312)

n = 20

m=0

for i in range(0, n):
    a=np.random.choice([1, 2, 3], p=[.5, .5], size=10)
    b=np.random.choice([0, 1], p=[.5, .5], size=10)

    if sum(a)==sum(b):
        m+=1


p=m/n
print(p)

