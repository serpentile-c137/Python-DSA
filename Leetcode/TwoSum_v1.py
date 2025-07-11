def two_sum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
 
nums = [2, 11, 15, 7, 6]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")