# complexity: O(n^2)
def InsertionSort(arr):
    for i in range(1, len(arr)-1):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[i]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Pass {i}: ", *arr)
    return arr

# Example usage

arr = [64, 25, 12, 22, 11]
print("Insertion Sort Algorithm")
print("Unsorted array is:", *arr)
sorted_arr = InsertionSort(arr)
print("Sorted array is:", sorted_arr)

# Output:

# Insertion Sort Algorithm
# Unsorted array is: 64 25 12 22 11
# Pass 1:  64 25 12 22 11
# Pass 2:  64 25 12 22 11
# Pass 3:  64 25 12 22 11
# Sorted array is: [64, 25, 12, 22, 11]