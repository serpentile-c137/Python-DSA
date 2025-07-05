# complecity O(n^2)
def BubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Pass {i+1}: ", *arr)  # Print the array after each pass
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", *arr)
sorted_arr = BubbleSort(arr)
print("Sorted array is:", *sorted_arr)
