def maxSubArray(nums):
    n = len(nums)
    max_sum = float('-inf')
    total = 0

    for i in range(n):
        total += nums[i]
        max_sum = max(max_sum, total)
        
        if total < 0:
            total = 0
    return max_sum

# def maxSubArray(nums):
#     max_sum = float('-inf')
#     current_sum = 0
#     for num in nums:
#         if current_sum < 0:
#             current_sum = num
#         else:
#             current_sum += num
        
#         # update max sum
#         max_sum = max(current_sum, max_sum)
#     return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # Output: 6