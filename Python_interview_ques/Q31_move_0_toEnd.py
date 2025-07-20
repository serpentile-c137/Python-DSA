def move_zeros_to_end(nums):
    if len(nums) == 0:
        return
    
    i=0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1

    if i == len(nums):
        return
    j = i + 1

    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    
nums = [1,2,4,0,3,0,0,3,5,1]

move_zeros_to_end(nums)
print(nums)  # Output: [1, 2, 4, 3, 5, 1, 0, 0, 0, 0]
    