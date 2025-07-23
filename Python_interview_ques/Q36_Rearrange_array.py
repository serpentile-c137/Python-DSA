def rearrangeArray(nums):
        n = len(nums)
        res = [0] * n
        pos, neg = 0, 1

        for i in range(0,n):
            if nums[i] >= 0:
                res[pos] = nums[i]
                pos += 2
            else:
                res[neg] = nums[i]
                neg += 2

        return res

nums = [3, -2, 1, -5, -1, 4, 2]
print(rearrangeArray(nums))  # Output: [3, -2, 1, -5, 4, -1, 2]