from array import *

arr = array('i', [1, 2, 3, 4, 5])
print(arr)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr, 3))  # Output: 2
print(linear_search(arr, 6))  # Output: -1