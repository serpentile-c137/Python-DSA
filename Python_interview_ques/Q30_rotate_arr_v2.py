def rotate_array(arr,k):
    n = len(arr)
    temp = arr[-k:]  # Get the last k elements
    for i in range(n-1, k-1, -1):
        arr[i] = arr[i-k]
    for i in range(k):
        arr[i] = temp[i]
    return arr 

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_arr = rotate_array(arr, k)
print(rotated_arr) # Output: [5, 6, 7, 1, 2, 3, 4]