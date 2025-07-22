# Merge 2 Sorted Arrays Without Duplicates

def merge_sorted_arrays(num1, num2):
    n = len(num1)
    m = len(num2)
    res = []
    i, j = 0, 0
    while i < n and j < m:
        if nums1[i] < num2[j]:
            if len(res) == 0 or res[-1] != num1[i]:
                res.append(num1[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != num2[j]:
                res.append(num2[j])
            j += 1
        
    while i < n:
        if len(res) == 0 or res[-1] != num1[i]:
            res.append(num1[i])
        i += 1

    while j < m:
        if len(res) == 0 or res[-1] != num2[j]:
            res.append(num2[j])
        j += 1
    return res

nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]

result = merge_sorted_arrays(nums1, nums2)
print(result)  # Output: [1, 2, 3, 4, 6, 7, 8, 9, 10]