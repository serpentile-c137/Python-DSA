import array

arr = array.array('i')
print(arr)

arr1 = array.array('i', [1, 2, 3, 4, 5])
print(arr1)

# using numpy
import numpy as np
arr2 = np.array([], dtype=int)
print(arr2)

arr3 = np.array([1, 2, 3, 4, 5])
print(arr3)