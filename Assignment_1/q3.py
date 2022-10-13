import random as rnd
import numpy as np


a = []
v = np.random.uniform(0, 1, 100)


# taking two univariate normal distribution with mean 0 , 2 and variance 1 ,8 respectively
for i in np.nditer(v):
    if i <= 0.5:
        a.append(np.random.normal(0, 1))
    else:
        a.append(np.random.normal(2, 8))

mean = np.sum(a)/100.0
b = np.full(100, mean)
c = np.subtract(a, b)
d = np.square(c)
e = np.sum(d)
variance = e/(100-1)

print("estimated mean = ", mean)

print("estimated variance = ", variance)
