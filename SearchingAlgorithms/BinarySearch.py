# complexity: O(log n)
def BinarySearch(arr, target): 
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Not Found"


arr = [1, 2, 3, 4, 5]
target = 3
result = BinarySearch(arr, target)
print("array: ", *arr)
print(f"Element {target} found at index: {result}")

target = 6
result = BinarySearch(arr, target)
print("array: ", *arr)
print(f"Element {target} found at index: {result}")
