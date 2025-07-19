def checkSortedArray(arr):
    n = len(arr)

    for i in range(0, n-1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
print("Is the array sorted?", checkSortedArray(arr))
arr = [5, 3, 2, 4, 1]
print("Is the array sorted?", checkSortedArray(arr))
arr = [1, 2, 2, 3, 4]
print("Is the array sorted?", checkSortedArray(arr))