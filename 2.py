import numpy as np

np.random.seed(312)

n = 20

m=0

for i in range(0, n):
    a=np.random.choice([1, 2, 3, 4, 5], size=2)

    print(a, a[0] - a[1]>=2)


    if a[0]- a[1] >=2:
        m+=1


p=m/n
print(p)

