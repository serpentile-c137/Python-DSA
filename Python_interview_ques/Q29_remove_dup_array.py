def remove_duplicated(nums):
    n = len(nums)
    freq_map = {}

    for i in range(n):
        freq_map[nums[i]] = 0
    
    j= 0 
    for k in freq_map:
        nums[j] = k
        j += 1
    
    return j
    

nums = [1,1,1,3,4,4,7,9,9,9,10]
result = remove_duplicated(nums)
print(result)