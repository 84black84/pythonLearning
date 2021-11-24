import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6])
# print(a[0])

array_1 = np.array([[1, 2, 7], [3, 4, 8]])
array_2 = np.array([[1, 2], [3, 9], [4, 16]])


res = np.dot(array_1, array_2)
# print(res)

array = np.array([1,2,3])
array1 = np.array([4,5,6])
array2 = np.dot(array, array1)
print(array2)

help(np.dot)


