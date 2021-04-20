import numpy as np

a = np.arange(1, 10).reshape(3, 3)
print(a)
b = np.arange(10, 19).reshape(3, 3)
print(b)

c = np.dot(a, b)

sum = np.sum(c)

print(sum)


sum1 = np.sum(a)

print(sum1)