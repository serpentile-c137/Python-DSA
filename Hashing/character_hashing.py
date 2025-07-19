s = "azyxyyzaaaa"
q = ['d', 'a', 'y', 'z']

hash_list = [0] * 26

for char in s:
    ascii_val = ord(char)
    idx = ascii_val - 97
    hash_list[idx] += 1

print(hash_list)

for char in q:
    ascii_val = ord(char)
    idx = ascii_val - 97
    print(hash_list[idx])