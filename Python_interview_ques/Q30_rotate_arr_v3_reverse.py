def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    reverse(arr, 0, n-1)  # Reverse the entire array
    reverse(arr, 0, k-1)  # Reverse the first k elements
    reverse(arr, k, n-1)  # Reverse the remaining elements
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotated_arr = rotate_array(arr, k)
print(rotated_arr) # Output: [5, 6, 7, 1, 2, 3, 4]