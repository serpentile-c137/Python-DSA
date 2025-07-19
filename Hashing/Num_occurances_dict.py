#constraints: 
# 1 <= n[i] <= 10
# n can have 10^8 elements
# m can have 10^8 elements


n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_dict = {}
print(hash_dict)

for i in range(len(n)):
    hash_dict[n[i]] = hash_dict.get(n[i], 0) + 1
print(hash_dict)

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_dict.get(num, 0))