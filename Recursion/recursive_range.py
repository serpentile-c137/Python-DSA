def recursiveRange(num):
    if num == 1:
        return num
    else:
        return num + recursiveRange(num-1)
        
        
print(recursiveRange(6)) # 21
print(recursiveRange(10)) # 55 