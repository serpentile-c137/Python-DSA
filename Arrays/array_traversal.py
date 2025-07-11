from array import *

arr = array('i', [1, 2, 3, 4, 5])
print(arr)
arr1 = array('d', [1.1, 2.2, 3.3, 4.4, 5.5])
print(arr1)

def array_traversal(arr):
    for i in arr:
        print(i)

array_traversal(arr) # complexity O(n)