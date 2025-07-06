# complexity: O(n log n)
def MergeSort():
    def merge(left, right, depth):
        print(f"{'   ' * depth}Merging: {left} and {right}")
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        print(f"{'   ' * depth}Result: {result}")
        return result

    def merge_sort(arr, depth=0):
        if len(arr) <= 1:
            return arr

        print(f"\n{'   ' * depth}Splitting: {arr}")
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid], depth + 1)
        right_half = merge_sort(arr[mid:], depth + 1)

        return merge(left_half, right_half, depth)

    return merge_sort


sample_array = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort Algorithm")
print("Unsorted array:", *sample_array)
sorted_array = MergeSort()(sample_array)
print("\nSorted array:", *sorted_array)

# Output:

# Merge Sort Algorithm
# Unsorted array: 38 27 43 3 9 82 10

# Splitting: [38, 27, 43, 3, 9, 82, 10]

#    Splitting: [38, 27, 43]

#       Splitting: [27, 43]
#       Merging: [27] and [43]
#       Result: [27, 43]
#    Merging: [38] and [27, 43]
#    Result: [27, 38, 43]

#    Splitting: [3, 9, 82, 10]

#       Splitting: [3, 9]
#       Merging: [3] and [9]
#       Result: [3, 9]

#       Splitting: [82, 10]
#       Merging: [82] and [10]
#       Result: [10, 82]
#    Merging: [3, 9] and [10, 82]
#    Result: [3, 9, 10, 82]
# Merging: [27, 38, 43] and [3, 9, 10, 82]
# Result: [3, 9, 10, 27, 38, 43, 82]

# Sorted array: 3 9 10 27 38 43 82