import numpy as np

np.random.seed(3113948)

n = 12
n2 = 18

twelve = 0
eighteen = 0

for i in range(0, 2000):

    a = np.random.choice([1, 2, 3, 4, 5, 6], size=12)
    b = np.random.choice([1, 2, 3, 4, 5, 6], size=18)

    m=0

    for i in range(0, 12):

        # if there's 2 elemetns = 6
        if a[i] == 6:
            m+=1

    if (m>=2):
        twelve+=1

    m=0

    for i in range(0, 18):
        if b[i] == 6:
            m+=1

    if (m>=2):
        eighteen+=1

print(twelve)
print(eighteen)

