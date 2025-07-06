# complexity: O(n + k), where n is the number of elements in the input array and k is the range of the input values.
def CountingSort(arr):
    if not arr:
        return arr
   
    # Find the maximum element in the array
    max_val = max(arr)

    # Create a count array with size of max_val + 1
    count = [0] * (max_val + 1)

    # Count occurrences of each element
    for num in arr:
        count[num] += 1

    # Build the sorted array
    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1
        print(f"Pass {i}: ", *arr)
    return arr

# Example usage
arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print("Counting Sort Algorithm")
print("Unsorted array is:", *arr)
sorted_arr = CountingSort(arr)
print("Sorted array is:", sorted_arr)

# Output:

# Counting Sort Algorithm
# Unsorted array is: 4 2 2 6 3 3 1 6 5 2 3
# Pass 0:  4 2 2 6 3 3 1 6 5 2 3
# Pass 1:  1 2 2 6 3 3 1 6 5 2 3
# Pass 2:  1 2 2 2 3 3 1 6 5 2 3
# Pass 3:  1 2 2 2 3 3 3 6 5 2 3
# Pass 4:  1 2 2 2 3 3 3 4 5 2 3
# Pass 5:  1 2 2 2 3 3 3 4 5 2 3
# Pass 6:  1 2 2 2 3 3 3 4 5 6 6
# Sorted array is: [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]