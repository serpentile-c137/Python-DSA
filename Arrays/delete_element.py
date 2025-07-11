from array import *

arr = array('i', [1, 2, 3, 4, 5, 6])
print(arr)

def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        return "Index out of bounds"
    arr.remove(arr[index])
    # Alternatively, you can use the following line to delete by index:
    # del arr[index]
    return arr

print(delete_element(arr, 2))  # Output: array('i', [1, 2, 4, 5, 6])
print(delete_element(arr, 5))  # Output: Index out of bounds