def largest_number(arr):
    largest = float('-inf')
    n = len(arr)

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    return largest if largest != float('-inf') else None


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Largest number in the array:", largest_number(arr))
