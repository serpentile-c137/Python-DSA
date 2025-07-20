def rotate_array(arr,k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    arr[:] = arr[-k:] + arr[:-k]  # Rotate the array in place
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_arr = rotate_array(arr, k)
print(rotated_arr) # Output: [5, 6, 7, 1, 2, 3, 4]