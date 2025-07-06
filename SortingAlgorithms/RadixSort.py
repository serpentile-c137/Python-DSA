# complexity: O(n⋅k)
def RadixSort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1  # Exponent for the current digit

    while max_num // exp > 0:
        counting = [0] * 10  # Initialize counting array for digits 0-9
        output = [0] * len(arr)  # Output array

        # Count occurrences of each digit
        for num in arr:
            index = (num // exp) % 10
            counting[index] += 1

        # Update counting array to contain actual positions
        for i in range(1, 10):
            counting[i] += counting[i - 1]

        # Build the output array
        for i in range(len(arr) - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[counting[index] - 1] = arr[i]
            counting[index] -= 1

        # Copy the output array back to the original array
        arr[:] = output[:]
        
        exp *= 10  # Move to the next digit
        print(f"After sorting by digit {exp // 10}: ", *arr)  # Print the array after each digit sort
    return arr


sample_array = [170, 45, 75, 90, 802, 24, 2, 66]
print("Radix Sort Algorithm")
print("Unsorted array:", *sample_array)
sorted_array = RadixSort(sample_array)
print("Sorted array:", *sorted_array)

# Output:

# Radix Sort Algorithm
# Unsorted array: 170 45 75 90 802 24 2 66
# After sorting by digit 1:  170 90 802 2 24 45 75 66
# After sorting by digit 10:  802 2 24 45 66 170 75 90
# After sorting by digit 100:  2 24 45 66 75 90 170 802
# Sorted array: 2 24 45 66 75 90 170 802