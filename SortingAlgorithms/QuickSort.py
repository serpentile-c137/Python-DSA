# complexity: O(n log n) on average, O(n^2) in the worst case
def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # mid element as pivot
        
        # Divide array into three parts:
        left = [x for x in arr if x < pivot] # Elements less than pivot
        middle = [x for x in arr if x == pivot] # Elements equal to pivot
        right = [x for x in arr if x > pivot] # Elements greater than pivot
        
        # Recursively sort left and right partitions, then combine with middle
        print(f"array: {arr} \n\tPivot: {pivot}, \tLeft: {left}, \tMiddle: {middle}, \tRight: {right}")
        return QuickSort(left) + middle + QuickSort(right)
    

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Quick Sort Algorithm")
print("Unsorted array is:", *arr)
sorted_arr = QuickSort(arr) 
print("Sorted array is:", *sorted_arr)

# Output:

# Quick Sort Algorithm
# Unsorted array is: 64 34 25 12 22 11 90
# array: [64, 34, 25, 12, 22, 11, 90] 
#         Pivot: 12,      Left: [11],     Middle: [12],   Right: [64, 34, 25, 22, 90]
# array: [64, 34, 25, 22, 90] 
#         Pivot: 25,      Left: [22],     Middle: [25],   Right: [64, 34, 90]
# array: [64, 34, 90] 
#         Pivot: 34,      Left: [],       Middle: [34],   Right: [64, 90]
# array: [64, 90] 
#         Pivot: 90,      Left: [64],     Middle: [90],   Right: []
# Sorted array is: 11 12 22 25 34 64 90