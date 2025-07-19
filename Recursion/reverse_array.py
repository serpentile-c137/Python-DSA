def reverse_array(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array(arr, left + 1, right - 1)

arr = [5,9,8,3,6,7,1,4,2]
left = 2
right = 4
print(f"Original array: {arr}")
reverse_array(arr, left, right)
print(f"Reversed array: {arr}")