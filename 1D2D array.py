import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr_2d = np.reshape(arr, (2, 5))

arr_2d[0][0] = 22

print('1D array:')
print(arr)
print('2D array:')
print(arr_2d)