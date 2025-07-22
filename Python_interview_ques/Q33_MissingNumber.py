
# def missingNumber(nums):
#         for i in range(0,len(nums)+1):
#             # if i != len(nums)
#             if i not in nums:
#                 return i
            
def missingNumber(nums):
        return sum(range(len(nums)+1)) - sum(nums)



nums = [0, 1, 2, 3, 5]
print(missingNumber(nums))  # Output: 4