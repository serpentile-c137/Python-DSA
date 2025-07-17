def findMaxNumber(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], findMaxNumber(arr, n-1))
    
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
n = len(arr)
print(f"The maximum number in the array is: {findMaxNumber(arr, n)}")