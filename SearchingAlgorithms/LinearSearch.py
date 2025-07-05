def LinearSearch(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return "Not Found"

arr = [1, 2, 3, 4, 5]
target = 3
result = LinearSearch(arr, target)
print("array: ",*arr)
print(f"Element {target} found at index: {result}")

target = 6
result = LinearSearch(arr, target)
print("array: ",*arr)
print(f"Element {target} found at index: {result}")