def max_consecutive_ones(nums):
    count = 0
    max_count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

nums = [1,0,1,0,0,1,1,1,1,0,1]
print(max_consecutive_ones(nums))  # Output: 4