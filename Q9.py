import numpy as np

#-----------------------------------------
#a = np.array([1, 2, 3, 4, 5])
#b = np.array([5, 6, 7, 8, 9])
#-----------------------------------------
""" attempt #1

x = np.array([[5], [5, 6, 7, 8, 9]])

sum = np.sum(x)

print(sum)
"""

a = np.array ([5])
b = np.array ([5])
c = np.array ([6])
d = np.array ([7])
e = np.array ([8])
f = np.array ([9])


sum = np.sum((a,b,c,d,e,f))

print(sum)

#Cant lie I feel proud after this but im sure there was maybe a shorter way to complete it?