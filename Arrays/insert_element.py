import array

arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)

arr.insert(2, 6)  # Insert 6 at index 2
print(arr)

arr.insert(0, 7)  # Insert 7 at index 0
print(arr)

# Using numpy
import numpy as np

arr_np = np.array([1, 2, 3, 4, 5])
print(arr_np)

arr_np = np.insert(arr_np, 2, 6)  # Insert 6 at index 2
print(arr_np)

arr_np = np.insert(arr_np, 0, 7)  # Insert 7 at index 0
print(arr_np)