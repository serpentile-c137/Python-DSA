nums = [1,2,3,1,2,1,9,9,1,2,3,4,9,1,0,2,3,4,5,6,7,8,9]

freq = {} # or freq = dict()

for i in range(len(nums)):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1

print(freq)