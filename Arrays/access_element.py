from array import *

arr = array('i', [1, 2, 3, 4, 5])
print(arr)

def access_element(arr, index):
    if index < 0 or index >= len(arr):
        return "Index out of bounds"
    return arr[index]

print(access_element(arr, 2))  # Output: 3
print(access_element(arr, 5))  # Output: Index out of bounds