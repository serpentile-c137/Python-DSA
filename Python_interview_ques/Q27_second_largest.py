def second_largest(arr):
    largest = second = float('-inf')

    for i in range(len(arr)):
        largest = max(largest, arr[i])

    for i in range(len(arr)):
        if arr[i] != largest:
            second = max(second, arr[i])

    return second


arr = [12, 35, 1, 10, 34, 1]
print("Second largest element is:", second_largest(arr))