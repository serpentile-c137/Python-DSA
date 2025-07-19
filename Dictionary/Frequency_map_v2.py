nums = [1,2,3,1,2,1,9,9,1,2,3,4,9,1,0,2,3,4,5,6,7,8,9]

freq = {} # or freq = dict()
n = len(nums)

for i in range(n):
    freq[nums[i]] = freq.get(nums[i], 0) + 1

print(freq)