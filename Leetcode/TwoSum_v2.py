def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
        print(f"Seen so far: {seen}")
 
nums = [2, 11, 15, 7, 6]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")