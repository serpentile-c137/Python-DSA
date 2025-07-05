# complexity: O(n^2)
def SelectionSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted array
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Pass {i+1}: ", *arr)
    return arr

arr = [64, 25, 12, 22, 11]
print("Selection Sort Algorithm")
print("Unsorted array is:", *arr)
sorted_arr = SelectionSort(arr)
print("Sorted array is:", *sorted_arr)


# Output:

# Selection Sort Algorithm
# Unsorted array is: 64 25 12 22 11
# Pass 1:  11 25 12 22 64
# Pass 2:  11 12 25 22 64
# Pass 3:  11 12 22 25 64
# Pass 4:  11 12 22 25 64
# Pass 5:  11 12 22 25 64
# Sorted array is: 11 12 22 25 64